from app.processing.etl_pipeline import ETLPipeline
from app.processing.elt_pipeline import ELTPipeline
from app.utils.config import settings

def main():
    etl = ETLPipeline(settings.API_URL)
    etl.run()
    elt = ELTPipeline(settings.API_URL)
    elt.run()


if __name__ == "__main__":
    main()
