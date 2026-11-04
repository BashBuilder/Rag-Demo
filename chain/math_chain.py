import os

from dotenv import load_dotenv
from langchain_classic.chains import LLMMathChain
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key)

# 1. Plain LLM answer (may be wrong on big numbers)
result = llm.invoke("What is 17 raised to the power of 11")
print(result.content)
print("-" * 50)

# 2. LLM writes the formula
result = llm.invoke(
    "Give me the python formula that represents what is 17 raised to the power of 11. "
    "Only reply with the formula, nothing else"
)
print(result.content)
print("-" * 50)

# 3. LLM writes the formula, a real calculator computes it
llm_math_model = LLMMathChain.from_llm(llm)
result = llm_math_model.invoke("What is 17 raised to the power of 11")
print(result["answer"])
print("-" * 50)

# use lang graph for newwer models
