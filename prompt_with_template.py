import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI

openai_key = "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"
os.environ["OPENAI_API_KEY"] = openai_key

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo"
)

prompt = PromptTemplate(
    input_variables=["Posisi", "Perusahaan", "keterampilan"],
    template="Yang terhormat HRD Manajer {perusahaan},\n\nDengan surat ini, saya [NAMA KAMU], ingin melamar untuk posisi {posisi} di {perusahaan}. Saya memiliki pengalaman di bidang {keterampilan}. Terima kasih telah mempertimbangkan lamaran saya.\n\nHormat saya,\n[NAMA KAMU]"
)

def generate_cover_letter(posisi: str, perusahaan: str, keterampilan: str) -> str:
    formatted_prompt = prompt.format(posisi=posisi, perusahaan=perusahaan, keterampilan=keterampilan)
    response = llm.invoke(formatted_prompt).content
    return response

inputs = [
    gr.Textbox(label='posisi'),
    gr.Textbox(label='perusahaan'),
    gr.Textbox(label='keterampilan')
]

output = gr.Textbox(label="template surat")

gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(server_name="0.0.0.0", server_port=7860, share= True)
