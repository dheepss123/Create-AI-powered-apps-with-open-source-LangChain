import gradio as gr
def greet(name):
    return "Halo " + name + ", Selamat bergabung di IBM Academy!"
demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)