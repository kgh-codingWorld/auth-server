from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import User, AccessToken
from datetime import datetime

def check_admin(access_token: str, db: Session = Depends(get_db)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Access-Token이 필요합니다.")

    token_data = db.query(AccessToken).filter(AccessToken.token == access_token).first()
    if not token_data:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")

    if token_data.expires_at < datetime.now():
        raise HTTPException(status_code=401, detail="토큰이 만료되었습니다.")

    user = db.query(User).filter(User.id == token_data.user_id).first()
    if not user:
        print(f"사용자 정보 없음: user_id={token_data.user_id}")

    if not user.is_admin:
        print(f"관리자 권한 없음: user_id={user.id}, username={user.username}")
        raise HTTPException(status_code=403, detail="권한이 없습니다.")

    print(f"관리자 확인 완료: user_id={user.id}, username={user.username}")

    return user