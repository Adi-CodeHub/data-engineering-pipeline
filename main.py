from app.processing.etl_pipeline import ETLPipeline
from app.processing.elt_pipeline import ELTPipeline

def main():
    url = "https://restcountries.com/v3.1/all"
    etl = ETLPipeline(url)
    elt = ELTPipeline(url)
    etl.run()
    elt.run()


if __name__ == "__main__":
    main()
