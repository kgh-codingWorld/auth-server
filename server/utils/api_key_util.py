import secrets, logging
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import APIKey
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def validate_api_key(api_key: str, db: Session):
    api_key_data = db.query(APIKey).filter(APIKey.api_key == api_key).first()
    if not api_key_data:
        logger.warning("유효하지 않은 API Key")
        raise HTTPException(status_code=403, detail="유효하지 않은 API Key")

def create_api_key():
    return secrets.token_hex(32)

def save_api_key(user_id: int, api_key: str, db: Session):
    try:
        existing_key = db.query(APIKey).filter(APIKey.api_key == api_key).first()
        if existing_key:
            logger.warning(f"사용자 {user_id}는 이미 API Key를 발급받음: {existing_key.api_key}")
            raise HTTPException(status_code=400, detail="이미 발급 받은 키가 존재합니다.")
        expires_at = datetime.now() + timedelta(days=30)
        new_api_key = APIKey(user_id=user_id, api_key=api_key, expires_at=expires_at)
        db.add(new_api_key)
        db.commit()
        return new_api_key
    except Exception as e:
        db.rollback()
        logger.exception(f"API Key 저장 중 오류 발생: {e}")
        raise Exception("API Key 저장 중 오류 발생")

def get_api_key_id_by_user_id(user_id:int, db: Session):
    api_key_data = db.query(APIKey).filter(APIKey.user_id == user_id).first()
    if not api_key_data:
        logger.warning("존재하지 않는 API Key")
        raise HTTPException(status_code=403, detail="존재하지 않는 API Key")
    return api_key_data.id