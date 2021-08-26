import os
from dotenv import load_dotenv
import psycopg2 as pg2

def db_connection_setup():
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
    
    return conn

conn = db_connection_setup()

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS size (
    size_id SERIAL NOT NULL,
    size_name VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY(size_id)
    );
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS product_name(
    product_name_id SERIAL NOT NULL,
    name VARCHAR NOT NULL,
    PRIMARY KEY(product_name_id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS card_type(
    card_type_id SERIAL NOT NULL,
    type VARCHAR NOT NULL,
    PRIMARY KEY(card_type_id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS payment_type(
    payment_type_id SERIAL NOT NULL,
    method VARCHAR NOT NULL,
    PRIMARY KEY(payment_type_id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS branch (
    branch_id SERIAL NOT NULL,
    location VARCHAR(255) NOT NULL,
    PRIMARY KEY(branch_id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS product_detail (
    product_detail_id SERIAL NOT NULL,
    size_id INT references size(size_id) NOT NULL,
    product_name_id INT references product_name(product_name_id) NOT NULL,
    price FLOAT NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS transaction(
    transaction_id SERIAL NOT NULL,
    payment_type_id INT references payment_type(payment_type_id) NOT NULL,
    branch_id INT references branch(branch_id) NOT NULL,
    card_type_id INT references card_type(card_type_id) NOT NULL,
    time_stamp  TIMESTAMP ,
    total_price FLOAT NOT NULL,
    PRIMARY KEY(transaction_id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS basket (
    transaction_id INT NOT NULL,
    product_details_id INT NOT NULL, 
    quantity INT NOT NULL,
    CONSTRAINT fk_transaction
    FOREIGN KEY(transaction_id) 
    REFERENCES transaction (transaction_id));
""")

# print(cur.fetchone())

conn.commit()