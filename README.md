# Data Engineering - Breweries Case

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

6. Como parar o Container:
   
   docker-compose down
