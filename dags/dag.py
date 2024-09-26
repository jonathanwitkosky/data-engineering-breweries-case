# Imports
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import requests 
import json
import pandas as pd

# Argumentos
default_args ={
    'owner': 'Jonathan',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email':['jonathanwitkosky@gmail.com'],
    'email_on_failure':True,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

def extract_data():
    # URL da API
    url = 'https://api.openbrewerydb.org/breweries'
    response = requests.get(url)
    breweries = response.json()
      
    # Salvando o arquivo JSON na pasta bronze
    with open('/opt/airflow/dags/breweries_raw.json', 'w') as f:
        json.dump(breweries, f)

def transform_data():
    with open('/opt/airflow/dags/breweries_raw.json') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df.to_parquet('/opt/airflow/dags/breweries.parquet', partition_cols=['state'])

def load_data():
    df = pd.read_parquet('/opt/airflow/dags/breweries.parquet')
    df_agrouped = df.groupby(['brewery_type', 'state'], observed=True).size().reset_index(name='brewery_count')
    df_agrouped_filtered = df_agrouped.query('brewery_count >= 1')
    # Salva o DataFrame final em um arquivo CSV
    df_agrouped_filtered.to_csv('/opt/airflow/dags/brewery.csv', index=False)

with DAG('brewery_pipeline',
         default_args=default_args,
         schedule_interval='@once',
         catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    extract_task >> transform_task >> load_task