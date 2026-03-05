import os
import json
import pandas as pd
from app.utils.logger import get_logger

logger = get_logger(__name__)

class DataValidator:
    def __init__(self, file_path:str):
        self.file_path = file_path
        self.data = None
        self.df = None

    def load_raw_data(self):
        try:
            logger.info(f'Loading raw file: {self.file_path}')
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            logger.info('Raw data loaded successfully.')

        except Exception as e:
            logger.error(f'Failed to load raw data : {e}')
            raise

    def convert_to_dataframe(self):
        try:
            self.df = pd.json_normalize(self.data)
            logger.info('Converted JSON to Dataframe.')

        except Exception as e:
            logger.error(f'Failed to convert JSON into Dataframe: {e}')
            raise

    def generate_schema_report(self):
        try:
            logger.info('Generating Schema Report...')

            schema_report={
                "total_rows":len(self.df),
                "total_columns":len(self.df.columns),
                "columns": list(self.df.columns),
                "null_counts": self.df.isnull().sum().to_dict(),
                "data_types": self.df.dtypes.astype(str).to_dict()
            }

            os.makedirs("data/processed", exist_ok=True)

            report_path = "data/processed/schema_report.json"

            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(schema_report,f, indent=4)
            
            logger.info(f'Schema report saved to {report_path}')
            return schema_report
        
        except Exception as e:
            logger.error(f'Failed to generate schema report: {e}')
            raise
