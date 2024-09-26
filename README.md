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
## Orchestration
The solution uses Apache Airflow to orchestrate the data pipeline, which includes data ingestion, transformation, and aggregation. Airflow allows:

1. Scheduling: Configuration of periodic execution of the DAG (Directed Acyclic Diagram).

2. Retries and Error Handling: If a task fails, Airflow tries to execute the task again and sends a email in case of error.

3. Monitoring: The Airflow interface is used to monitor the status of tasks and workflows.
   
## Design Choices and Trade-offs

1. Orchestration: Apache Airflow
Why it was chosen: Airflow is widely used in the market and offers a robust interface for creating and monitoring data pipelines. Furthermore, it allows easy scalability and integration with various services and tools.
Trade-off: Airflow may have a higher overhead in terms of resources, especially if run locally. However, the flexibility and scheduling power make up for this disadvantage.

2. Local Data Lake vs. Cloud (AWS S3)
Current choice: To simplify implementation and not involve cloud services, data is stored locally.
Trade-off: Storing data locally limits the scalability and availability of the solution. In real production, it would be preferable to use a cloud storage service like Amazon S3, which offers greater reliability and integrates well with tools like Spark and Airflow.

3. Transformations in Python
Why it was chosen: Python is a familiar language for manipulating data, and its integration with Airflow is straight, making the pipeline construction easier.
Trade-off: Although Python is flexible, for large volumes of data, using distributed frameworks like Spark could improve performance. However, for this use case, Python was sufficient for the necessary transformations.
