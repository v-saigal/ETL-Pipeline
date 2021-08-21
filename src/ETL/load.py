import os
from dotenv import load_dotenv
import psycopg2 as pg2
import psycopg2.extras

from transform import transform_transaction_format, get_unique_item
from helper_modules.helper_funcs import pretty_print_dict

# Set up connection
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
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

cur.execute(\
    """
        TRUNCATE TABLE size;        
    """)
conn.commit()

cur.execute("""
    SELECT * FROM test;
""")

print(cur.fetchall())

## Skeleton code when loading
def load_test():
    basket = transform_transaction_format()
    sql = """
        INSERT INTO load_test (product_name, quantity)
        VALUES (%s, %s)
    """

    for data in basket:
        print(data)

def load_size():
    conn = db_connection_setup()
    cur = conn.cursor()
    sql = \
        '''
            INSERT INTO size (size_name)  
            VALUES (%s)
            RETURNING size_id
        '''
    
    sizes = ['large', 'regular']
    
    for one_data in sizes:
        try:
            cur.execute(sql, (one_data,))
            print(cur.fetchall())
        except:
            print('cannot be added')
    
    conn.commit()
    cur.close()
    conn.close()

def load_product():
    basket = transform_transaction_format()
    pretty_print_dict(basket)

# load_product()
load_size()
