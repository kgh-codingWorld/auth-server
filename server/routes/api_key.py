from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from server.utils.access_token_util import validate_access_token
from server.utils.api_key_util import create_api_key, save_api_key

router = APIRouter(
    prefix="/api-key",
    tags=["API Key Management"]
)

# Access Token을 확인해 API Key를 발급 → API_KEYS에 저장됨
@router.post("/generate")
async def generate_api_key(access_token: str = Header(None, alias="Access-Token"), db: Session = Depends(get_db)):
    user_id = validate_access_token(access_token, db)
    print(f"아이디 가져옴")
    api_key = create_api_key()
    print(f"가져온 걸로 키 생성함")
    save_api_key(user_id, api_key, db)
    print(f"키 저장함")
    return {"message": "API Key 발급 성공", "api_key": api_key}
