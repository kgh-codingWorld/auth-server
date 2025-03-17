import logging
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import AccessToken
from datetime import datetime

logger = logging.getLogger(__name__)

def validate_access_token(access_token: str, db: Session):
    token_data = db.query(AccessToken).filter(AccessToken.token == access_token).first()
    if not token_data or token_data.expires_at < datetime.now():
        logger.warning("유효하지 않은 토큰")
        raise HTTPException(status_code=401, detail="로그아웃 상태입니다. 로그인 또는 회원가입을 진행해 주세요.")
    logger.info(f"유효한 토큰 확인됨 - user_id: {token_data.user_id}")
    return token_data.user_id