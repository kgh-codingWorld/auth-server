import logging
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import User
from ..models.request_model import SignUpRequest
from ..utils.password_hash import hash_password

# 로깅 설정
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/sign-up")
async def sign_up(request: SignUpRequest, db: Session = Depends(get_db)):
    try:
        if not request.username or not request.password:
            logger.warning(f"빈 요청")
            return JSONResponse(status_code=401, content={"detail": "아이디 또는 비밀번호를 입력하세요."})
        # 아이디 중복 체크
        existing_user = db.query(User).filter(User.username == request.username).first()
        if existing_user:
            logger.warning(f"회원가입 실패: 이미 존재하는 아이디 - {request.username}")
            return JSONResponse(status_code=400, content={"detail": "이미 존재하는 아이디입니다."})

        # 새 사용자 추가
        new_user = User(username=request.username, password=hash_password(request.password), is_admin=request.is_admin)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        logger.info(f"회원가입 성공: {request.username}")

        return JSONResponse(status_code=200, content={"message": "회원가입 성공", "is_admin": request.is_admin})
    
    except Exception as e:
        logger.exception(f"회원가입 중 서버 내부 오류 발생: {e}")
        return JSONResponse(status_code=500, content={"detail": "서버 내부 오류가 발생했습니다."})
