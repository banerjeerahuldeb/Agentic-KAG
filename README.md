
# Agentic KAG

This scaffold contains a minimal runnable starter project for a Knowledge-Augmented Generator (KAG):
- FastAPI backend (planner + executor)
- Neo4j sample loader
- Postgres sample loader
- FAISS vector tool (index persistence expected at /data)
- Minimal React frontend (Vite)

## Quickstart (local)
1. Copy `.env.example` to `.env` and fill values (OPENAI_API_KEY if you want embeddings).
2. Start services with Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Once containers are up, run demo data loader (or use the provided script):
   ```bash
   ./scripts/demo_data.sh
   ```
4. Open the API at http://localhost:8000/docs for the FastAPI interactive docs.
5. Frontend (if you want to run): `cd frontend && npm install && npm run dev` (or serve built files).

## Notes
- This is a starter scaffold. Replace the Planner with LLM-driven planner and secure credentials for production.
