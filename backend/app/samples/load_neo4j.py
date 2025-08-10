
from neo4j import GraphDatabase
import os, time

uri = os.getenv('NEO4J_URI','bolt://neo4j:7687')
user = os.getenv('NEO4J_USER','neo4j')
passw = os.getenv('NEO4J_PASSWORD','password')

driver = GraphDatabase.driver(uri, auth=(user, passw))

with driver.session() as s:
    s.run("CREATE CONSTRAINT IF NOT EXISTS FOR (o:Order) REQUIRE o.id IS UNIQUE")
    s.run("MERGE (o:Order {id:'ORD-123', created_at: date()})")
    s.run("MERGE (s:Supplier {id:'SUP-1', name:'Acme Supplies', region:'IN'})")
    s.run("MERGE (s2:Supplier {id:'SUP-2', name:'Beta Logistics', region:'CN'})")
    s.run("MATCH (o:Order {id:'ORD-123'}), (s:Supplier {id:'SUP-1'}) MERGE (o)-[:ORDERED_FROM]->(s)")
    s.run("MATCH (o:Order {id:'ORD-123'}), (s:Supplier {id:'SUP-2'}) MERGE (o)-[:ORDERED_FROM]->(s)")

print('neo4j sample data loaded')
