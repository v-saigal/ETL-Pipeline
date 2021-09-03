
import os
from typing import final
import psycopg2 as pg2
from datetime import datetime
from ETL.extract import Extract
import boto3
from ETL.transform import get_unique_item_key, transform_transaction_format, get_unique_item
from ETL.helper_modules.helper_funcs import pretty_print_dict

# Set up connection
def db_connection_setup():
    client = boto3.client('redshift', region_name='eu-west-1')
    
    redshift_user = os.environ.get("redshift_user")
    redshift_cluster = os.environ.get("redshift_cluster")
    redshift_database = os.environ.get("redshift_database")
    host = os.environ.get("redshift_host")
    port = os.environ.get("redshift_port")
    
    creds = client.get_cluster_credentials(
      DbUser=redshift_user,
      DbName=redshift_database,
      ClusterIdentifier=redshift_cluster,
      DurationSeconds=3600)
    
    conn = pg2.connect(
        user=creds["DbUser"], 
        password=creds["DbPassword"],
        host=host,
        database=redshift_database,
        port=port            
    )

    return conn

# def get_sql_query(sql):
#     conn = db_connection_setup()
#     cur = conn.cursor()
    
#     cur.execute(sql)
    
#     return cur.fetchall()

def compare_get_query_id(sql, value):
    conn = db_connection_setup()
    cur = conn.cursor()
    cur.execute(sql)
    
    row = cur.fetchall()
    # print(row)
    for item in row:
        # print('loop over item:',item)
        if item[1] == value:
            return item[0]

# conn = db_connection_setup()
# cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# cur.execute(\
#     """
#         TRUNCATE TABLE size;        
#     """)
# conn.commit()

# cur.execute("""
#     SELECT * FROM test;
# """)

# print(cur.fetchall())

## Skeleton code when loading
def load_test():
    basket = transform_transaction_format()
    sql = """
        INSERT INTO load_test (product_name, quantity)
        VALUES (%s, %s)
    """

    for data in basket:
        print(data)

##############################
# Product side
def load_size(data):
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
            # print(cur.fetchall())
        except:
            print('cannot be added')
        finally:
            conn.commit()

    cur.close()
    conn.close()
    
def load_product_detail(item, conn, cur):
    conn = db_connection_setup()
    cur = conn.cursor()
    
    sql_product_details = \
    """
        INSERT INTO product_detail(size_id, product_name_id, price)
        VALUES (%s, %s, %s)
    """
    try:
        ## Load product_detail table
        id_for_size = compare_get_query_id('SELECT * FROM size', item['size'])
        id_for_product_name = compare_get_query_id('SELECT * FROM product_name', item['name'])
        values = (id_for_size, id_for_product_name, float(item['price']))
        
        print('test:', id_for_size, id_for_product_name)
        cur.execute(F"""
                        SELECT * FROM product_detail
                        WHERE size_id = {id_for_size} AND product_name_id = {id_for_product_name} AND price = {item['price']}
                    """)
        
        if cur.fetchone() is None:
            print('There is nothing similar')
            cur.execute(sql_product_details, values, )
        else:
            print('There is already something similar')

    except Exception as e:
        print('Cannot add to product_detail', e)
    finally:
        conn.commit()

def load_product_side(data):
    # Get unique products with size and size
    unique_item = get_unique_item(data)
    
    pretty_print_dict(unique_item)

    sql_product_name = \
        """
            INSERT INTO product_name(product_name)
            VALUES (%s)
            RETURNING product_name_id
        """


    conn = db_connection_setup()
    cur = conn.cursor()

    for item in unique_item:
        try:
            ## Load product_name table
            cur.execute(sql_product_name, (item['name'], ))
        except Exception as e:
            print('Cannot add this product: ', e)

        finally:
            conn.commit()
        
        load_product_detail(item, conn, cur)

    cur.close()
    conn.close()


# load_product()
# load_size()

# load_product_side()

###################################
# Transaction side
def load_branch(data):
    unique_branch = get_unique_item_key('store_location', data)
    print(unique_branch)
    sql = \
        """
            INSERT INTO branch(location)
            VALUES(%s)
            RETURNING branch_id
        """
    conn = db_connection_setup()
    cur = conn.cursor()

    for branch in unique_branch: 
        try:
            cur.execute(sql, (branch,))

        except Exception as e:
            print('Cannot add branch', e)
        finally:
            conn.commit()

    cur.close()
    conn.close()


def load_payment_type(data):
    unique_payment = get_unique_item_key('payment_type', data)
    sql = \
        """
            INSERT INTO payment_type(method)
            VALUES(%s)
            RETURNING payment_type_id
        """

    conn = db_connection_setup()
    cur = conn.cursor()
    
    for payment in unique_payment:
        try:
            cur.execute(sql, (payment,) )

        except Exception as e:
            print('Cannot add payment', e)
        finally:
            conn.commit()

    cur.close()
    conn.close()


# def load_card_type(data):
#     unique_card_type = get_unique_item_key('card_type', data)
#     sql = \
#         """
#             INSERT INTO card_type(type)
#             VALUES(%s)
#         """
#     conn = db_connection_setup()
#     cur = conn.cursor()
    
#     for card_type in unique_card_type:
#         try:
#             cur.execute(sql, (card_type,) )

#         except Exception as e:
#             print('Cannot add card_type', e)
#         finally:
#             conn.commit()

#     cur.close()
#     conn.close()

def basket_load(transaction_with_quantity, transaction_id, count):
        sql_basket = \
        """
            INSERT INTO basket (transaction_id, product_detail_id, quantity)
            VALUES (%s, %s, %s)
        """
        conn = db_connection_setup()
        cur = conn.cursor()
        for basket_list in transaction_with_quantity[count]:
            for key, value in basket_list.items():
                key_split = key.split(',')
                print(key_split, value)
                size_id = compare_get_query_id('SELECT * FROM size', key_split[0])
                name_id = compare_get_query_id('SELECT * FROM product_name', key_split[1])
                
    
                print(size_id, name_id)
                cur.execute(f"""
                                SELECT product_detail_id
                                FROM product_detail
                                WHERE size_id = {size_id} AND product_name_id = {name_id}
                            """)
                product_detail_id = cur.fetchone()[0]
                print('details', product_detail_id)
                sql_value = (transaction_id, product_detail_id, int(value),)
                print(sql_value)
                print(sql_basket)
                cur.execute(sql_basket, sql_value)

                conn.commit()
        cur.close()
        conn.close()

def load_transaction_side(data):
    extract = Extract()
    # data = extract.extract_dict("../../data/cleaned_data.csv")
    transaction_with_quantity = transform_transaction_format(data)
    
    conn = db_connection_setup()
    cur = conn.cursor()
    
    sql = \
        """
            INSERT INTO transaction (payment_type_id, branch_id, time_stamp, total_price)
            VALUES (%s, %s, %s, %s)
            RETURNING transaction_id
        """
    load_branch(data)
    load_payment_type(data)
    # load_card_type(data)
    
    count = 0
    for each_transaction in data:
        # print(each_transaction)
        payment_type_val = compare_get_query_id('SELECT * FROM payment_type', each_transaction['payment_type'])
        branch_val = compare_get_query_id('SELECT * FROM branch', each_transaction['store_location'])
        # card_type_val = compare_get_query_id('SELECT * FROM card_type', each_transaction['card_type'])
        print(each_transaction['timestamp'])
        time = datetime.strptime(each_transaction['timestamp'], '%d/%m/%Y %H:%M')
        
        values = (payment_type_val, branch_val, time, float(each_transaction['total_price']))
        # print('values: ',values)
        try:
            cur.execute(sql, values, )
            transaction_id = cur.lastrowid
        except Exception as e:
            print('Cannot add transaction', e)
        finally:
            conn.commit()
        
        basket_load(transaction_with_quantity, transaction_id, count)
        # product_details_id = compare_get_query_id()
        
        count += 1 
    
    cur.close()
    conn.close()

def load_data(data):
    load_size(data)
    load_product_side(data)
    print('Transaction side loading')
    load_transaction_side(data)