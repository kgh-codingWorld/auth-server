import secrets # 암호화 키, 토큰, 비밀번호, API 키 생성하는 Python 내장 모듈
from fastapi import APIRouter, HTTPException # FastAPI 라우팅 및 예외처리 모듈
from typing import Dict # 타입 힌트를 위한 Dict
from configs.config import USERS
from models.response_model import LoginResponse
from models.request_model import LoginRequest
from utils.password_hash import hash_password

# FastAPI 라우터 생성(각 API 엔드포인트를 정의하는 객체)
router = APIRouter()

# Token 저장
ACCESS_TOKENS: Dict[str, str] = {}

# 로그인 API 엔드포인트(사용자가 로그인하면 Access Token을 발급하는 기능)
@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    username = request.username # 요청에서 사용자명 가져오기
    password = request.password # 요청에서 비밀번호 가져오기
    if request.username in USERS: # 입력된 아이디가 존재하는지 확인
        hashed_pw = hash_password(password) # 입력된 비밀번호를 해싱
        if USERS[username] == hashed_pw: # 해싱된 비밀번호가 저장된 값과 일치하는지 확인
            access_token = secrets.token_hex(16) # 16바이트 랜덤 API Key 생성
            ACCESS_TOKENS[access_token] = username # API Key 저장 / ACCESS_TOKENS[username] = access_token -> 사용자명을 키로 지정하고 access_token을 값으로 저장해놓고 api_key.py에서 token을 키로해서 값을 찾으려니까 안 찾아짐
            return LoginResponse(message="인증 성공", access_token=access_token)
        
    raise HTTPException(status_code=401, detail="인증 실패: ID 또는 비밀번호가 잘못되었습니다.")