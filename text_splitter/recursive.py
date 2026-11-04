from langchain_text_splitters import RecursiveCharacterTextSplitter

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

splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30,
    length_function=len,
    separators=["\n\n", "\n", " ", " "],
)

chunks = splitter.split_text(sample_text)
chunks = splitter.split_text(sample_text)
print(chunks)
print(type(chunks))
print(len(chunks))
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}\n")
    print("-" * 50)
