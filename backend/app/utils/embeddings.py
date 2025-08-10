
import os
import openai

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY

def get_embedding(text: str):
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set. Set it in .env to use embeddings.")
    resp = openai.Embedding.create(model='text-embedding-3-small', input=text)
    return resp['data'][0]['embedding']
