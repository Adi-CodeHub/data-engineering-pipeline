from app.utils.logger import get_logger
import pandas as pd

logger = get_logger(__name__)

class DataCleaner:

    def __init__(self, df:pd.DataFrame):
        self.df = df

    def select_columns(self):
        columns_needed = [
            "name.common",
            "region",
            "subregion",
            "population",
            "area",
            "capital",
            "currencies",
            "languages",
            "timezones",
            "independent"
        ]

        # logger.info(f"Available columns: {self.df.columns.tolist()}")
        self.df = self.df.reindex(columns=columns_needed)

        logger.info("selected relevant columns")
        return self.df
    

    def rename_columns(self):
        self.df = self.df.rename(columns={
            "name.common": "country",
            "region": "region",
            "subregion": "subregion",
            "population": "population",
            "area": "area",
            "capital": "capital",
            "currencies": "currencies",
            "languages": "languages",
            "timezones": "timezones",
            "independent": "is_independent"
        })

        logger.info('Columns Renamed')
        return self.df
    
    def handle_missing_values(self):
        self.df["capital"]=self.df['capital'].apply(
            lambda x:x[0] if isinstance(x, list) and len(x) > 0 else x if isinstance(x, str) else None
            )
        
        self.df["subregion"]= self.df["subregion"].fillna("unknown")
        self.df["population"]=self.df["population"].fillna(0)
        
        logger.info("Handled missing values")
        return self.df
    
    def normalize_nested_field(self):

        def extract_currency(currencies):
            if isinstance(currencies, dict):
                return ', '.join([v["name"] for v in currencies.values()])
            return None
        
        def extract_language(languages):
            if isinstance(languages, dict):
                return ", ".join(str(v) for v in languages.values())
            return None
        
        self.df["currencies"]=self.df['currencies'].apply(extract_currency)
        self.df["languages"]=self.df['languages'].apply(extract_language)

        logger.info("Nested field normalized")
        return self.df
    
    def clean(self):
        self.select_columns()
        self.rename_columns()
        self.handle_missing_values()
        self.normalize_nested_field()
        logger.info(f"Clean dataset shape: {self.df.shape}")
        logger.info("Data cleaning completed")
        return self.df

