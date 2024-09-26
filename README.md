# Data Engineering - Breweries Case

## Project Description

This data engineering project consumes data from the [Open Brewery DB](https://api.openbrewerydb.org/breweries) API, transforms it, and persists the data in a Data Lake following the **Medallion Architecture** with three layers:

- **Bronze**: Raw data extracted from the API.
- **Silver**: Transformed data, stored in Parquet format.
- **Gold**: Aggregated data (count of breweries by type and state) stored in CSV format.

The project uses **Airflow** for orchestration, **Pandas** for data transformation, and **Docker** for containerization. The pipeline is scheduled to run daily.

---

## Requirements

Before starting, make sure you have installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to run

1. Clone the repository:
   ```bash
   git clone https://github.com/jonathanwitkosky/data-engineering-breweries-case.git
   cd data-engineering-breweries-case
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build -d
   ```

3. Access the Airflow interface:

   URL: http://localhost:8080

   Username: airflow

   Password: airflow

4. Start the `brewery_pipeline` DAG to run the ETL pipeline.

5. The output files will be inside the `/opt/airflow/dags` folder for analysis.

6. How to stop the container:
   ```bash
   docker-compose down
   ```