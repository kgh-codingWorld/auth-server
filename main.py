from fastapi import FastAPI
from server.routes import feature_admin, sign_up, auth, api_key, feature

app = FastAPI(openapi_url="/openapi.json") # Swagger 무한로딩 방지

# 라우터 등록(각 기능별 API 연결)
app.include_router(sign_up.router)
app.include_router(auth.router)
app.include_router(api_key.router)
app.include_router(feature.router)
app.include_router(feature_admin.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)