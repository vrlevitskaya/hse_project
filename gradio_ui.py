import gradio as gr
from utils import generate_group1, generate_group2

with gr.Blocks() as demo:
    gr.Markdown("Выберите одну из опций")
    with gr.Row():
        inputs = [gr.Textbox(label="Введите код для того, чтобы добавить в него пропуски"),
                  gr.Textbox(label="Введите количество пропусков")]

        outputs = gr.Textbox(label="Сгенерированные задания")

    btn_1 = gr.Button("Сгенерировать задания с пропусками")
    btn_1.click(fn=generate_group1, inputs=inputs, outputs=outputs)

    with gr.Row():
        inputs = [gr.Textbox(label="Введите код для того, чтобы добавить в него шум")]

        outputs = gr.Textbox(label="Сгенерированные задания")

    btn_1 = gr.Button("Сгенерировать задания с шумом")
    btn_1.click(fn=generate_group2, inputs=inputs, outputs=outputs)

demo.launch()
