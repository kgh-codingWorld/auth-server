from pydantic import BaseModel, Field

# 로그인 요청 데이터 모델
class LoginRequest(BaseModel):
    username: str = Field(..., example="user1")
    password: str = Field(..., example="password1")