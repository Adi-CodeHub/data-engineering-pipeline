# Data Engineering Pipeline

A production-grade data pipeline demonstrating both **ETL** (Extract-Transform-Load) and **ELT** (Extract-Load-Transform) approaches. This project ingests country data from a REST API, validates and transforms it, and stores it in SQLite with comprehensive logging and error handling.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Architecture](#architecture)
- [Data Flow](#data-flow)
- [Output](#output)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- **API Data Ingestion** - Fetches real-time data from REST Countries API
- **Dual Pipeline Approaches** - Implements both ETL and ELT methodologies
- **Data Validation** - Schema validation with detailed reports
- **Data Cleaning** - Automated data cleansing and standardization
- **Complex Transformations** - Normalization and denormalization of country data
- **SQLite Storage** - Persistent data storage with structured schema
- **Comprehensive Logging** - Activity tracking and error reporting
- **Error Handling** - Robust exception handling throughout the pipeline

## 📁 Project Structure

```
data-engineering-pipeline/
├── app/
│   ├── ingestion/
│   │   └── api_client.py          # API communication and data fetching
│   ├── pipelines/
│   │   └── transformer.py         # Pipeline transformation logic
│   ├── processing/
│   │   ├── cleaner.py             # Data cleaning operations
│   │   ├── elt_pipeline.py        # Extract-Load-Transform pipeline
│   │   ├── etl_pipeline.py        # Extract-Transform-Load pipeline
│   │   ├── transformer.py         # Data transformation logic
│   │   └── validator.py           # Data validation and schema verification
│   ├── storage/
│   │   └── database.py            # Database operations and management
│   └── utils/
│       └── logger.py              # Logging configuration
├── data/
│   ├── raw/                       # Raw JSON files from API
│   └── processed/                 # Cleaned and transformed CSV files
├── logs/                          # Application logs
├── tests/                         # Test suite (if applicable)
├── main.py                        # Entry point for the pipeline
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone or Extract the Repository

```bash
cd data-engineering-pipeline
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

The pipeline uses environment variables for configuration. Create a `.env` file in the project root (optional):

```env
LOG_LEVEL=INFO
API_URL=https://restcountries.com/v3.1/all
DATABASE_PATH=data/database.db
```

## 💻 Usage

### Run Both Pipelines

Execute the main script to run both ETL and ELT pipelines:

```bash
python main.py
```

### Run Individual Pipelines

Create a separate script or modify `main.py`:

```python
from app.processing.etl_pipeline import ETLPipeline
from app.processing.elt_pipeline import ELTPipeline

# ETL Pipeline Only
etl = ETLPipeline("https://restcountries.com/v3.1/all")
etl.run()

# ELT Pipeline Only
elt = ELTPipeline("https://restcountries.com/v3.1/all")
elt.run()
```

## 🏗️ Architecture

### ETL Pipeline

```
Extract → Validate → Clean → Transform → Load
   ↓        ↓        ↓        ↓        ↓
  API   Schema   Raw Data  Normalize  CSV
       Report   Cleanup    Tables     Files
```

**Steps:**
1. **Extract** - Fetch data from REST Countries API
2. **Validate** - Check data integrity and generate schema reports
3. **Clean** - Remove duplicates, handle missing values, standardize formats
4. **Transform** - Normalize data into separate country, region, language, and currency tables
5. **Load** - Export processed data to CSV files

### ELT Pipeline

```
Extract → Load → Transform (SQL)
   ↓       ↓        ↓
  API   SQLite   Normalized
       Raw Table Tables
```

**Steps:**
1. **Extract** - Fetch data from REST Countries API
2. **Load** - Insert raw JSON data into SQLite raw_countries table
3. **Transform** - Use SQL queries to normalize and structure data in database

## 📊 Data Flow

### Input

- **Source:** REST Countries API (https://restcountries.com/v3.1/all)
- **Format:** JSON
- **Content:** Country information including names, codes, regions, languages, currencies

### Processing

- Data validation against expected schema
- Cleaning and standardization of fields
- Normalization into structured tables
- Deduplication and consistency checks

### Output

#### ETL Pipeline Output
Located in `data/processed/`:
- `countries.csv` - Cleaned country master data
- `regions.csv` - Unique regions
- `languages.csv` - Language mappings
- `currencies.csv` - Currency information
- `schema_report.json` - Data validation report

#### ELT Pipeline Output
Located in SQLite database (`data/database.db`):
- `raw_countries` - Raw JSON data
- `countries` - Processed country data
- `regions` - Region lookup table
- `languages` - Language lookup table
- `currencies` - Currency lookup table

## 📝 Logging

Application logs are stored in the `logs/` directory with timestamps. Log levels can be configured via the `logger.py` module.

**Log Locations:**
- `logs/` - Contains application execution logs

**Logged Information:**
- Pipeline execution steps
- Data validation results
- Transformation operations
- Error messages and exceptions

## 🔧 Troubleshooting

### Issue: API Connection Error
**Solution:** Verify internet connection and that REST Countries API is accessible:
```bash
curl https://restcountries.com/v3.1/all
```

### Issue: File Not Found Error
**Solution:** Ensure data directories exist and paths are correct:
```bash
mkdir -p data/raw data/processed logs
```

### Issue: Database Locked Error
**Solution:** Close any other connections to `data/database.db` and try again.

### Issue: Memory Error with Large Datasets
**Solution:** Process data in batches or increase available memory.

## 📚 Dependencies

Key dependencies (see `requirements.txt`):

- **requests** - HTTP library for API calls
- **pandas** - Data manipulation and analysis
- **python-dotenv** - Environment variable management
- **sqlite3** - Data storage (included with Python)

## 🔄 ETL vs ELT Comparison

| Aspect | ETL | ELT |
|--------|-----|-----|
| **Order** | Transform then Load | Load then Transform |
| **Performance** | Slower (all data processed before load) | Faster (load raw data first) |
| **Flexibility** | Less flexible (transformation rules fixed) | More flexible (transform using database) |
| **Best For** | Smaller datasets, fixed schemas | Large datasets, evolving requirements |
| **Storage** | Files (CSV) | Database (SQLite) |

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 👤 Author

Created as a portfolio project demonstrating data engineering best practices.

---

**Last Updated:** March 2026