import requests
import json
import os
from datetime import datetime
from app.utils.logger import get_logger

logger = get_logger(__name__)

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_data(self) -> list:
        try:
            logger.info("Starting API request...")
            
            headers = {
            "User-Agent": "data-engineering-pipeline/1.0",
            "Accept": "application/json"
            }

            params = {
            "fields": "name,capital,region,population"
            }

            response = requests.get(
            self.base_url,
            headers=headers,
            params=params,
            timeout=10
            )

            response.raise_for_status()  # Raises HTTPError for bad status

            logger.info("API request successful.")
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise

        except requests.exceptions.RequestException as err:
            logger.error(f"Request error occurred: {err}")
            raise

    def save_raw_data(self, data: list):
        try:
            os.makedirs("data/raw", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = f"data/raw/countries_raw_{timestamp}.json"

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            logger.info(f"Raw data saved at {file_path}")

        except Exception as e:
            logger.error(f"Failed to save raw data: {e}")
            raise