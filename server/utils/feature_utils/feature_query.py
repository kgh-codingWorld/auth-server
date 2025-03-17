import logging
import gradio as gr
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import Feature

logger = logging.getLogger(__name__)

# 기능 리스트 조회
def get_feature_list(db: Session):
    # 모든 데이터를 한꺼번에 가져오므로 DB 연결 문제, 네트워크 오류 등 발생 가능성 있어 try-except 사용
    try:
        features = db.query(Feature.name).all()
        feature_list = [feature[0] for feature in features]
        logger.info("기능 리스트 조회 성공")
        return feature_list
    except Exception as e:
        logger.exception(f"기능 리스트 조회 중 오류 발생: {e}")
        raise Exception("기능 리스트를 가져오는 중 서버 내부 오류 발생")

# 기능 새로고침 후 업데이트
def update_feature_list():
    try:
        db = next(get_db()) 
        feature_list = get_feature_list(db)
        return gr.update(choices=feature_list)  # Gradio UI 업데이트
    except Exception as e:
        logger.exception(f"기능 업데이트 중 오류 발생: {e}")
        raise Exception("기능 업데이트 중 서버 내부 오류 발생")

# def get_feature_by_id(id: int, db: Session):
#     feature = db.query(Feature).filter(Feature.id == id).first()
#     if not feature:
#         logger.warning("존재하지 않는 기능")
#         raise HTTPException(status_code=404, detail="해당 기능이 존재하지 않습니다.")
#     return feature.id

# 기능 존재 여부 확인
def get_feature_id_by_name(name: str, db: Session):
    feature = db.query(Feature).filter(Feature.name == name).first()
    if not feature:
        logger.warning("존재하지 않는 기능")
        raise HTTPException(status_code=404, detail=f"해당 기능 '{name}'이 존재하지 않습니다.")
    return feature.id