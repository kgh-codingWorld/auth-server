## 📂 `server/README.md`

# Authentication Server (FastAPI)

이 폴더는 **FastAPI 기반 인증 서버**를 포함하고 있습니다.

---

## 📌 개요
- **백엔드 프레임워크**: FastAPI
- **인증 방식**: Access Token, API Key
- **ORM**: SQLAlchemy
- **배포 환경**: Docker, Uvicorn

---

## 📂 폴더 구조
```bash
server/
│── error/
│   ├── exception_handler.py   # 예외 처리
│── models/
│   ├── request_model.py       # Pydantic 데이터 모델 정의
│   ├── response_model.py      # API 응답 모델 정의
│── routes/
│   ├── api_key.py             # API Key 관련 라우트
│   ├── auth.py                # 로그인/회원가입 라우트
│   ├── feature_access.py      # 기능 접근 라우트
│   ├── feature_admin.py       # 관리자 기능 추가 라우트
│   ├── feature_subscribe.py   # 기능 구독 라우트
│── utils/
│   ├── access_token_util.py   # Access Token 관련 유틸리티
│   ├── api_key_util.py        # API Key 관련 유틸리티
│   ├── auth_util.py           # 인증 관련 유틸리티
│── main.py                    # FastAPI 실행 엔트리포인트

```

## 🚀 실행 방법

### 1️. 환경 설정 및 패키지 설치

```bash
bash
복사편집
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

```

### 2️. FastAPI 서버 실행

```bash
bash
복사편집
uvicorn server.main:app --host 0.0.0.0 --port 8000

```

### 3️. API 문서 확인

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## 🔑 인증 시스템

### 1️. 회원가입 API

```
POST /signup/

```

```json
{
  "username": "testuser",
  "password": "password123",
  "is_admin": false}

```

### 2️. 로그인 API

```

POST /auth/login

```

```json

{
  "username": "testuser",
  "password": "password123"
}

```

### 응답 예시

```json
json
복사편집
{
  "access_token": "abcd1234efgh5678",
  "is_admin": false}

```

---

## 🔧 문제 해결
