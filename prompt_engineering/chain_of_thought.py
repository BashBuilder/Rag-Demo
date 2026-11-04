import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=api_key,
    temperature=0.7,
)

chain_of_thought_template = """
You are a highly professional customer support specialist at a premium tech company.
Your goal is to address the customer's concerns while maintaining a calm and helpful demeanor.

Let's approach this step by step:

1. First, analyze the customer's sentiment and identify the core issues in their message
2. Then, formulate an empathetic acknowledgment of their feelings
3. Next, address each identified issue with specific solutions
4. Finally, end with a positive and forward-looking statement

Here are some examples of good responses:
Angry Customer: "Your product is terrible! I've been trying to make it work for hours and nothing helps!"
Thought Process:
1. Sentiment: Customer is frustrated due to wasted time and product difficulties
2. Core issues: Product not working, time wasted, lack of proper guidance
3. Required: Immediate assistance, clear steps, acknowledgment of time value
Response: "I sincerely apologize for the frustration you're experiencing. I understand how valuable your time is, and it's unacceptable that you're not able to use the product. Let me help you troubleshoot the issue.

Now, please analyze and respond to this customer message: {customer_message}
Please show your thought process before providing the response."""

chain_of_thought_template = PromptTemplate.from_template(chain_of_thought_template)
chain_of_thought_chain = chain_of_thought_template | llm

customer_message = """
I've been waiting for 2 hours for your delivery and it still .hasn't arrived!
.This is absolutely unacceptable! I paid extra for express delivery and this
is.what .I.get? .I.want.my money back immediately!
"""
response = chain_of_thought_chain.invoke({"customer_message": customer_message})
print(response.content)
