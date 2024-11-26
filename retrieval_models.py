import os
from sklearn.feature_extraction.text import TfidfVectorizer
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load data files from the 'data' directory
def load_data(data_dir="data"):
    texts = []
    for root, _, files in os.walk(data_dir):
        for file in files:
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts

# TF-IDF Retrieval
def tfidf_retrieval(query, texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    top_indices = np.argsort(similarities)[::-1][:3]  # Top 3 results
    return [texts[i] for i in top_indices]

# KeyBERT Retrieval
def keybert_retrieval(query, texts):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(query, keyphrase_ngram_range=(1, 2), stop_words='english')
    extracted_keywords = [kw[0] for kw in keywords]
    results = [text for text in texts if any(keyword in text for keyword in extracted_keywords)]
    return results[:3]  # Top 3 results

# Hugging Face Retrieval
def huggingface_retrieval(query, texts):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_embedding = model.encode([query], convert_to_tensor=True)
    text_embeddings = model.encode(texts, convert_to_tensor=True)
    similarities = cosine_similarity(
        query_embedding.cpu().numpy(),
        text_embeddings.cpu().numpy()
    ).flatten()
    top_indices = np.argsort(similarities)[::-1][:3]  # Top 3 results
    return [texts[i] for i in top_indices]

# Unified function for app.py
def retrieve_documents(query, method="tfidf", data_dir="data"):
    texts = load_data(data_dir)
    if method == "tfidf":
        return tfidf_retrieval(query, texts)
    elif method == "keybert":
        return keybert_retrieval(query, texts)
    elif method == "huggingface":
        return huggingface_retrieval(query, texts)
    else:
        raise ValueError("Unsupported retrieval method. Choose from 'tfidf', 'keybert', or 'huggingface'.")

# Main function for testing
if __name__ == "__main__":
    query = "artificial intelligence"
    print("TF-IDF Retrieval:")
    print(retrieve_documents(query, method="tfidf"))
    print("\nKeyBERT Retrieval:")
    print(retrieve_documents(query, method="keybert"))
    print("\nHugging Face Retrieval:")
    print(retrieve_documents(query, method="huggingface"))
