import hashlib                              # SHA, MD5 등의 해시 알고리즘 제공하는 Python 내장 라이브러리(암호화 또는 무결성 검증)
import secrets                              # 암호화 키, 토큰, 비밀번호, API 키 생성하는 Python 내장 모듈
from fastapi import FastAPI, HTTPException
import gradio as gr

app = FastAPI()

# 하드코딩된 사용자 정보 (SHA-256으로 해싱된 비밀번호 저장)
USERS = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
    "user3": hashlib.sha256("password3".encode()).hexdigest(),
}

# API Key 저장
API_KEYS = {}

# 비밀번호 암호화
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@app.post("/login")
def login(username: str, password: str):
    hashed_pw = hash_password(password)
    
    if username in USERS and USERS[username] == hashed_pw:
        api_key = secrets.token_hex(16) # 16바이트 랜덤 API Key 생성
        API_KEYS[username] = api_key    # API Key 저장
        return {"message": "인증 성공", "api_key": api_key}
    else:
        raise HTTPException(status_code=401, detail="인증 실패: ID 또는 비밀번호가 잘못되었습니다.")

def authenticate(username, password):
    try:
        response = login(username, password)
        return f"인증 성공, API Key: {response['api_key']}"
    except HTTPException as e:
        return f"인증 실패: {e.detail}"

# Gradio UI
iface = gr.Interface(
    fn=authenticate,
    inputs=["text", "text"],
    outputs="text",
    title="인증 시스템",
    description="ID와 비밀번호를 입력하면 API Key를 발급합니다."
)

if __name__ == "__main__":
    iface.launch()