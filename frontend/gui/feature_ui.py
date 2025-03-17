import gradio as gr
from frontend.utils.feature_subscribe_util import feature_subscribe
from frontend.utils.feature_access_util import feature_access
from server.utils.feature_utils.feature_query import get_feature_list, update_feature_list
from db.configs.database import get_db

def feature_ui(token_output, api_key_output):
    with gr.Blocks() as feature_demo:
        gr.Markdown("## 기능 접근 테스트")

        db = next(get_db())
        feature_list = get_feature_list(db)

        feature_name_input = gr.Dropdown(choices=feature_list, label="기능 선택")

        subscription_btn = gr.Button("해당 기능 구독하기")
        access_btn = gr.Button("기능 접근 테스트")
        refresh_btn = gr.Button("🔄 기능 목록 새로고침")
        subscribe_output = gr.Textbox(label="구독 결과")
        access_output = gr.Textbox(label="기능 접근 결과")

        subscription_btn.click(feature_subscribe, inputs=[token_output, api_key_output, feature_name_input], outputs=subscribe_output)
        access_btn.click(feature_access, inputs=[token_output, api_key_output, feature_name_input], outputs=access_output)
        refresh_btn.click(update_feature_list, outputs=feature_name_input)

    return feature_demo
