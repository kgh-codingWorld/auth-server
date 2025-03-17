from sqlalchemy import Boolean, Integer, String, ForeignKey, TIMESTAMP, Text
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    create_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)

class AccessToken(Base):
    __tablename__ = "access_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id =  Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    token = Column(Text, unique=True, nullable=False)  # token, api key의 길이 변동 가능성 때문에 일단 Text 사용 -> 추후 픽스 후에 검색 성능 증가를 위해 String(N)으로 바꿀 가능성.
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)
    expires_at = Column(TIMESTAMP, nullable=False)

class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    api_key = Column(Text, unique=True, nullable=False)
    create_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)
    expires_at = Column(TIMESTAMP, nullable=False)

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    create_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)

class UserFeature(Base):
    __tablename__ = "user_features"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    feature_id = Column(Integer, ForeignKey("features.id", ondelete="CASCADE"))
    api_key_id = Column(Integer, ForeignKey("api_keys.id", ondelete="CASCADE"))
    assigned_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc), nullable=False)
