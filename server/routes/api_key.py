from fastapi import APIRouter, HTTPException, Header
import secrets
from routes.auth import ACCESS_TOKENS
from typing import Dict

router = APIRouter()

API_KEYS: Dict[str, str] = {}

# Access Token을 확인해 API Key를 발급 → API_KEYS에 저장됨
@router.post("/generate-api-key")
async def generate_api_key(access_token: str = Header(None, alias="Access-Token")):
    if not access_token:
        raise HTTPException(status_code=400, detail="토큰이 제공되지 않았습니다.")

    if access_token not in ACCESS_TOKENS:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰")

    username = ACCESS_TOKENS[access_token] # 토큰을 키로 사용하여 유저명 가져오기
    api_key = secrets.token_hex(32)
    API_KEYS[username] = api_key           # API Key 저장
    return {"message": "API Key 발급 성공", "api_key": api_key}
