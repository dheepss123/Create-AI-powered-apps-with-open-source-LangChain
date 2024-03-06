import gradio as gr
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os

os.environ["OPENAI_API_KEY"] = ""
llm = ChatOpenAI(temperature=0.9)
def handle_complaint(komplain: str) -> str:
    
    
   
    prompt = PromptTemplate(input_variables=["komplain"], template="Saya seorang perwakilan layanan pelanggan. Saya menerima keluhan berikut: {komplain}. Respon saya adalah:")
    
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(komplain)

iface = gr.Interface(fn=handle_complaint, inputs="text", outputs="text")
iface.launch(share=True)
