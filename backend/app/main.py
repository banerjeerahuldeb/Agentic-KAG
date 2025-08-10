
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.planner import Planner
from app.executor import Executor

app = FastAPI(title="KAG Starter API")

planner = Planner()
executor = Executor()

class QueryRequest(BaseModel):
    query: str
    user_id: str | None = None

@app.post('/query')
async def query_endpoint(req: QueryRequest):
    try:
        plan = planner.create_plan(req.query)
        result = await executor.execute_plan(plan)
        final_answer = planner.generate_answer(req.query, result)
        return {"plan": plan, "result": result, "answer": final_answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
