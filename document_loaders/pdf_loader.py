import os

from langchain_community.document_loaders import PyPDFLoader

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "sample.pdf")

loader = PyPDFLoader(file_path)
data = loader.load()
# print(data)
print(type(data))
print(data[0].page_content)
print(data[0].metadata)
