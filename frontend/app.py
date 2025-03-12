import gradio   as gr
from gui.login_ui   import login_ui
from gui.api_key_ui import api_key_ui
from gui.feature_ui import feature_ui

login_demo, token_output        = login_ui()                                # token_output 반환
api_key_demo, api_key_output    = api_key_ui(token_output)                  # 반환된 token_output 이용, api_key 반환
feature_demo                    = feature_ui(token_output, api_key_output)  # 반환된 token_output, api_key 이용

with gr.Blocks() as demo:
    gr.Markdown("# 기능 접근 인증 시스템")

    with gr.Tab("로그인"):
        login_demo.render()

    with gr.Tab("API Key 발급"):
        api_key_demo.render()

    with gr.Tab("접근 기능"):
        feature_demo.render()

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
