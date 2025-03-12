import hashlib                                  # SHA, MD5 등의 해시 알고리즘 제공하는 Python 내장 라이브러리(암호화 또는 무결성 검증)
import secrets                                  # 암호화 키, 토큰, 비밀번호, API 키 생성하는 Python 내장 모듈
from fastapi    import APIRouter, HTTPException # FastAPI 라우팅 및 예외처리 모듈
from pydantic   import BaseModel, Field         # 데이터 검증을 위한 Pydantic 모델
from typing     import Dict, List               # 타입 힌트를 위한 Dict, List 모듈

# FastAPI 라우터 생성(각 API 엔드포인트를 정의하는 객체)
router = APIRouter()

# Token 저장
ACCESS_TOKENS: Dict[str, str] = {}

# 유저별 접근 가능한 기능
USER_PERMISSIONS: Dict[str, List[str]] = {
    "user1": ["feature1", "feature2", "feature3"],
    "user2": ["feature1", "feature3"],
    "user3": ["feature2"],
    "user4": [] #접근 불가
}

# 하드코딩된 사용자 정보 (SHA-256으로 해싱된 비밀번호 저장)
USERS = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
    "user3": hashlib.sha256("password3".encode()).hexdigest(),
    "user4": hashlib.sha256("password4".encode()).hexdigest()
}

# 로그인 요청 데이터 모델
class LoginRequest(BaseModel):
    username: str = Field(..., example="user1")
    password: str = Field(..., example="password1")

# 로그인 응답 데이터 모델
class LoginResponse(BaseModel):
    message: str                        # 성공 또는 실패 메시지
    access_token: str | None = None


# 비밀번호 암호화
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# 로그인 API 엔드포인트(사용자가 로그인하면 Access Token을 발급하는 기능)
@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    username = request.username                       # 요청에서 사용자명 가져오기
    password = request.password                       # 요청에서 비밀번호 가져오기
    if request.username in USERS:                     # 입력된 아이디가 존재하는지 확인
        hashed_pw = hash_password(password)           # 입력된 비밀번호를 해싱
        if USERS[username] == hashed_pw:              # 해싱된 비밀번호가 저장된 값과 일치하는지 확인
            access_token = secrets.token_hex(16)      # 16바이트 랜덤 API Key 생성
            ACCESS_TOKENS[access_token] = username    # API Key 저장 / ACCESS_TOKENS[username] = access_token -> 사용자명을 키로 지정하고 access_token을 값으로 저장해놓고 api_key.py에서 token을 키로해서 값을 찾으려니까 안 찾아짐
            return LoginResponse(message="인증 성공", access_token=access_token)
        
    raise HTTPException(status_code=401, detail="인증 실패: ID 또는 비밀번호가 잘못되었습니다.")