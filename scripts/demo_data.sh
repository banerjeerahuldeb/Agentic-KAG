
#!/bin/bash
set -e
echo "Waiting for databases to come up..."
sleep 8
python backend/app/samples/load_neo4j.py || true
python backend/app/samples/load_postgres.py || true
echo "Demo data load attempted."
