import os
import traceback

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA
from langchain_deepseek import ChatDeepSeek
from langchain_huggingface import (
    HuggingFaceEmbeddings,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
api_key = os.getenv("API_KEY")

os.environ["RAG_DEMO_API_KEY"] = api_key

# PREPARE SIMPLE DOCUMENTS
document = """
Artificial.Intelligence.(AI) .is.transforming the way.we live and.work. Machine learning,
a subset of AI, enables.computers.to learn from.data without explicit programming.
Deep learning, a type of machine learning, uses.neural.networks .inspired.by the human brain.

Natural.Language Processing (NLP)-is.a.branch.of.AI.that.helps.computers.understand.and
process.human language. It's.used in applications.like translation, chatbots, and text analysis.

Computer Vision is another important field in.AI. It enables machines.to understand and
process.visual .information from the world, like images and videos. Applications include
facial recognition, autonomous vehicles, and medical image analysis.

Reinforcement.Learning is a type of machine learning where agents.learn by interacting
with an environment. They receive rewards for good actions and penalties for bad ones.
This is.used.in game playing, robotics, and.autonomous systems.
"""

print("Document Loaded. Lenggth", len(document), "Characters")

# step 2 : Text chunking
print("Step 2: Text Chunking")
print("-" * 50)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    length_function=len,
    separators=["\n\n", "\n", ". ", " "],
)

chunks = text_splitter.split_text(document)

print(f"Document split into {len(chunks)} chunks:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}\n")
    print("-" * 50)

# step 3 : Initialize Embeddings
print("Step 3: Initialize Embeddings")
print("-" * 50)

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

print("Embeddings Initialized.", embeddings.model_name)

# step 4 : Create and  populate vector store
print("Step 4: Create and Populate Vector Store")
print("-" * 50)

vector_store = Chroma.from_texts(
    texts=chunks, embedding=embeddings, persist_directory="./chroma.db"
)

print("Vector Store Created and Populated.")
print(f"Number of texts {len(chunks)}")
print(f" Embedding Dimension {len(embeddings.embed_query('test'))} ")

# step 5 : Similarity Search Example
# print("Step 5: Similarity Search Example")
# print("-" * 50)

# query = "What is reinforcemnt  learning"
# results = vector_store.similarity_search(query, k=2)

# print(f"Query: {query}")
# print(f"Top {len(results)} Results:")
# for i, result in enumerate(results):
#     print(f"Result {i + 1}: {result.page_content}\n")
#     print("-" * 50)

# step 6 set up rag with hugging face
# print("Step 6: Set up RAG with Hugging Face")
# print("-" * 50)

# endpoint = HuggingFaceEndpoint(
#     # repo_id="Qwen/Qwen2.5-7B-Instruct",
#     repo_id="deepset/roberta-base-squad2",
#     task="text-generation",
#     huggingfacehub_api_token=api_key,
#     temperature=0.1,
#     max_new_tokens=512,
# )
# llm = ChatHuggingFace(llm=endpoint)

# llm = HuggingFaceEndpoint(
#     repo_id="deepseek-ai/DeepSeek-R1",
#     task="text2text-generation",
#     huggingfacehub_api_token=api_key,
#     temperature=0,
#     max_new_tokens=512,
# )

llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=api_key,
    temperature=0.1,
    max_tokens=512,
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(),
)

questions = [
    "What is reinforcement learning and how does it work",
    "What are the main applications of computer vision",
    "How is NLP used in real world applications",
]

for question in questions:
    print(f"Question: {question}")
    try:
        result = qa_chain.invoke({"query": question})
        print(f"Answer: {result['result']}\n")
    except ValueError as e:
        # print("Error processing question:", e)
        print(f"Error type: {type(e).__name__}")
        traceback.print_exc()
