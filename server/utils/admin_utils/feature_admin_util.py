import logging
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.models import Feature, User
from server.models.request_model import FeatureRequest

logger = logging.getLogger(__name__)

# 관리자 권한 체크
def check_admin_permissions(user: User):
    logger.info(f"권한 체크: {user.is_admin}")
    logger.info(f"테이블 아이디: {user.id}")
    logger.info(f"이름: {user.username}")
    if not user.is_admin:
        logger.warning("일반회원, 관리자만 접근 가능")
        raise HTTPException(status_code=403, detail="관리자만 접근 가능합니다.")
    
# 기능 요청 유효성 검사
def validate_feature_request(request: FeatureRequest):
    if not request.name or not request.description:
        logger.warning("기능 이름 또는 설명이 비어 있음")
        raise HTTPException(status_code=400, detail="기능 이름과 설명을 입력해야 합니다.")

# 중복 기능 확인    
def check_existing_feature(request: FeatureRequest, db: Session):
    existing_feature = db.query(Feature).filter(Feature.name == request.name).first()
    if existing_feature:
        logger.warning("이미 존재하는 기능")
        raise HTTPException(status_code=400, detail="이미 존재하는 기능입니다.")
    
# 기능 추가
def add_new_feature(request: FeatureRequest, db: Session):
    try:
        new_feature = Feature(name=request.name, description=request.description)
        db.add(new_feature)
        db.commit()
        db.refresh(new_feature)
        logger.info("기능 추가 성공")
        return new_feature
    except Exception as e:
        db.rollback()
        logger.exception(f"기능 추가 중 오료 발생: {e}")
        raise HTTPException(status_code=500, detail="기능 추가 중 오류가 발생했습니다.")