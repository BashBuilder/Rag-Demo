import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key, temperature=0.7)

# Define prompt template
role_context_template = """
You are a highly professional customer support specialist at a premium tech company.
Your goal is to address the customer's concerns while maintaining a calm and helpful demeanor.

Customer Message: {customer_message}

Please provide a response that:
1. Acknowledges the customer's feelings
2. Addresses their concerns professionally
3. Offers concrete solutions
4. Ends with a positive note
"""

basic_template = PromptTemplate.from_template(role_context_template)
role_chain = basic_template | llm

customer_message = """
I've been waiting for 2 hours for your delivery and it still .hasn't arrived!
.This is absolutely unacceptable! I paid extra for express delivery and this
is.what .I.get? .I.want.my money back immediately!
"""
response = role_chain.invoke({"customer_message": customer_message})
print(response.content)
