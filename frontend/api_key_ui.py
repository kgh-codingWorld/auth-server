import gradio   as gr
import requests
from config     import BASE_URL

def get_api_key(access_token):
    try:
        headers = {"Access-Token": access_token}
        response = requests.post(f"{BASE_URL}/generate-api-key", headers=headers)
        if response.status_code == 200:
            return response.json()["api_key"], "키 발급 성공"
        return "", f"API Key 발급 실패: {response.json().get('detail', 'Unknown Error')}"
    except Exception as e:
        return f"서버 오류: {str(e)}"
    
def api_key_ui(token_output):
    with gr.Blocks() as api_key_demo:
        gr.Markdown("API Key 발급")
        api_key_btn = gr.Button("API Key 요청")
        api_key_output = gr.Textbox(label="발급된 API Key", visible=False)
        api_key_status = gr.Textbox(label="API Key 상태", interactive=False)
        api_key_btn.click(fn=get_api_key, inputs=token_output, outputs=[api_key_output, api_key_status])

    return api_key_demo, api_key_output