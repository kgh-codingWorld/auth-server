import gradio as gr
from frontend.gui.sign_up_ui import sign_up_ui
from frontend.gui.login_ui import login_ui
from frontend.gui.api_key_ui import api_key_ui
from frontend.gui.feature_ui import feature_ui
from frontend.gui.feature_admin_ui import feature_admin_ui
sign_up_demo = sign_up_ui()
login_demo, token_output = login_ui()
api_key_demo, api_key_output = api_key_ui(token_output)
feature_demo = feature_ui(token_output, api_key_output)
feature_admin_demo = feature_admin_ui(token_output)

with gr.Blocks() as demo:
    gr.Markdown("# 기능 접근 인증 시스템")

    with gr.Tab("회원가입"):
        sign_up_demo.render()

    with gr.Tab("로그인"):
        login_demo.render()

    with gr.Tab("API Key 발급"):
        api_key_demo.render()

    with gr.Tab("기능 접근"):
        feature_demo.render()

    with gr.Tab("관리자(기능 관리)"):
        feature_admin_demo.render()

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
