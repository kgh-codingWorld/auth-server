import requests
from frontend.configs.base_url_config import BASE_URL

def feature_subscribe(access_token, api_key, feature_name):
    response = requests.post(f"{BASE_URL}/feature/subscribe/{feature_name}", headers={"Access-Token": access_token, "API-Key": api_key})
    return response.json()["message"] if response.status_code == 200 else "구독 중 오류 발생"
