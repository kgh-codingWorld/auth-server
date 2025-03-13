import secrets, logging
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import User, AccessToken
from fastapi.responses import JSONResponse
from ..models.request_model import LoginRequest
from datetime import datetime, timedelta
from ..utils.password_hash import hash_password

logger = logging.getLogger(__name__)

# FastAPI 라우터 생성(각 API 엔드포인트를 정의하는 객체)
router = APIRouter()

# 로그인 API 엔드포인트(사용자가 로그인하면 Access Token을 발급하는 기능)
@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    if not request.username or not request.password:
        logger.warning("입력된 값 없음")
        return JSONResponse(status_code=401, content={"detail": "ID 또는 비밀번호를 입력해 주세요."})
    
    user = db.query(User).filter(User.username == request.username).first()
    if not user or user.password != hash_password(request.password): 
        return JSONResponse(status_code=401, content={"detail": "인증 실패: ID 또는 비밀번호가 잘못되었습니다."})
        
    expires_at = datetime.now() + timedelta(hours=1)

    access_token = secrets.token_hex(16)
    new_token = AccessToken(user_id=user.id, token=access_token, expires_at=expires_at)
    db.add(new_token)
    db.commit()

    return JSONResponse(status_code=200, content={"message": "인증 성공", "access_token":access_token, "is_admin":user.is_admin})
    