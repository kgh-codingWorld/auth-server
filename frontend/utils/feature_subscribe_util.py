import requests
from frontend.configs.base_url_config import BASE_URL

def feature_subscribe(access_token, api_key, feature_name):
    try:
        response = requests.post(f"{BASE_URL}/feature/subscribe/{feature_name}", headers={"Access-Token": access_token, "API-Key": api_key})
        
        if response.status_code == 200:
            response.json()("message")
        else:
            return response.json().get("detail")
    except Exception as e:
        return f"서버 오류: {str(e)}"