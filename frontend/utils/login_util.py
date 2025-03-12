import requests # HTTP 요청을 보내는 라이브러리(FastAPI와 통신)
from configs.config import BASE_URL # FastAPI 서버의 기본 URL 설정

# 로그인 요청 함수 (Gradio → FastAPI)
def login(username, password):
    try:
        # FastAPI의 '/login' 엔드포인트로 POST 요청을 보냄
        response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password}, # JSON 형태로 데이터 전송
                                 headers={"Content-Type": "application/json"})                           # HTTP 요청 헤더 (JSON 형식 지정)
        if response.status_code == 200:
            data = response.json()                                          # JSON 응답 데이터 가져옴
            access_token = data.get("access_token", "Access Token 없음")    # Access Token 추출
            return access_token, "로그인 성공"                               # Access Token과 성공 메시지 반환
        else:
            print(response.json())
            return "", f"인증 실패: {response.json().get('detail', 'Unknown Error')}"
    except Exception as e:
        return f"서버 오류: {str(e)}"