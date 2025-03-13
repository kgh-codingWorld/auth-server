import gradio as gr
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import Feature

def get_feature_list(db: Session):
    features = db.query(Feature.name).all()
    return [feature[0] for feature in features] # 리스트로 변환

def update_feature_list():
    db = next(get_db())  # DB 세션 열기
    feature_list = get_feature_list(db)  # 최신 기능 목록 가져오기
    return gr.update(choices=feature_list)  # Gradio UI 업데이트