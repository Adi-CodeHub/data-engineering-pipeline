import glob
import os
from app.ingestion.api_client import APIClient
from app.processing.validator import DataValidator
from app.processing.cleaner import DataCleaner

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
    df = validator.df
    return df

def run_cleaning(df):
    cleaner = DataCleaner(df)
    clean_df = cleaner.clean()
    clean_df.to_csv("data/processed/clean_countries.csv", index=False)
    return clean_df


if __name__ == "__main__":
    # run_ingestion()
    # run_validation()
    df= run_validation()
    run_cleaning(df)