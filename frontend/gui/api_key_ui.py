import gradio as gr
from frontend.utils.api_key_util import get_api_key
    
def api_key_ui(token_output):
    with gr.Blocks() as api_key_demo:
        gr.Markdown("API Key 발급")
        api_key_btn = gr.Button("API Key 요청")
        api_key_output = gr.Textbox(label="발급된 API Key", visible=False)
        api_key_status = gr.Textbox(label="API Key 상태", interactive=False)
        api_key_btn.click(fn=get_api_key, inputs=token_output, outputs=[api_key_output, api_key_status])

    return api_key_demo, api_key_output