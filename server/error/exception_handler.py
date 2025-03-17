from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
import logging

# 로거 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def set_exception_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def custom_http_exception_handler(request: Request, exc: HTTPException):
        if exc.status_code in {400, 401, 403, 404}:
            # HTTPException은 FastAPI에서 정상적으로 처리 가능한 예외이므로, 치명적인 오류는 아니지만 경고해야 하는 상황(404, 400)
            logger.warning(f"HTTPException 발생: {exc.detail} (Status: {exc.status_code})")
        else:
            # logger.exception()은  실제 예외 객체(Exception)가 있어야 하지만, HTTPException은 FastAPI가 예상하는 예외이므로 logger.error()가 적절함
            logger.error(f"HTTP 오류 발생: {exc.detail} (Status: {exc.status_code})")
        
        # rasise HTTPException(...)을 호출하면 FastAPI가 자동으로 예외 처리 후 JSONResponse를 반환 그러나 커스텀을 만든 경우 직접 JSONResponse를 반환해야 함
        # 그렇지 않으면 FastAPI의 기본 예외 처리가 적용됨
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        # Exception은 예상하지 못한 오류일 가능성이 크고 logger.exception()은 자동으로 스택 트레이스를 포함하므로 오류 원인을 쉽게 찾을 수 있음(logger.error()는 메시지만 출력)
        logger.exception(f"서버 내부 오류 발행: {exc}")
        return JSONResponse(status_code=500, content={"detail": "An unexpected error occurred"})
    
    # 예외 핸들러 등록 함수
    app.add_exception_handler(HTTPException, custom_http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
