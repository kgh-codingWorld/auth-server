import gradio   as gr           # Gradio UI 라이브러리
import requests                 # HTTP 요청을 보내는 라이브러리(FastAPI와 통신)
from config     import BASE_URL # FastAPI 서버의 기본 URL 설정

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

# Gradio UI 정의 (로그인 화면)
def login_ui():
    with gr.Blocks() as login_demo:                                             # Gradio 블록 기반 UI
        gr.Markdown("## 로그인")                                                # 제목 표시                                
        with gr.Row():                                                          # 가로 정렬
            username_input = gr.Textbox(label="아이디")                         # 입력 필드
            password_input = gr.Textbox(label="비밀번호", type="password")      # 입력 필드
            login_btn = gr.Button("로그인")                                     # 로그인 버튼
            
        token_output = gr.Textbox(label="발급된 토큰", visible=False)           # Access Token 출력 필드
        login_status = gr.Textbox(label="로그인 상태", interactive=False)       # 로그인 상태 표시

        # 로그인 버튼 클릭하면 'login' 함수를 실행하여 FastAPI에 요청
        # 결과를 'token_output' (Access Token)과 'login_status' (로그인 메시지)에 표시
        login_btn.click(login, inputs=[username_input, password_input], outputs=[token_output, login_status]) # outputs의 매개변수가 2개이므로 login()에서 무조건 return 값은 2개여야 함

    return login_demo, token_output                                            # 로그인 UI와 Access Token 출력을 반환


