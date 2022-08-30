from datetime import datetime

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from src.db import save_data
from src.main import run

default_args= {
    'owner': 'Alefe Almeida',
    'email_on_failure': False,
    'email': ['alefeofdealmeida@gmail.com'],
    'start_date': datetime(2022, 8, 1)
}

with DAG(
    "scrapy_book",
    description='End-to-end Web Scraping',
    schedule_interval='@daily',
    default_args=default_args, 
    catchup=False) as dag:

    # task: 1
    creating_book_table = PostgresOperator(
        task_id="creating_book_table",
        postgres_conn_id='postgres_default',
        sql='sql/create_table.sql'
    )

    # task: 2
    web_scraping = PythonOperator(
        task_id='web_scraping',
        python_callable=run
    )

    # task: 3
    save_data = PythonOperator(
        task_id='save_data',
        python_callable=save_data
    )

    creating_book_table >> web_scraping >> save_data