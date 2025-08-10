
import asyncio
from app.tools.graph_tool import GraphTool
from app.tools.sql_tool import SQLTool
from app.tools.vector_tool import VectorTool

class Executor:
    def __init__(self):
        self.graph = GraphTool()
        self.sql = SQLTool()
        self.vector = VectorTool()

    async def execute_action(self, action: dict):
        tool = action.get('tool')
        intent = action.get('intent')
        params = action.get('params', {})
        if tool == 'GRAPH':
            return await self.graph.run(intent, params)
        if tool == 'SQL':
            return await self.sql.run(intent, params)
        if tool == 'VECTOR':
            return await self.vector.run(intent, params)
        if tool == 'TEXT':
            return {"error":"no text tool"}
        return {"error":"unknown tool"}

    async def execute_plan(self, actions: list) -> dict:
        coros = [self.execute_action(a) for a in actions]
        results = await asyncio.gather(*coros, return_exceptions=True)
        out = {}
        for i, r in enumerate(results):
            if isinstance(r, Exception):
                out[f"action_{i}"] = {"error": str(r)}
            else:
                out[f"action_{i}"] = r
        return out
