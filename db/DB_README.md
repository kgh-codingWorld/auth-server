# Database (PostgreSQL)

이 폴더는 **PostgreSQL 데이터베이스 설정 및 관련 스크립트**를 포함하고 있습니다.

---

## 개요
- **DBMS**: PostgreSQL
- **ORM**: SQLAlchemy
- **데이터베이스 실행 환경**: Docker 컨테이너

---

## 폴더 구조
```bash
db/
│── configs/
│   ├── database.py        # 데이터베이스 설정 및 테이블 생성
│── models.py              # 데이터베이스 모델 정의
│── docker-compose.yaml    # Docker 기반 DB 실행 설정
```

## 실행 방법

### 1. Docker 컨테이너 실행

```bash

docker-compose up -d

```

- PostgreSQL 컨테이너가 실행됩니다.

### 2️. 테이블 생성

```bash

python -m db.configs.database

```

- 데이터베이스 테이블을 초기화합니다.

### 3️. 데이터베이스 접속

```bash

docker exec -it auth-server_postgres_1 bash
psql -U postgres

```

- `\l` → 데이터베이스 목록 확인
- `\dt` → 테이블 목록 확인
- `SELECT * FROM users;` → users 테이블 조회

### 4️. 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성하고 다음 내용을 추가합니다.

```bash

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres

```

---

## 문제 해결
| **문제** | **해결 방법** |
| --- | --- |
| `docker-compose up -d` 실행 후 DB 연결 오류 | `docker ps`로 컨테이너 상태 확인 후 `docker logs postgres`로 오류 확인 |
| 데이터베이스가 초기화되지 않음 | `python -m db.configs.database` 실행 |
