import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(
    api_key=api_key,
    temperature=0.7,
    model="deepseek-chat",
)
basic_prompt = PromptTemplate.from_template(
    "You are quizergo support expert, Reply to this customer message in not more than a sentence: {customer_message}"
)

basic_chain = basic_prompt | llm

customer_message = """
I've been waiting for 2 hours for your delivery and it still .hasn't arrived!
.This is absolutely unacceptable! I paid extra for express delivery and this
is.what .I.get? .I.want.my money back immediately!
"""

response = basic_chain.invoke({"customer_message": customer_message})
print(response.content)
