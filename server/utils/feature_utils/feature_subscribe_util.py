from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import UserFeature
from server.utils.feature_utils.feature_query import get_feature_id_by_name
from server.utils.api_key_util import get_api_key_id_by_user_id
import logging

logger = logging.getLogger(__name__)

def add_feature_subscribe(user_id: int, feature_name: str, api_key: str, db: Session):
    try:
        feature_id = get_feature_id_by_name(feature_name, db)
        api_key_id = get_api_key_id_by_user_id(user_id, db)
        if had_subscription is None:
            new_subsribe = UserFeature(user_id=user_id, feature_id=feature_id, api_key_id=api_key_id)
            db.add(new_subsribe)
            db.commit()
            db.refresh(new_subsribe)
            logger.info(f"{user_id}가 기능 {feature_name}를 구독함")

            return {"message": f"기능 {feature_name} 구독 성공"}
    except Exception as e:
        db.rollback()
        logger.exception(f"기능 구독 중 오류 발생: {e}")
        raise Exception("기능 구독 중 오류 발생")
    
def had_subscription(user_id: int, feature_name: str, db: Session):
    feature_id = get_feature_id_by_name(feature_name, db)
    had_subscribe = db.query(UserFeature).filter(UserFeature.user_id == user_id, UserFeature.feature_id == feature_id).first()
    if had_subscribe:
        logger.warning(f"{user_id}는 이미 해당 {feature_name}를 구독함")
        raise HTTPException(status_code=400, detail="이미 해당 기능을 구독하였습니다.")
    return had_subscribe is not None