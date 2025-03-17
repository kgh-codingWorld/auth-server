import requests
from frontend.configs.base_url_config import BASE_URL

def feature_access(access_token, api_key, feature_name):
    headers = {"Access-Token": access_token, "API-Key": api_key}
    response = requests.post(f"{BASE_URL}/feature/access/{feature_name}", headers=headers)
    return response.json()["message"] if response.status_code == 200 else "기능 접근 거부됨"