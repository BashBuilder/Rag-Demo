import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_deepseek import ChatDeepSeek
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict

load_dotenv()

llm = ChatDeepSeek(model="deepseek-chat", api_key=os.getenv("API_KEY"), temperature=0)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


class State(TypedDict):
    url: str
    question: str
    chunks: list[str]
    context: str
    answer: str


def scrape(state: State):
    text = WebBaseLoader(state["url"]).load()[0].page_content
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return {"chunks": splitter.split_text(text)}


def retrieve(state: State):
    store = Chroma.from_texts(state["chunks"], embedding=embeddings)
    docs = store.similarity_search(state["question"], k=4)
    return {"context": "\n\n".join(d.page_content for d in docs)}


def answer(state: State):
    prompt = (
        "You are an educator. Answer using only the context below.\n\n"
        f"Context:\n{state['context']}\n\nQuestion: {state['question']}"
    )
    return {"answer": llm.invoke(prompt).content}


builder = StateGraph(State)
builder.add_node("scrape", scrape)
builder.add_node("retrieve", retrieve)
builder.add_node("answer", answer)
builder.add_edge(START, "scrape")
builder.add_edge("scrape", "retrieve")
builder.add_edge("retrieve", "answer")
builder.add_edge("answer", END)

graph = builder.compile()

result = graph.invoke(
    {"url": "https://en.wikipedia.org", "question": "What are the uses of Wikipedia?"}
)
print(result["answer"])
