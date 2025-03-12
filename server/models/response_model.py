from pydantic import BaseModel

# 로그인 응답 데이터 모델
class LoginResponse(BaseModel):
    message: str # 성공 또는 실패 메시지
    access_token: str | None = None