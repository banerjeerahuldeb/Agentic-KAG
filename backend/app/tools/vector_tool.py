
from app.utils.embeddings import get_embedding
import faiss
import numpy as np
import pickle
import os

INDEX_PATH = '/data/faiss_index.bin'
META_PATH = '/data/faiss_meta.pkl'

class VectorTool:
    def __init__(self):
        if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
            try:
                self.index = faiss.read_index(INDEX_PATH)
                with open(META_PATH, 'rb') as f:
                    self.meta = pickle.load(f)
            except Exception as e:
                print("Failed to load FAISS index:", e)
                self.index = None
                self.meta = []
        else:
            self.index = None
            self.meta = []

    async def run(self, intent: str, params: dict):
        q = params.get('query','')
        try:
            embedding = get_embedding(q)
        except Exception as e:
            return {"error": f"embedding failure: {e}"}
        if self.index is None:
            return []
        D, I = self.index.search(np.array([embedding]).astype('float32'), 5)
        results = []
        for dist, idx in zip(D[0], I[0]):
            if idx < 0 or idx >= len(self.meta):
                continue
            meta = self.meta[idx]
            results.append({"score": float(dist), "meta": meta})
        return results
