FROM apache/airflow:2.8.0

# Instalar bibliotecas adicionais necessárias
USER root
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# Instalar pacotes Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar DAGs e scripts
COPY ./dags /opt/airflow/dags
