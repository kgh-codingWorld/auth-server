import gradio as gr
import requests
from config import BASE_URL

def access_feature(access_token, api_key, feature_name):
    headers = {"Access-Token": access_token, "API-Key": api_key}
    response = requests.get(f"{BASE_URL}/access-feature/{feature_name}", headers=headers)
    return response.json()["message"] if response.status_code == 200 else "기능 접근 거부됨"

def feature_ui(token_output, api_key_output):
    with gr.Blocks() as feature_demo:
        gr.Markdown("## 기능 접근 테스트")

        feature_name_input = gr.Dropdown(choices=["feature1", "feature2", "feature3"], label="기능 선택")

        access_btn = gr.Button("기능 접근 테스트")
        access_output = gr.Textbox(label="기능 접근 결과")

        access_btn.click(access_feature, inputs=[token_output, api_key_output, feature_name_input], outputs=access_output)

    return feature_demo
