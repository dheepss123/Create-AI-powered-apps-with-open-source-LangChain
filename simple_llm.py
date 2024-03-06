import os
from langchain_openai import chatOpenAI

os.environ["OPEN_API_KEY"] = "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"
gpt3 = chatOpenAI(model_name="gpt-3.5-turbo")

text = "halo aku dheo apa kabar"
print(gpt3.invoke(text).content)
