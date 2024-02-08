import gradio as gr

def main():
    gr.Interface(
            fn=lambda x: x,
        inputs=[
            gr.inputs.Textbox(lines=2, placeholder="Enter your question here:"),
        ],
        outputs=[gr.outputs.Textbox()],
    ).launch(server_name='0.0.0.0')

if __name__ == '__main__':
    main()
