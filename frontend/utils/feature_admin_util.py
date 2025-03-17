import requests
from frontend.configs.base_url_config import BASE_URL

def add_feature(access_token, name, description, username):
    try:
        headers = {"Access-Token": access_token, "Content-Type": "application/json"}
        response = requests.post(
            f"{BASE_URL}/admin/feature/add",
            json={"name": name, "description": description, "username": username},
            headers=headers
        )

        # 응답 상태 코드 확인
        if response.status_code == 200:
            return "기능 추가 성공"

        # FastAPI의 에러 메시지를 그대로 반영
        elif response.status_code in [400, 401, 403, 500]:
            return f"오류 발생: {response.json().get('detail', '알 수 없는 오류')}"

        else:
            return f"예상치 못한 오류: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"서버 요청 오류: {str(e)}"
