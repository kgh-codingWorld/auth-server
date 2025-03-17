import logging
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import UserFeature

logger = logging.getLogger(__name__)

# 사용자 기능 접근 권한 확인
def check_user_feature_access(user_id: int, feature_id: int, db: Session):
    user_faeture = db.query(UserFeature).filter(UserFeature.user_id == user_id, UserFeature.feature_id == feature_id).first()
    if not user_faeture:
        logger.warning(f"{user_id}는 {feature_id}기능에 대한 접근 권한 없음")
        raise HTTPException(status_code=403, detail="이 기능에 대한 접근 권한이 없습니다.")