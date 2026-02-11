from langchain_ollama import OllamaEmbeddings

def get_embedding_function():
    # Comment out Bedrock and use Ollama instead
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
