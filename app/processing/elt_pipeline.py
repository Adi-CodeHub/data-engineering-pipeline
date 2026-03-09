import json
import os
import glob
import sqlite3

from app.utils.logger import get_logger
from app.ingestion.api_client import APIClient

logger = get_logger(__name__)

DB_PATH = "data/database.db"

class ELTPipeline:
    def __init__(self, api_url:str):
        self.api_url = api_url

    def extract(self):
        logger.info("ELT Extraction Started")

        client = APIClient(self.api_url)
        data = client.fetch_data()
        client.save_raw_data(data)

        logger.info("ELT Extraction Completed")

    def load_raw(self):
        logger.info("loading raw data into database")

        latest_file = max(glob.glob('data/raw/*.json'), key = os.path.getctime)

        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('Delete from raw_countries')
        for row in data:
            cursor.execute(" insert into raw_countries (data) values (?)", (json.dumps(row),))

        conn.commit()
        conn.close()
        logger.info("Raw data loaded into raw_countries table")

    
    def transform_sql(self):
        logger.info("Starting SQL Transformation")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS countries_elt")
        cursor.execute("""Create TABLE countries_elt AS 
                        select 
                            json_extract(data, '$.name.common') AS country,
                            json_extract(data, '$.region') AS region,
                            json_extract(data, '$.subregion') AS subregion,
                            json_extract(data, '$.population') AS population,
                            json_extract(data, '$.area') AS area
                        from raw_countries
                       """)
        conn.commit()
        conn.close()

        logger.info('SQL Transformation Completed')

    
    def run(self):
         logger.info("ELT Pipeline Started")
         
         self.extract()
         self.load_raw()
         self.transform_sql()
         
         logger.info("ELT Pipeline Completed")