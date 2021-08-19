import os
from dotenv import load_dotenv
import psycopg2 as pg2

load_dotenv()

load_dotenv()
host = os.environ.get("postgres_host")
user = os.environ.get("postgres_user")
password = os.environ.get("postgres_pass")
warehouse_db_name = os.environ.get("postgres_db")

conn = pg2.connect(
    user=user, 
    password=password,
    host=host,
    database=warehouse_db_name            
)

cur = conn.cursor()

cur.execute("""
    SELECT * FROM test
""")

print(cur.fetchone())