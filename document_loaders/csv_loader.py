import os

from langchain_community.document_loaders import CSVLoader

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "data", "customers-100.csv")

loader = CSVLoader(file_path=file_path)

data = loader.load()
# print(data)
print(type(data))
print(data[0])
