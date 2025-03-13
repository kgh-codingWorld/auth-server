from fastapi import APIRouter, HTTPException, Header, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import APIKey, AccessToken
import secrets
from datetime import datetime, timedelta

router = APIRouter()

# Access Token을 확인해 API Key를 발급 → API_KEYS에 저장됨
@router.post("/generate-api-key")
async def generate_api_key(access_token: str = Header(None, alias="Access-Token"), db: Session = Depends(get_db)):
    token_data = db.query(AccessToken).filter(AccessToken.token == access_token).first()

    if not token_data or token_data.expires_at < datetime.now():
        raise HTTPException(status_code=400, detail="유효하지 않은 토큰")

    api_key = secrets.token_hex(32)
    expires_at = datetime.now() + timedelta(days=30)

    new_api_key = APIKey(user_id=token_data.user_id, api_key=api_key, expires_at=expires_at)
    db.add(new_api_key)
    db.commit()

    return {"message": "API Key 발급 성공", "api_key": api_key}
