import os

from dotenv import load_dotenv
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=api_key,
    temperature=0.7,
)

memory = ConversationBufferMemory()

conversation_buffer_chain = ConversationChain(llm=llm, memory=memory)

print("Message 1:")
print("-" * 50 + "\n")
print(
    conversation_buffer_chain.invoke({"input": "Hello, my name is anthony"})["response"]
)

print("Message 2:")
print("-" * 50 + "\n")
print(
    conversation_buffer_chain.invoke(
        {"input": "What is the weather in nigeria today, one line answer"}
    )["response"]
)

print("Message 3:")
print("-" * 50 + "\n")
print(conversation_buffer_chain.invoke({"input": "What is my name?"})["response"])

print("Memory contents:")
print("-" * 50 + "\n")
print(memory.chat_memory.messages)
