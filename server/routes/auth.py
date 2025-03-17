import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import User, AccessToken
from server.models.request_model import LoginRequest
from server.utils.auth_util import validate_login_request, authenticate_user, create_access_token, save_access_token

logger = logging.getLogger(__name__)

# FastAPI 라우터 생성(각 API 엔드포인트를 정의하는 객체)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# 로그인 API 엔드포인트(사용자가 로그인하면 Access Token을 발급하는 기능)
@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    
    # 로그인 요청 데이터 검증
    error_response = validate_login_request(request)
    if error_response:
        return error_response
    
    # 사용자 인증
    user = authenticate_user(request, db)

    # 토큰 생성 및 저장
    access_token = create_access_token()
    save_access_token(user.id, access_token, db)

    return {"message": "인증 성공", "access_token":access_token, "is_admin":user.is_admin}
    