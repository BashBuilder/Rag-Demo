import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key)

prompt = PromptTemplate.from_template(
    "Give short details of the following text: {text}"
)


# prompt2 = PromptTemplate.from_template(
#     "Give me the main points of the following summary: {summary}"
# )

chain = prompt | llm

result = chain.invoke({"text": "biology"})

prompt2 = PromptTemplate.from_template(
    "Give me the main points of the following summary: {summary}"
)
print(result.content)
print("-" * 50)

chain2 = prompt2 | llm

result2 = chain2.invoke({"summary": result})

print(result2.content)
