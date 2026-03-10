# End-to-End Data Engineering Pipeline

A production-style data pipeline that ingests data from an API, performs validation and transformations, and loads structured datasets into SQLite. The project demonstrates both ETL and ELT architectures.

---

## Features

- **API Data Ingestion** — Fetches data from external REST APIs
- **Raw Data Storage** — Persists unprocessed data before transformation
- **Schema Validation** — Enforces data contracts on incoming records
- **Data Cleaning** — Handles nulls, type coercion, and anomalies
- **Advanced Transformations** — Produces analytics-ready datasets via Pandas
- **Relational Data Modeling** — Normalized table design in SQLite
- **ETL Pipeline** — Transform-before-load architecture
- **ELT Pipeline** — Transform-inside-database architecture
- **Logging & Config Management** — Structured logging with environment-based configuration

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data transformation |
| SQLite | Data warehouse |
| Requests | API ingestion |
| python-dotenv | Config management |

---

## Architecture

```
         ┌─────────────┐
         │     API      │
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │ Data Ingestion│
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │  Raw Storage  │
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │  Validation   │
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │   Cleaning    │
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │Transformation │
         └──────┬───────┘
                │
         ┌──────▼───────┐
         │   SQLite DB   │
         └─────────────┘
```

Two pipeline patterns are implemented:

- **ETL** — Data is transformed in Python/Pandas before being loaded into the database
- **ELT** — Raw data is loaded first, then transformed using SQL inside the database

---

## Project Structure

```
data-engineering-pipeline/
│
├── app/
│   ├── ingestion/
│   │   └── api_client.py        # Fetches data from REST API
│   │
│   ├── processing/
│   │   ├── validator.py         # Schema validation logic
│   │   ├── cleaner.py           # Null handling, type coercion
│   │   └── transformer.py       # Feature engineering, normalization
│   │
│   ├── storage/
│   │   └── database.py          # SQLite connection and write logic
│   │
│   ├── pipelines/
│   │   ├── etl_pipeline.py      # ETL orchestrator
│   │   └── elt_pipeline.py      # ELT orchestrator
│   │
│   └── utils/
│       ├── config.py            # Env-based config loader
│       └── logger.py            # Structured logging setup
│
├── data/                        # SQLite database output
├── logs/                        # Pipeline run logs
│
├── main.py                      # Entry point
├── requirements.txt
├── .env.example
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone <repo_url>
cd data-engineering-pipeline
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and update values as needed:

```bash
cp .env.example .env
```

```env
API_URL=https://restcountries.com/v3.1/all
DATABASE_PATH=data/database.db
LOG_LEVEL=INFO
```

### Run

```bash
python main.py
```

---

## Example SQL Queries

**Top populated regions:**
```sql
SELECT region, SUM(population) AS total_population
FROM countries
GROUP BY region
ORDER BY total_population DESC;
```

**Countries using a specific currency:**
```sql
SELECT country
FROM currencies
WHERE currency = 'Euro';
```

---

## Learning Outcomes

This project covers core data engineering competencies:

- REST API ingestion and JSON normalization
- Data validation and quality enforcement
- Transformation pipeline design with Pandas
- Relational data modeling and SQL storage
- ETL vs ELT architectural tradeoffs
- Modular, production-style project structure
- Logging and environment-based configuration

---

## Potential Enhancements

- [ ] Add pipeline scheduling with **Apache Airflow**
- [ ] Containerize with **Docker**
- [ ] Scale transformations using **Apache Spark**