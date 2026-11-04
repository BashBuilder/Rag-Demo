import os

from dotenv import load_dotenv
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_deepseek import ChatDeepSeek

load_dotenv()
llm = ChatDeepSeek(model="deepseek-chat", api_key=os.getenv("API_KEY"))

memory = ConversationBufferWindowMemory(k=2)

conversation_window_chain = ConversationChain(llm=llm, memory=memory)

print(conversation_window_chain.invoke({"input": "My name is Anthony."}))
print("-" * 50 + "\n")
print(
    conversation_window_chain.invoke({"input": "How many countries are in the world?"})
)
print("-" * 50 + "\n")
print(
    conversation_window_chain.invoke(
        {"input": "What is the weather in nigeria today, one line answer"}
    )
)
print("-" * 50 + "\n")
print(conversation_window_chain.invoke({"input": "What is my name?"}))
