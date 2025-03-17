from pydantic import BaseModel

# 로그인 요청 데이터 모델
class LoginRequest(BaseModel):
    username: str
    password: str

class SignUpRequest(BaseModel):
    username: str
    password: str
    is_admin: bool = False

class FeatureRequest(BaseModel):
    name: str
    description: str | None = None

class UserFeatureRequest(BaseModel):
    name: str
    username: str
    feature_id: int