import gradio as gr
from ..utils.feature_util import access_feature
from server.utils.feature_util import get_feature_list, update_feature_list
from sqlalchemy.orm import Session
from db.configs.database import get_db

def feature_ui(token_output, api_key_output):
    with gr.Blocks() as feature_demo:
        gr.Markdown("## 기능 접근 테스트")

        db = next(get_db())
        feature_list = get_feature_list(db)

        feature_name_input = gr.Dropdown(choices=feature_list, label="기능 선택")

        access_btn = gr.Button("기능 접근 테스트")
        refresh_btn = gr.Button("🔄 기능 목록 새로고침")
        access_output = gr.Textbox(label="기능 접근 결과")

        access_btn.click(access_feature, inputs=[token_output, api_key_output, feature_name_input], outputs=access_output)

        refresh_btn.click(update_feature_list, outputs=feature_name_input)

    return feature_demo
