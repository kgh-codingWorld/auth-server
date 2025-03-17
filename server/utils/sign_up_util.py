import logging
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import User
from server.models.request_model import SignUpRequest
from server.utils.password_hash_util import hash_password

logger = logging.getLogger(__name__)

# 회원가입 요청 유효성 검사
def validate_signup_request(request: SignUpRequest):
    if not request.username or not request.password:
        logger.warning("입력된 값 없음")
        raise HTTPException(status_code=400, detail="ID 또는 비밀번호를 입력해 주세요.")

# 중복 아이디 확인    
def check_existing_user(username: str, db: Session):
    # 단순(한 개) 데이터 조회는 try-except이 필요 없음
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        logger.warning(f"회원가입 실패: 이미 존재하는 아이디 - {username}")
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다.")

# 회원가입    
def create_new_user(request: SignUpRequest, db: Session):
    try:
        new_user = User(username=request.username, password=hash_password(request.password), is_admin=request.is_admin)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.info(f"회원가입 성공: {request.username}")
        return new_user
    except Exception as e:
        db.rollback()
        logger.exception(f"회원가입 중 오류 발생: {e}")
        raise Exception("회원가입 중 오류 발생")