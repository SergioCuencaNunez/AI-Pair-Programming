apt-get update && apt-get upgrade
apt-get install sqlite3
sqlite3 test.db '.read ./ai_docs/databases.sql'