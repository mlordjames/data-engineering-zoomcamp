#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import argparse
from sqlalchemy import create_engine
from time import time
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_name = 'yellow_tripdata_2022.parquet'

    os.system(f"wget {url} -O {parquet_name}")
    


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_parquet(parquet_name, engine='fastparquet')

    df.columns = [c.lower() for c in df.columns]
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name =table_name, con = engine, if_exists='replace')

    df.to_sql(name =table_name, con = engine, if_exists='append', chunksize=100000)
    print("extraction completed")

 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data ingestion into PostgreBD')

    parser.add_argument('--user', help='username for the PostgreBD')
    parser.add_argument('--password', help='password for the PostgreBD')
    parser.add_argument('--host', help='host for the PostgreBD')
    parser.add_argument('--port', help='port for the PostgreBD')
    parser.add_argument('--db', help='the postgresql')
    parser.add_argument('--table_name', help='name of the table to write to')
    parser.add_argument('--url', help='url of the file')


    args = parser.parse_args()

    main(args)








