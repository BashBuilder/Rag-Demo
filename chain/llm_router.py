import os

from dotenv import load_dotenv
from langchain_classic.chains.router import MultiPromptChain
from langchain_deepseek import ChatDeepSeek

load_dotenv()
api_key = os.getenv("API_KEY")

llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key)

# Route templates
beginner_template = """You are a physics teacher who is really
focused on beginners and explaining complex topics in simple to understand terms.
You assume no prior knowledge. Here is the question\n{input}"""

expert_template = """You are a world expert physics professor who explains physics topics
to advanced audience members. You can assume anyone you answer has a
PhD level understanding of Physics. Here is the question\n{input}"""

empty_template = """{input}"""

# Route prompts
prompt_infos = [
    {
        "name": "empty",
        "description": "Replies to empty questions",
        "prompt_template": empty_template,
    },
    {
        "name": "advanced physics",
        "description": "Answers advanced physics questions",
        "prompt_template": expert_template,
    },
    {
        "name": "beginner physics",
        "description": "Answers basic beginner physics questions",
        "prompt_template": beginner_template,
    },
]

chain = MultiPromptChain.from_prompts(llm, prompt_infos, verbose=True)

print(chain.invoke("How do magnets work explain"))
print("-" * 50)

print(chain.invoke("How do feyman diagrams works"))
print("-" * 50)
