from fastapi import APIRouter, HTTPException, Header, Depends
from sqlalchemy.orm import Session
from db.configs.database import get_db
from db.models import AccessToken, APIKey, Feature, UserFeature

router = APIRouter()

@router.get("/access-feature/{feature_name}")
async def access_feature(
    feature_name: str,
    access_token: str = Header(None, alias="Access-Token"), 
    api_key: str = Header(None, alias="API-Key"),
    db: Session = Depends(get_db)):

    token_data = db.query(AccessToken).filter(AccessToken.token == access_token).first()
    if not token_data:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰")

    user_id = token_data.user_id # access_token 테이블의 user_id 가져오기

    api_key_data = db.query(APIKey).filter(APIKey.api_key == api_key).first()
    if not api_key_data:
        raise HTTPException(status_code=403, detail="유효하지 않은 API Key")
    
    feature = db.query(Feature).filter(Feature.name == feature_name).first()
    if not feature:
        raise HTTPException(status_code=404, detail="해당 기능이 존재하지 않습니다.")

    user_feature = db.query(UserFeature).filter(
        UserFeature.user_id == user_id,
        UserFeature.feature_id == feature.id).first() 

    # 사용자 접근권한 확인
    if not user_feature:
        raise HTTPException(status_code=403, detail="이 기능에 대한 접근 권한이 없습니다.")

    return {"message": "기능 접근 허용됨"}
