import logging
from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import Feature, User
from ..models.request_model import FeatureRequest
from fastapi.responses import JSONResponse
from ..utils.admin_util import check_admin

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/admin/add-feature")
async def add_feature(
    request: FeatureRequest, 
    db: Session = Depends(get_db),
    access_token: str = Header(None)
):
    try:
        user_id_data = db.query(User).filter(User.username == request.user_id).first()
        print(f"권한 확인: {user_id_data.is_admin}")
        if not access_token:
            logger.warning(f"토큰 없음, 로그아웃 상태")
            return JSONResponse(status_code=401, content={"detail":"로그인을 진행해 주세요."})
        
        if user_id_data.is_admin is False:
            logger.warning(f"일반회원")
            return JSONResponse(status_code=401, content={"detail":"관리자만 접근 가능합니다."})


        print(f"기능 이름: {request.name}")
        print(f"기능 설명: {request.description}")
        if not request.name or not request.description or request.user_id:
            logger.warning(f"아이디 또는 기능 이름 또는 설명 비어있음")
            return JSONResponse(status_code=400, content={"detail": "아이디 및 기능 이름 또는 설명을 입력해야 합니다."})

        existing_feature = db.query(Feature).filter(Feature.name == request.name).first()
        if existing_feature:
            logger.warning(f"이미 존재하는 기능")
            return JSONResponse(status_code=400, content={"detail":"이미 존재하는 기능입니다."})

        # 새 사용자 추가
        new_feature = Feature(name=request.name, description=request.description)
        db.add(new_feature)
        db.commit()
        db.refresh(new_feature)

        logger.info("기능 추가 성공")

        return JSONResponse(status_code=200, content={"message": "기능 추가 성공"})
    except Exception as e:
        logger.exception(f"기능 추가 중 서버 내부 오류 발생: {e}")
        return JSONResponse(status_code=500, content={"detail": "서버 내부 오류가 발생했습니다."})