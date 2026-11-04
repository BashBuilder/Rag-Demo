# import os
# from pathlib import Path

# from crewai import LLM, Agent, Crew, Task
# from crewai_tools import ScrapeWebsiteTool, TXTSearchTool
# from dotenv import load_dotenv

# load_dotenv()

# llm = LLM(model="deepseek/deepseek-chat", api_key=os.getenv("API_KEY"))

# data_dir = Path(__file__).resolve().parent.parent / "data"
# data_dir.mkdir(exist_ok=True)
# txt_path = data_dir / "ai.txt"

# scrape_tool = ScrapeWebsiteTool(website_url="https://en.wikipedia.org")
# text = scrape_tool.run()

# print(text)
# print(txt_path)
# txt_path.write_text(text, encoding="utf-8")

# search_tool = TXTSearchTool(
#     txt=str(txt_path),
#     config={
#         "embedding_model": {
#             "provider": "huggingface",
#             # "config": {"model": "sentence-transformers/all-MiniLM-L6-v2"},
#             "config": {"model": "sentence-transformers/all-MiniLM-L6-v2"},
#         },
#         "vectordb": {
#             "provider": "chromadb",
#             "config": {},
#         },
#     },
# )

# data_analyst = Agent(
#     role="Educator",
#     goal="Answer questions accurately using the provided text file",
#     backstory="You are a data expert",
#     llm=llm,
#     tools=[search_tool],
#     verbose=True,
#     allow_delegation=False,
# )

# test_task = Task(
#     description="What are the uses of Wikipedia? Search the text file and answer.",
#     expected_output="A correct, concise answer",
#     agent=data_analyst,
# )

# crew = Crew(agents=[data_analyst], tasks=[test_task])
# output = crew.kickoff()
# print(output.raw)

import os
from pathlib import Path

from crewai import LLM, Agent, Crew, Task
from crewai.tools import tool
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

txt_path = Path(__file__).resolve().parent.parent / "data" / "ai.txt"
text = txt_path.read_text(encoding="utf-8")

chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_text(
    text
)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
store = Chroma.from_texts(chunks, embedding=embeddings, persist_directory="./scrape")
retriever = store.as_retriever(search_kwargs={"k": 4})


@tool("Search text file")
def search_text(query: str) -> str:
    """Search the scraped text file and return the most relevant passages."""
    docs = retriever.invoke(query)
    return "\n\n".join(d.page_content for d in docs)


llm = LLM(model="deepseek/deepseek-chat", api_key=os.getenv("API_KEY"))

analyst = Agent(
    role="Educator",
    goal="Answer questions accurately using the provided text",
    backstory="You are a data expert",
    llm=llm,
    tools=[search_text],
    allow_delegation=False,
)

task = Task(
    description="What are the uses of Wikipedia? Search the text and answer.",
    expected_output="A correct, concise answer",
    agent=analyst,
)

print(Crew(agents=[analyst], tasks=[task]).kickoff().raw)
