from fastapi import APIRouter, HTTPException, Header
from routes.auth import ACCESS_TOKENS, USER_PERMISSIONS
from routes.api_key import API_KEYS

router = APIRouter()

@router.get("/access-feature/{feature_name}")
async def access_feature(
    feature_name: str,
    access_token: str = Header(None, alias="Access-Token"), 
    api_key: str = Header(None, alias="API-Key")):

    if access_token not in ACCESS_TOKENS:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰")

    username = ACCESS_TOKENS[access_token]

    if API_KEYS.get(username) != api_key:
        raise HTTPException(status_code=403, detail="유효하지 않은 API Key")
    
    if feature_name not in USER_PERMISSIONS.get(username, []):
        raise HTTPException(status_code=403, detail="이 기능에 대한 접근 권한이 없습니다.")

    return {"message": "기능 접근 허용됨"}
