import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

class ConsultaSQL:
    def __init__(self):
        load_dotenv()
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
            )

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query):
        if not self.conn:
            raise ConnectionError(
                'Conexão com o banco de dados não estabelecida.'
            )
        return pd.read_sql_query(query, self.conn)

    def save_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)
        print(f'Dados salvos em {file_path}.')

    def run(self, query, output_file):
        self.connect()
        df = self.execute_query(query)
        self.save_to_csv(df, output_file)
        self.disconnect()
