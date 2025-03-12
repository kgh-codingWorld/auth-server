from fastapi    import FastAPI
from routes     import auth, api_key, feature

app = FastAPI(openapi_url="/openapi.json") # Swagger 무한로딩 방지

# 라우터 등록(각 기능별 API 연결)
app.include_router(auth.router)     # 로그인 관련 API
app.include_router(api_key.router)  # API Key 생성 API
app.include_router(feature.router)  # 특정 기능 접근 API

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)