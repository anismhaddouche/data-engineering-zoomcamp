import pandas as pd 
from sqlalchemy import create_engine
import argparse
import os 



def main(params):
    user=params.user
    password=params.password
    host=params.host
    port = params.port
    db=params.db
    table_name=params.table_name
    url = params.url
    pq_name = 'output.pq'
    
    #Download csv
    # FOr macos 
   # os.system(f"curl -o {pq_name} {url}")
    # For linux
    os.system(f"wget {url} -O {pq_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    df = pd.read_parquet(pq_name)
    df.head(n=0).to_sql(name = table_name, con=engine, if_exists='replace')
    #TODO Add an iterator in ordler to upload data by batch
    df.to_sql(df.to_sql(name = table_name, con=engine, if_exists='append'))

    

   


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for for postgres')
    parser.add_argument('--port', help='port for for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='Table name where result will be writed')
    parser.add_argument('--url', help='Url for the csv file')

    args = parser.parse_args()
    main(args)



