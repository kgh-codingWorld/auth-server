import requests
from ..configs.config import BASE_URL

def access_feature(access_token, api_key, feature_name):
    headers = {"Access-Token": access_token, "API-Key": api_key}
    response = requests.get(f"{BASE_URL}/access-feature/{feature_name}", headers=headers)
    return response.json()["message"] if response.status_code == 200 else "기능 접근 거부됨"