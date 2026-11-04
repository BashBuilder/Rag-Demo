import os

from langchain_community.document_loaders import UnstructuredHTMLLoader

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "example.html")

loader = UnstructuredHTMLLoader(file_path)
data = loader.load()
print(data)
print(type(data))
