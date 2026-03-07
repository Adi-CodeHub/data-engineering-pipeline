import sqlite3
from app.utils.logger import get_logger

logger = get_logger(__name__)

DB_PATH = "data/etl.db"

class DatabaseManager:
    
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        
    def create_tables(self):
        cursor = self.conn.cursor()
        
        cursor.execute("""
        create table if not exists countries(
            country TEXT PRIMARY KEY,
            region TEXT,
            subregion TEXT,
            population INTEGER,
            area REAL,
            capital TEXT,
            currencies TEXT,
            languages TEXT,
            timezones TEXT,
            is_independent BOOLEAN,
            population_density REAL
        )    
        """)    
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS regions (
            region TEXT PRIMARY KEY,
            total_population INTEGER,
            avg_population REAL,
            country_count INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS languages (
            country TEXT,
            language TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS currencies (
            country TEXT,
            currency TEXT
        )
        """)
        
        self.conn.commit()
        
        logger.info("Database tables created")
        
    
    def load_dataframe(self, df, table_name):
        try:
            df.to_sql(
                table_name, self.conn, if_exists = "replace", index=False
            )
            
            logger.info(f"Data loaded into {table_name}")
            
        except Exception as e:
            logger.error(f"Failed loading {table_name}: {e}")
            raise
            
    def close(self):
        self.conn.close()
        
    