# 인증 서버(AuthenticationServer)

FastAPI 기반 API 인증 및 접근 제어 시스템입니다. 사용자는 Access Token으로 API를 인증하고, API Key로 특정 기능 접근을 제어할 수 있습니다.

이 프로젝트는 FastAPI**,** PostgreSQL**,** SQLAlchemy**,** Gradio를 기반으로 하며, Docker 환경에서 실행 가능하도록 설계되었습니다.

> ⚠️ 이 프로젝트는 **Docker Desktop** 환경을 전제로 작성되었습니다.
설치 및 실행 전에 Docker Desktop이 반드시 설치되어 있고, 실행 중인지 확인하세요.
> 

## 프로젝트 개요

---

### 실행 환경

- 데이터베이스: PostgreSQL(Docker 컨테이너 실행)
- 백엔드: FastAPI
- 프론트엔드: Gradio
- 필수 요구사항: Docker Desktop이 설치 및 실행 중이어야 함

### 주요 기능

- 사용자 인증: 회원가입 및 로그인, Access Token 기반 인증
- API Key 발급 및 관리(특정 기능 접근을 위해 필요)
- 기능 접근 제어: API Key 및 Access Token을 통한 기능 접근 관리
- 관리자 기능: 새로운 기능 등록(관리자 계정 필요)
- 에러 핸들링: FastAPI 예외 처리 적용

## 기술 스택

---

- 언어: Python 3.11.9
- 백엔드: FastAPI
- 프론트엔드: Gradio
- 데이터베이스: PostgreSQL
- ORM: SQLAlchemy
- 인증 방식: Access Token, API Key
- 배포 환경: Docker, Uvicorn

## 설치 및 실행 방법

---

### 사전 요구사항

- Python 3.11.9
- Docker 및 Docker Compose
- Docker Desktop 실행 중 필수
- pip 패키지 관리자

### 로컬 실행 방법

- 프로젝트 클론

```bash
git clone http://github.com/your-repo/auth-server.git
cd auth-server
```

- 가상 환경 생성 및 패키지 설치

```bash
python -m venv venv
sourcevenv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

- Docker Compose를 이용한 컨테이너 생성 및 실행

```bash
docker-compose up -d
```

- 테이블 생성

```bash
python -m db.configs.database
```

- 서버 실행(포트 충돌 시 해결 방법은 문제 해결 섹션 참고)

```bash
uvicorn server.main:app
```

- Gradio UI 실행

```bash
python -m frontend.app
```

※ 각각 다른 터미널에서 uvicorn과 Gradio UI를 실행하도록 한다.

### Docker 컨테이너 관리 및 상태 확인

1. **실행 중인 컨테이너 확인**
    
    ```bash
    docker ps
    ```
    
    - auth-server_postgres_1 컨테이너가 실행 중인지 확인하세요.
2. **Docker Desktop에서 컨테이너 상태 확인**
    - `Containers` 탭에서 `auth-server` 컨테이너가 실행 중인지 확인
    - 실행되지 않았다면, 터미널에서 `docker start auth-server` 실행
3. **Docker Desktop에서 컨테이너 로그 확인**
    - `Containers` → `auth-server` 클릭 후 `Logs` 탭에서 서버 상태 확인
4. **컨테이너 종료 및 삭제**
    
    ```bash
    docker-compose down
    ```
    

### Docker를 이용한 데이터베이스 접근

Docker Desktop에서 PostgreSQL 데이터베이스에 직접 접근하는 방법입니다.

1. **PostgreSQL 컨테이너에 접속 (`bash` 실행)**

```
docker exec -it auth-server_postgres_1 bash
```

2. **PostgreSQL 쉘(`psql`) 실행**

```
psql -U postgres
```

- `postgres` 데이터베이스에 로그인됨
3. **데이터베이스 목록 확인**

```
\l
```

4. **현재 사용 중인 데이터베이스 확인**

```
SELECT current_database();
```

5. **테이블 목록 확인**

```
\dt
```

6. **테이블 데이터 조회 (예: users 테이블)**

```
SELECT * FROM users;
```

7. **PostgreSQL에서 나가기**

```
\q
```

8. **컨테이너에서 나가기**

```
exit
```

## 환경 변수 설정

---

`.env` 파일을 프로젝트 루트에 생성 후 다음 내용을 추가합니다:

```bash
PORT=8000
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres
SECRET_KEY=mysecretkey
TOKEN_EXPIRATION=3600
```

환경 변수를 자동으로 로드하려면 dotenv 패키지를 설치하세요:

```bash
pip install python-dotenv
```

## 데이터베이스 설정

---

데이터베이스 초기화 및 테이블 생성을 수행합니다:

```bash
python -m db.configs.database
```

## 기능별 사용방법

---

### 프로젝트 구조

```bash
project_root/
│── db/
│   ├── configs/
│   │   ├── database.py           # 데이터베이스 설정
│   ├── models.py                 # 데이터베이스 모델 정의
│   ├── docker-compose.yaml       # Docker 설정
│
│── frontend/
│   ├── gui/
│   │   ├── api_key_ui.py         # API Key 발급 UI
│   │   ├── feature_admin_ui.py   # 관리자 기능 추가 UI
│   │   ├── feature_ui.py         # 기능 구독 및 접근 UI
│   │   ├── login_ui.py           # 로그인 UI
│   │   ├── sign_up_ui.py         # 회원가입 UI
│   ├── utils/
│   │   ├── api_key_util.py       # API Key 요청 처리
│   │   ├── feature_access_util.py # 기능 접근 요청 처리
│   │   ├── feature_admin_util.py  # 관리자 기능 추가 처리
│   │   ├── feature_subscribe_util.py # 기능 구독 요청 처리
│   │   ├── login_util.py         # 로그인 요청 처리
│   │   ├── sign_up_util.py       # 회원가입 요청 처리
│   ├── .env                      # 환경 변수 설정
│   │── app.py                        # FastAPI 실행 엔트리포인트
│
│── server/
│   ├── error/
│   │   ├── exception_handler.py  # 예외 처리
│   ├── models/
│   │   ├── request_model.py      # Pydantic 데이터 모델 정의
│   │   ├── response_model.py     # API 응답 모델 정의
│   ├── routes/
│   │   ├── api_key.py            # API Key 관련 라우트
│   │   ├── auth.py               # 로그인/회원가입 라우트
│   │   ├── feature_access.py     # 기능 접근 라우트
│   │   ├── feature_admin.py      # 관리자 기능 추가 라우트
│   │   ├── feature_subscribe.py  # 기능 구독 라우트
│   │   ├── sign_up.py            # 회원가입 라우트
│   ├── utils/
│   │   ├── admin_utils/
│   │   │   ├── feature_admin_util.py # 관리자 기능 관리 유틸리티
│   │   ├── feature_utils/
│   │   │   ├── feature_access_util.py # 기능 접근 유틸리티
│   │   │   ├── feature_query.py   # 기능 조회 유틸리티
│   │   │   ├── feature_subscribe_util.py # 기능 구독 유틸리티
│   │   ├── access_token_util.py   # Access Token 관련 유틸리티
│   │   ├── api_key_util.py        # API Key 관련 유틸리티
│   │   ├── auth_util.py           # 인증 관련 유틸리티
│   │   ├── password_hash_util.py  # 비밀번호 해싱 유틸리티
│   │   ├── sign_up_util.py        # 회원가입 유틸리티
│   │── main.py                       # 메인 실행 파일
│
│── .gitignore                    # Git 무시 파일

```

### 회원가입 및 로그인 인증 시스템

- **주요 기능 설명**
    - 회원가입 API (`POST /signup/`)
        - 새로운 사용자를 등록하는 API입니다.
        - “is_admin”이 False면 일반 회원, True면 관리자 권한
        - 요청 예시
        
        ```
        {
            "username": "testuser",
            "password": "password123",
            "is_admin": false
        }
        ```
        
        - 응답 예시
        
        ```
        {
            "message": "회원가입 성공"
        }
        ```
        
    - 로그인 API (`POST /auth/login`)
        - 로그인을 수행하고, Access Token을 발급합니다.
        - 요청 예시
        
        ```
        {
            "username": "testuser",
            "password": "password123"
        }
        ```
        
        - 응답 예시
        
        ```
        {
            "message": "인증 성공",
            "access_token": "abcd1234efgh5678",
            "is_admin": false
        }
        ```
        
    - Access Token 검증 (`validate_access_token`)
        - 사용자의 인증 상태를 확인하는 기능입니다. 인증이 만료되었거나 잘못된 경우 로그인 상태를 갱신해야 합니다.
        - 요청 예시
        
        ```
        curl -X POST "http://127.0.0.1:8000/auth/token/validate" \
             -H "Access-Token: abcd1234efgh5678"
        ```
        
        - 응답 예시 (유효한 경우)
        
        ```
        {
            "message": "Access Token이 유효합니다.",
        }
        ```
        
        - 응답 예시 (만료된 경우)
        
        ```bash
        {
            "detail": "로그아웃 상태입니다. 로그인 또는 회원가입을 진행해 주세요."
        }
        ```
        

### API 사용법

- **주요 기능 설명**
    - API Key 발급 (`POST /api-key/generate`)
        - 사용자가 Access Token을 이용하여 API Key를 요청하면, 새로운 API Key를 발급받을 수 있습니다.
        - 요청 예시
        
        ```
        curl -X POST "http://127.0.0.1:8000/api-key/generate" -H "Access-Token: abcd1234efgh5678"
        ```
        
    - 응답 예시
        
        ```
        {
            "message": "API Key 발급 성공",
            "api_key": "1234567890abcdef"
        }
        ```
        

### 기능 접근 및 구독

- 주요 기능 설명
    - 기능 구독 (`POST /feature/subscribe/{feature_name}`)
        - 사용자가 특정 기능을 구독할 수 있습니다.
        - 요청 예시
        
        ```
        curl -X POST "http://127.0.0.1:8000/feature/subscribe/예제기능" \
             -H "Access-Token: abcd1234efgh5678" \
             -H "API-Key: 1234567890abcdef"
        ```
        
        - 응답 예시
        
        ```
        {
            "message": "기능 예제기능 구독 성공"
        }
        ```
        
    - 기능 접근 (`POST /feature/access/{feature_name}`)
        - 구독한 기능에 대한 접근 권한을 확인합니다.
        - 요청 예시
        
        ```
        curl -X POST "http://127.0.0.1:8000/feature/access/예제기능" \
             -H "Access-Token: abcd1234efgh5678" \
             -H "API-Key: 1234567890abcdef"
        ```
        
        - 응답 예시
        
        ```bash
        {
            "message": "기능 접근 허용됨"
        }
        ```
        

### 관리자 기능 관리

- 주요 기능 설명
    - 기능 추가(`POST /admin/feature/add`)
        - 관리자가 새로운 기능을 추가할 수 있습니다.
        - 요청 예시:
        
        ```bash
        curl -X POST "http://127.0.0.1:8000/admin/feature/add" \
             -H "Access-Token: abcd1234efgh5678" \
             -H "Content-Type: application/json" \
             -d '{"name": "새로운 기능", "description": "기능 설명", "username": "admin"}'
        ```
        
        - 응답 예시:
        
        ```bash
        {
            "message": "기능 추가 성공"
        }
        ```
        

## 배포 방법

---

### Docker를 이용한 배포

Docker 이미지 빌드

```bash
docker build -t auth-server .
```

### Docker 컨테이너 실행

```bash
docker run -d -p 8000:8000 --name auth-server auth-server
```

### 클라우드 배포

- AWS EC2 또는 GCP Compute Engine에 Docker 컨테이너 배포
- Heroku를 활용한 FastAPI 배포 가능

## API 및 UI 접속 URL

---

FastAPI의 자동 생성 문서 및 UI를 확인하려면 서버 실행 후 아래 URL로 접속하세요.

- Swagger UI http://127.0.0.1:8000/docs
- ReDoc http://127.0.0.1:8000/redoc
- Gradio UI http://127.0.0.1:7860

## 문제 해결(Troubleshooting)
| **문제** | **해결 방법** |
| --- | --- |
| `docker-compose up -d` 실행 후 DB 연결 오류 | `docker ps`로 컨테이너 상태 확인 후 `docker logs postgres`로 오류 확인 |
| FastAPI 서버 실행 오류 | `.env` 파일이 존재하는지 확인하고 환경 변수 설정 |
| Gradio UI가 실행되지 않음 | `pip install -r requirements.txt` 실행 후 다시 시도 |
| 로그인 시 `401 Unauthorized` 오류 발생 | 데이터베이스에 사용자가 존재하는지 확인 |
| 8000 포트 충돌 | lsof -i :8000 (Mac/Linux) 또는 ‘netstat -ano’ findstr:8000(Windows)로 사용 중인 프로세스 종료 후 다시 실행 |
