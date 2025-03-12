import requests
from configs.config import BASE_URL

def get_api_key(access_token):
    try:
        headers = {"Access-Token": access_token}
        response = requests.post(f"{BASE_URL}/generate-api-key", headers=headers)
        if response.status_code == 200:
            return response.json()["api_key"], "키 발급 성공"
        return "", f"API Key 발급 실패: {response.json().get('detail', 'Unknown Error')}"
    except Exception as e:
        return f"서버 오류: {str(e)}"