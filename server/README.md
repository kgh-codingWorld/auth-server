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

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

```

### 2️. FastAPI 서버 실행

```bash

uvicorn server.main:app --host 0.0.0.0 --port 8000

```

### 3️. API 문서 확인

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## 🔑 인증 시스템

### 1️. 회원가입
요청 예시:
```
POST /signup/

```

```json
{
  "username": "testuser",
  "password": "password123",
  "is_admin": false
}
```
응답 예시:
```json
{
  "message": "회원가입 성공"
}
```

### 2️. 로그인
요청 예시:
```

POST /auth/login

```

```json

{
  "username": "testuser",
  "password": "password123"
}

```
응답 예시:

```json

{
  "message": "인증 성공",
  "access_token": "abcd1234efgh5678",
  "is_admin": false}

```
### 3️. Access Token 검증 API
Access Token이 유효한지 확인하는 API입니다.

요청 예시:
```http
POST /auth/token/validate
```
```bash
curl -X POST "http://127.0.0.1:8000/auth/token/validate" \
     -H "Access-Token: abcd1234efgh5678"
```
응답 예시 (토큰이 유효할 때):
```json
{
  "message": "Access Token이 유효합니다."
}
```
응답 예시 (토큰이 만료되었을 때):
```json
{
  "detail": "로그아웃 상태입니다. 로그인 또는 회원가입을 진행해 주세요."
}
```
4️. API Key 발급 API
사용자가 Access Token을 이용하여 API Key를 요청하면, 새로운 API Key를 발급받을 수 있습니다.

요청 예시:
```http
POST /api-key/generate
```
```bash
curl -X POST "http://127.0.0.1:8000/api-key/generate" \
     -H "Access-Token: abcd1234efgh5678"
```
응답 예시:
```json
{
  "message": "API Key 발급 성공",
  "api_key": "1234567890abcdef"
}
```
5. 기능 구독 API
사용자가 특정 기능을 구독할 수 있습니다.

요청 예시:
```http
POST /feature/subscribe/{feature_name}
```
```bash
curl -X POST "http://127.0.0.1:8000/feature/subscribe/예제기능" \
     -H "Access-Token: abcd1234efgh5678" \
     -H "API-Key: 1234567890abcdef"
```
응답 예시:
```json
{
  "message": "기능 예제기능 구독 성공"
}
```
6️. 기능 접근 API
구독한 기능에 대한 접근 권한을 확인합니다.

요청 예시:
```http
POST /feature/access/{feature_name}
```
```bash
curl -X POST "http://127.0.0.1:8000/feature/access/예제기능" \
     -H "Access-Token: abcd1234efgh5678" \
     -H "API-Key: 1234567890abcdef"
```
응답 예시:
```json
{
  "message": "기능 접근 허용됨"
}
```
---

## 문제 해결
| **문제** | **해결 방법** |
| --- | --- |
| FastAPI 서버 실행 오류 | `.env` 파일이 존재하는지 확인하고 환경 변수 설정 |
| 로그인 시 `401 Unauthorized` 오류 발생 | 데이터베이스에 사용자가 존재하는지 확인 |
| Access Token 검증 실패 | 로그인하여 새로운 토큰을 발급받아야 함 |
| API Key 발급 실패 | Access Token이 유효한지 확인 |
| 8000 포트 충돌 | `lsof -i :8000` (Mac/Linux) 또는 netstat -ano |
