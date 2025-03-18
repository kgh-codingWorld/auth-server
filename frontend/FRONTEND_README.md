## 📂 `frontend/README.md`

# Gradio UI

이 폴더는 **Gradio 기반 프론트엔드 UI**를 포함하고 있습니다.

---

## 📌 개요
- **프론트엔드 프레임워크**: Gradio
- **역할**: API Key 관리, 기능 접근, 사용자 인증 UI 제공
- **백엔드 통신**: FastAPI

---

## 📂 폴더 구조
```bash
frontend/
│── gui/
│   ├── api_key_ui.py         # API Key 발급 UI
│   ├── feature_admin_ui.py   # 관리자 기능 추가 UI
│   ├── feature_ui.py         # 기능 구독 및 접근 UI
│   ├── login_ui.py           # 로그인 UI
│   ├── sign_up_ui.py         # 회원가입 UI
│── utils/
│   ├── api_key_util.py       # API Key 요청 처리
│   ├── feature_access_util.py # 기능 접근 요청 처리
│   ├── feature_admin_util.py  # 관리자 기능 추가 처리
│   ├── feature_subscribe_util.py # 기능 구독 요청 처리
│   ├── login_util.py         # 로그인 요청 처리
│   ├── sign_up_util.py       # 회원가입 요청 처리
│── .env                      # 환경 변수 설정
│── app.py                    # Gradio 실행 파일

```

## 실행 방법

### 1️. 필요 패키지 설치

```bash

pip install -r requirements.txt

```

### 2️. Gradio UI 실행

```bash

python -m frontend.app

```

### 3️. UI 접속

- [http://127.0.0.1:7860](http://127.0.0.1:7860/)

---

## 문제 해결
| **문제** | **해결 방법** |
| --- | --- |
| `docker-compose up -d` 실행 후 DB 연결 오류 | `docker ps`로 컨테이너 상태 확인 후 `docker logs postgres`로 오류 확인 |
| 데이터베이스가 초기화되지 않음 | `python -m db.configs.database` 실행 |
