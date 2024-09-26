# Data Engineering - Breweries Case

<<<<<<< HEAD
## Project Description
=======
## Descrição do Projeto

Este projeto de engenharia de dados consome dados da API [Open Brewery DB](https://api.openbrewerydb.org/breweries), transforma e persiste os dados em um Data Lake seguindo a **Arquitetura Medallion** com três camadas:

- **Bronze**: Dados brutos extraídos da API.
- **Silver**: Dados transformados, armazenados em formato Parquet.
- **Gold**: Dados agregados (contagem de cervejarias por tipo e estado) armazenados em CSV.

O projeto utiliza **Airflow** para orquestração, **Pandas** para transformação de dados e **Docker** para containerização. O pipeline é agendado para execução diária.

---

## Requisitos

Antes de iniciar, certifique-se de ter instalado:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
>>>>>>> 2d8b2e0b241f33d45d772607a7383b66f6415ff5

This data engineering project consumes data from the [Open Brewery DB](https://api.openbrewerydb.org/breweries) API, transforms it, and persists the data in a Data Lake following the **Medallion Architecture** with three layers:

<<<<<<< HEAD
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
=======
1. Clone o repositório:
   git clone https://github.com/jonathanwitkosky/data-engineering-breweries-case.git

>>>>>>> 2d8b2e0b241f33d45d772607a7383b66f6415ff5
   cd data-engineering-breweries-case
   ```

<<<<<<< HEAD
2. Build and start the containers:
   ```bash
   docker-compose up --build -d
   ```

3. Access the Airflow interface:

   URL: http://localhost:8080
=======
2. Build e Start dos Containers

   docker-compose up --build -d

3. Acesse a interface do Airflow:

   URL: http://localhost:8080

   Usuário: airflow

   Senha: airflow
>>>>>>> 2d8b2e0b241f33d45d772607a7383b66f6415ff5

   Username: airflow

<<<<<<< HEAD
   Password: airflow

4. Start the `brewery_pipeline` DAG to run the ETL pipeline.

5. The output files will be inside the `/opt/airflow/dags` folder for analysis.

6. How to stop the container:
   ```bash
   docker-compose down
   ```
=======
5. Os arquivos vão estar dentro da pasta /opt/airflow/dags para análise.

6. Como parar o Container:
   
   docker-compose down
>>>>>>> 2d8b2e0b241f33d45d772607a7383b66f6415ff5
