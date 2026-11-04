import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key)

prompt = PromptTemplate.from_template(
    "What is the weather in {country} today, one line answer"
)

chain = prompt | llm

result = chain.invoke({"country": "nigeria"})


print(result)
