from ETL.load import db_connection_setup

def create_tables():
    print('creating tables')
    conn = db_connection_setup()
    cur = conn.cursor()
    
    try: 
        cur.execute("""
        CREATE TABLE IF NOT EXISTS size(
            size_id SERIAL NOT NULL,
            size_name VARCHAR(255) UNIQUE NOT NULL,
            PRIMARY KEY(size_id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS product_name(
            product_name_id SERIAL NOT NULL,
            product_name VARCHAR UNIQUE NOT NULL,
            PRIMARY KEY(product_name_id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS product_detail (
            product_detail_id SERIAL NOT NULL,
            size_id INT references size(size_id) NOT NULL,
            product_name_id INT references product_name(product_name_id) NOT NULL,
            price FLOAT NOT NULL,
            PRIMARY KEY(product_detail_id)
        );
        """)
        # 
        cur.execute("""
        CREATE TABLE IF NOT EXISTS payment_type(
            payment_type_id SERIAL NOT NULL,
            method VARCHAR(255) UNIQUE NOT NULL,
            PRIMARY KEY(payment_type_id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS branch(
            branch_id SERIAL NOT NULL,
            location VARCHAR(255) UNIQUE NOT NULL,
            PRIMARY KEY(branch_id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS transaction(
            transaction_id SERIAL NOT NULL,
            payment_type_id INT references payment_type(payment_type_id) NOT NULL,
            branch_id INT references branch(branch_id) NOT NULL,
            time_stamp  TIMESTAMP ,
            total_price FLOAT NOT NULL,
            PRIMARY KEY(transaction_id)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS basket(
            transaction_id INT references transaction(transaction_id) NOT NULL,
            product_detail_id INT references product_detail(product_detail_id) NOT NULL,
            quantity INT NOT NULL
        );
        """)
    
    except Exception as e:
        print(e)
    
    finally:
        conn.commit()
    
    cur.close()
    conn.close()