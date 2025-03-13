from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

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
    except:
        db.close()


if __name__ == "__main__":
    print("테이블 생성하는 중...")
    Base.metadata.create_all(bind=engine)