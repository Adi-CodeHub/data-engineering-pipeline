import pandas as pd
from app.utils.logger import get_logger

logger = get_logger(__name__)

class DataTransformer:
    def __init__(self, df:pd.DataFrame):
        self.df = df

    def add_population_density(self):
        self.df["population_density"] = self.df["population"] / self.df["area"]

        logger.info("Population density calculated")
        return self.df
    
    def region_statistics(self):
        region_df = self.df.groupby("region").agg(
            total_population = ("population","sum"),
            avg_population = ("population", "mean"),
            country_count = ("country", "count")
        ).reset_index()

        logger.info("Region statistics created")
        return region_df
    
    def language_table(self):
        lang_df = self.df[["country","languages"]].dropna()
        lang_df["languages"] = lang_df["languages"].str.split(", ")
        lang_df = lang_df.explode('languages')

        logger.info("Language table created")
        return lang_df
    
    def currency_table(self):
        cur_df = self.df[["country","currencies"]].dropna()
        cur_df['currencies'] = cur_df["currencies"].str.split(", ")
        cur_df = cur_df.explode('currencies')

        logger.info("Currency table created")
        return cur_df
    
    def transform(self):
        self.add_population_density()
        region_df = self.region_statistics()
        language_df = self.language_table()
        currency_df = self.currency_table()

        logger.info("All transformation completed")
        return self.df, region_df, language_df, currency_df
