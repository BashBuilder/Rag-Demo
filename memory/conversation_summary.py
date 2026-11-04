import os

from dotenv import load_dotenv
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationSummaryMemory
from langchain_deepseek import ChatDeepSeek

load_dotenv()
llm = ChatDeepSeek(model="deepseek-chat", api_key=os.getenv("API_KEY"))

memory = ConversationSummaryMemory(llm=llm)

conversation_summary_chain = ConversationChain(llm=llm, memory=memory)

print(conversation_summary_chain.invoke({"input": "My name is Anthony."}))
print("-" * 50 + "\n")
print(
    conversation_summary_chain.invoke({"input": "How many countries are in the world?"})
)
print("-" * 50 + "\n")
print(
    conversation_summary_chain.invoke(
        {"input": "What is the weather in nigeria today, one line answer"}
    )
)
print("-" * 50 + "\n")
print(conversation_summary_chain.invoke({"input": "What is my name?"}))
