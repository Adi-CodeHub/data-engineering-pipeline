from app.ingestion.api_client import APIClient

def run_ingestion():
    url = "https://restcountries.com/v3.1/all"
    client = APIClient(url)

    data = client.fetch_data()
    client.save_raw_data(data)

if __name__ == "__main__":
    run_ingestion()