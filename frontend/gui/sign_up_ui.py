import gradio as gr
from frontend.utils.sign_up_util import sign_up

def sign_up_ui():
    with gr.Blocks() as sign_up_demo:
        gr.Markdown("## 회원가입")
        username_input = gr.Textbox(label="아이디")
        password_input = gr.Textbox(label="비밀번호", type="password")
        sign_up_btn = gr.Button("회원가입")
        sign_up_status = gr.Textbox(label="회원가입 상태", interactive=False)

        sign_up_btn.click(sign_up, inputs=[username_input, password_input], outputs=sign_up_status)

        return sign_up_demo