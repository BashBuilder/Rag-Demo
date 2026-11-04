# import os
# from pathlib import Path

# from dotenv import load_dotenv
# from langchain_classic.chains import create_sql_query_chain
# from langchain_community.utilities import SQLDatabase
# from langchain_deepseek import ChatDeepSeek

# load_dotenv()
# api_key = os.getenv("API_KEY")

# llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key)

# db_path = Path(__file__).resolve().parent.parent / "chroma.db" / "chroma.sqlite3"
# db = SQLDatabase.from_uri(f"sqlite:///{db_path.as_posix()}")

# print(db.get_usable_table_names())  # see what tables actually exist

# chain = create_sql_query_chain(llm, db)

# response = chain.invoke({"question": "How many collections are there?"})
# print(response)

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_classic.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key, temperature=0)

db_path = Path(__file__).resolve().parent.parent / "chroma.db" / "chroma.sqlite3"
db = SQLDatabase.from_uri(
    f"sqlite:///{db_path.as_posix()}",
    include_tables=["collections"],
    sample_rows_in_table_info=0,
)

print(db.get_usable_table_names())  # ['collections']

chain = create_sql_query_chain(llm, db)

response = chain.invoke({"question": "How many collections are there?"})
print(response)
