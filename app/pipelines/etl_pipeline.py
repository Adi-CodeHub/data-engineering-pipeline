from app.ingestion.api_client import APIClient
from app.processing.validator import DataValidator
from app.processing.cleaner import DataCleaner
from app.processing.transformer import DataTransformer
from app.storage.database import DatabaseManager
from app.utils.logger import get_logger
import glob 
import os

logger = get_logger(__name__)

class ETLPipeline:

    def __init__(self, api_url:str):
        self.api_url = api_url

    def extract(self):
        logger.info("Starting Extraction Step")

        client = APIClient(self.api_url)
        data = client.fetch_data()
        client.save_raw_data(data)

        logger.info("Extraction completed")

    def validate(self):
        logger.info("Starting Data Validation")

        latest_file = max(glob.glob("data/raw/*json"), key=os.path.getctime)
        validator = DataValidator(latest_file)
        validator.load_raw_data()
        validator.convert_to_dataframe()
        validator.generate_schema_report()

        logger.info("Validation completed")
        return validator.df
    
    def transform(self, df):

        logger.info("Starting Data Transformation")

        cleaner = DataCleaner(df)
        clean_df = cleaner.clean()

        transformer = DataTransformer(clean_df)
        countries, regions, languages, currencies = transformer.transform()

        logger.info("Transformation Completed")
        return countries, regions, languages, currencies
    
    def load(self, countries, regions, languages, currencies):
        logger.info("Starting Loading data in DB")

        db = DatabaseManager()
        db.create_tables()
        db.load_dataframe(countries, "countries")
        db.load_dataframe(regions, "regions")
        db.load_dataframe(languages, "languages")
        db.load_dataframe(currencies, "currencies")

        db.close()

        logger.info("Loading Data completed")

    def run(self):
        logger.info("ETL pipeline started")
        self.extract()
        df = self.validate()
        countries, regions, languages, currencies = self.transform(df)
        self.load(countries, regions, languages, currencies)
        logger.info("ETL pipeline finished successfully")

