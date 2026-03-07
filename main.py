from app.processing.etl_pipeline import ETLPipeline

def main():
    url = "https://restcountries.com/v3.1/all"
    pipeline = ETLPipeline(url)
    pipeline.run()


if __name__ == "__main__":
    main()
