import glob
import os
from app.ingestion.api_client import APIClient
from app.processing.validator import DataValidator

def run_ingestion():
    url = "https://restcountries.com/v3.1/all"
    client = APIClient(url)

    data = client.fetch_data()
    client.save_raw_data(data)

def run_validation():
    latest_file = max(glob.glob("data/raw/*.json"), key=os.path.getctime)
    validator = DataValidator(latest_file)
    validator.load_raw_data()
    validator.convert_to_dataframe()
    validator.generate_schema_report()

if __name__ == "__main__":
    # run_ingestion()
    # run_validation()
    pass