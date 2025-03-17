import gradio as gr
from frontend.utils.feature_admin_util import add_feature

def feature_admin_ui(token_output):
    with gr.Blocks() as feature_admin_demo:
        gr.Markdown("## 기능 관리")
        username_input = gr.Textbox(label="관리자 ID")
        feature_name_input = gr.Textbox(label="기능 이름")
        feature_description_input = gr.Textbox(label="기능 설명")
        feature_add_btn = gr.Button("기능 추가")
        feature_add_status = gr.Textbox(label="기능 추가 상태", interactive=False)

        feature_add_btn.click(add_feature, inputs=[token_output, feature_name_input, feature_description_input, username_input], outputs=feature_add_status)

    return feature_admin_demo