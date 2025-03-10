import gradio as gr
import requests

# Gradio 인증 함수
def authenticate(username, password):
    try:
        response = requests.post(f"http://127.0.0.1:8000/login?username={username}&password={password}")
        if response.status_code == 200:
            return f"인증 성공, API Key: {response.json()['api_key']}"
        else:
            print(response.json())
            return f"인증 실패: {response.json()['detail']}"
    except Exception as e:
        return f"서버 오류: {str(e)}"

# Gradio UI
iface = gr.Interface(
    fn=authenticate,
    inputs=["text", "text"],
    outputs="text",
    title="인증 시스템",
    description="ID와 비밀번호를 입력하면 API Key를 발급합니다."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860, share=False)
