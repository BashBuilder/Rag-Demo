import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key)

science_prompt = PromptTemplate.from_template(
    "Your are a scientific expert. Answer the followint questions : {input}"
)
history_prompt = PromptTemplate.from_template(
    "Your are a historical expert. Answer the followint questions : {input}"
)
math_prompt = PromptTemplate.from_template(
    "Your are a mathematical expert. Answer the followint questions : {input}"
)

science_chain = science_prompt | llm | StrOutputParser()
history_chain = history_prompt | llm | StrOutputParser()
math_chain = math_prompt | llm | StrOutputParser()

# Create router prompt
router_prompt = PromptTemplate.from_template(
    """Given a question, determine which category it belongs to: Science, History, or Math.
Only respond with the category name.

Question: {input}
Category:
"""
)

router_chain = router_prompt | llm | StrOutputParser()


def route_chain(input_text):
    category = router_chain.invoke({"input": input_text}).strip().lower()
    print(category)
    print("-" * 50)
    if "science" in category:
        return science_chain
    elif "history" in category:
        return history_chain
    else:
        return math_chain


questions = [
    "What causes photosynthesis?",
    "Who was the first president of the United States?",
    "What is the square root of 100?",
]

for question in questions:
    print(f"\nQuestion: {question}")
    chain = route_chain(question)
    answer = chain.invoke({"input": question})
    print(f"Answer: {answer}")
