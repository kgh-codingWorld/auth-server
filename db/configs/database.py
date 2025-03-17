from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
import logging

logger = logging.getLogger(__name__)

# 연결할 DB URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

# 내 DB와 연결 가능한 engine 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True,connect_args={"options":"-c client_encoding=UTF8"})

# 접속이 끝나도 연결 상태를 유지하기 위해 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    try:
        yield db
    except Exception as e:
        logger.exception(f"데이터베이스 연결 중 오류 발생: {e}")
        raise # 예외 정상 처리하도록 다시 던짐
    finally:
        db.close()

if __name__ == "__main__":
    print("테이블 생성하는 중...")
    Base.metadata.create_all(bind=engine)