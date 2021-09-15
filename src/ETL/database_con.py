import os
import boto3

import psycopg2 as pg2

# Set up connection
class DbConn:
    def __init__(self):
        print('Starting to connection')

    def db_connection_setup(self):
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