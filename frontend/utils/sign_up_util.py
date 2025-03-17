import requests, logging
from frontend.configs.base_url_config import BASE_URL

logger = logging.getLogger(__name__)

def sign_up(username, password, is_admin=False):
    try:
        response = requests.post(f"{BASE_URL}/signup/", json={"username": username, "password": password, "is_admin": is_admin},
                                 headers={"Content-Type": "application/json"})
        
        if response.status_code == 200:
            return f"회원가입 성공(관리자: {is_admin})"
        else:
            return f"회원가입 실패: {response.json().get('detail', 'Unknown Error')}"
    except Exception as e:
        return f"서버 오류: {str(e)}"