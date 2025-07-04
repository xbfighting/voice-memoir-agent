import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
memory = []

# 简化：内存中保持文本列表

def add_to_memory(text):
    emb = model.encode([text])
    index.add(emb)
    memory.append(text)

def query_memory(text, top_k=3):
    emb = model.encode([text])
    D, I = index.search(emb, top_k)
    return "\n".join([memory[i] for i in I[0] if i < len(memory)])