
from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv('NEO4J_URI','bolt://neo4j:7687')
NEO4J_USER = os.getenv('NEO4J_USER','neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD','password')

class GraphTool:
    def __init__(self):
        try:
            self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        except Exception as e:
            self.driver = None
            print("Could not create Neo4j driver:", e)

    async def run(self, intent: str, params: dict):
        q = params.get('query','')
        if not self.driver:
            return {"error": "neo4j driver not available"}
        cypher = (
            "MATCH (o:Order)-[:ORDERED_FROM]->(s:Supplier) "
            "WHERE toLower(o.id) CONTAINS toLower($q) OR toLower(o.id) = toLower($q) "
            "RETURN o.id AS order_id, collect(s { .id, .name, .region }) AS suppliers LIMIT 50"
        )
        with self.driver.session() as session:
            res = session.run(cypher, q=q)
            rows = [dict(r) for r in res]
        return rows
