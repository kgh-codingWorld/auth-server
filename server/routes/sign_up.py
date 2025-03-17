import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.configs.database import get_db
from server.models.request_model import SignUpRequest
from server.utils.sign_up_util import validate_signup_request, check_existing_user, create_new_user

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/signup",
    tags=["User Resgistration"]
)

@router.post("/")
async def sign_up(request: SignUpRequest, db: Session = Depends(get_db)):
    try:
        validate_signup_request(request)
        check_existing_user(request.username, db)
        create_new_user(request, db)
        return {"message": "회원가입 성공"}
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.exception(f"회원가입 중 예상치 못한 오류 발생: {e}")
        raise HTTPException(status_code=500, detail="회원가입 중 오류가 발생했습니다.") from e