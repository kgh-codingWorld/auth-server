import secrets, logging
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import AccessToken, User
from server.models.request_model import LoginRequest
from server.utils.password_hash_util import hash_password
from server.utils.access_token_util import validate_access_token
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

# 사용자 테이블 아이디 기반 조회
def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logger.warning(f"해당 {user_id}를 찾을 수 없음")
        raise HTTPException(status_code=404, detail="해당 사용자를 찾을 수 없습니다.")
    return user

# 로그인 요청 유효성 검사
def validate_login_request(request: LoginRequest):
    if not request.username or not request.password:
        logger.warning("입력된 값 없음")
        raise HTTPException(status_code=400, detail="ID 또는 비밀번호를 입력해 주세요.")

# 사용자 인증(사용자 아이디) - 로그인 시 사용
def authenticate_user(request: LoginRequest, db: Session):
    user = db.query(User).filter(User.username == request.username).first()
    if not user or user.password != hash_password(request.password):
        logger.warning("None 값 반환")
        raise HTTPException(status_code=401, detail="잘못된 아이디 또는 비밀번호입니다.")
    return user

# 엑세스 토큰 생성
def create_access_token():
    return secrets.token_hex(16)

# 엑세스 토큰 저장
def save_access_token(user_id: int, access_token: str, db: Session):
    try:
        expires_at = datetime.now() + timedelta(hours=1)
        new_token = AccessToken(user_id=user_id, token=access_token, expires_at=expires_at)
        db.add(new_token)
        db.commit()
        return new_token
    except Exception as e:
        db.rollback()
        logger.exception(f"엑세스 토큰 저장 중 오류 발생: {e}")
        raise Exception("엑세스 토큰 저장 중 오류 발생")
    
def get_user_by_access_token(access_token: str, db: Session):
    if not access_token:
        logger.warning("엑세스 토큰이 없음")
        raise HTTPException(status_code=401, detail="엑세스 토큰이 필요합니다.")
    token_data = validate_access_token(access_token, db)
    user = get_user_by_id(token_data.user_id, db)

    return user.id