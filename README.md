# Data Engineering Breweries Case

## Pré-requisitos
- Docker
- Docker Compose

## Como rodar

1. Clone o repositório:
   git clone https://github.com/jonathanwitkosky/data-engineering-breweries-case.git

   cd data-engineering-breweries-case

2. Build e Start dos Containers

   docker-compose up --build -d

3. Acesse a interface do Airflow:

   URL: http://localhost:8080

   Usuário: airflow

   Senha: airflow

4. Inicie o DAG brewery_pipeline para executar o pipeline de ETL.

5. Os arquivos vão estar dentro da pasta /opt/airflow/dags para análise.
