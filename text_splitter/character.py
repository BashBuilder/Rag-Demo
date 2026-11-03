from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

# input document
sample_text = """
# Introduction to Machine Learning

Machine Learning (ML) is a subset of artificial intelligence that enables systems to learn and improve from

## Types of Machine Learning

### Supervised Learning
Supervised learning is where the model is trained on a labeled dataset. The model learns to predict the outp
- Classification
- Regression
- Neural Networks

### Unsupervised Learning
Unsupervised learning is where the model works on its own to discover patterns and information. Common examp
- Clustering
- Dimensionality Reduction
- Association

## Applications

Machine Learning has numerous real-world applications:
1. Image Recognition
2. Natural Language Processing
3. Recommendation Systems
4. Fraud Detection

"""

splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=200,
    chunk_overlap=50,
)

chunks = splitter.split_text(sample_text)
print(chunks)
print(type(chunks))
print(len(chunks))
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}\n")
    print("-" * 50)
