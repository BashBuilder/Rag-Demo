import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")
llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key, temperature=0.7)

few_shot_template = """
You are a highly professional customer support specialist at a premium tech company.
Your goal is to address the customer's concerns while maintaining a calm and helpful demeanor.

Here are some examples of good responses to angry customers:

Angry Customer: "Your product is terrible! I've been trying to make it work for hours and nothing helps!"
Response: "I sincerely apologize for the frustration you're experiencing. I understand how valuable your time is, and it's unaccept

Angry Customer: "I want a refund right now! This is the worst service ever!"
Response: "I completely understand your disappointment, and I want to make this right for you. I'll help you with the refund proces

Now, please respond to this customer message: (customer_message)
"""
short_template = PromptTemplate.from_template()
