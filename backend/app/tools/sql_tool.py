
import asyncpg
import os

POSTGRES_DSN = os.getenv('POSTGRES_DSN','postgresql://postgres:postgres@postgres:5432/postgres')

class SQLTool:
    def __init__(self):
        pass

    async def run(self, intent: str, params: dict):
        q = params.get('query','')
        try:
            conn = await asyncpg.connect(POSTGRES_DSN)
        except Exception as e:
            return {"error": f"cannot connect to postgres: {e}"}
        try:
            rows = await conn.fetch("SELECT shipment_id, status, planned_eta, actual_eta, order_id FROM shipments WHERE order_id::text LIKE $1 LIMIT 100", f"%{q}%")
            return [dict(r) for r in rows]
        finally:
            await conn.close()
