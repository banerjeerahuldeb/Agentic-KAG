
import asyncpg, asyncio, os, time

dsn = os.getenv('POSTGRES_DSN','postgresql://postgres:postgres@postgres:5432/postgres')

async def main():
    conn = await asyncpg.connect(dsn)
    await conn.execute("""CREATE TABLE IF NOT EXISTS shipments (
        shipment_id serial PRIMARY KEY,
        order_id text,
        status text,
        planned_eta timestamp,
        actual_eta timestamp,
        delay_reason text
    );""")
    await conn.execute("INSERT INTO shipments (order_id, status, planned_eta, actual_eta, delay_reason) VALUES ($1,$2,$3,$4,$5)",
                       'ORD-123', 'delayed', '2025-07-01', '2025-07-10', 'port congestion')
    await conn.close()
    print('postgres sample data loaded')

if __name__ == '__main__':
    asyncio.run(main())
