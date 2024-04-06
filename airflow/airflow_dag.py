from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from data_ingestion.data_ingestion import retrive_key
from data_transformation.data_transformation import apply_transformation
from db_connection import connect_to_database, create_table, insert_data, close_connection

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_transform_load(**kwargs):
    api_key = '5782baf9-b3d1-4670-8c61-11dacda86b6d'
    conn = connect_to_database()
    crypto_data = retrive_key(api_key)
    if crypto_data:
        bitcoin_price = 66042.85516079019
        transformed_data = apply_transformation(crypto_data, bitcoin_price)
        create_table(conn)
        insert_data(conn, transformed_data)
        close_connection(conn)

dag = DAG(
    'crypto_pipeline',
    default_args=default_args,
    description='Pipeline to extract cryptocurrency data and store in SQLite database',
    schedule_interval='0 22 * * *',  # Run daily at 10:00 PM
)

extract_task = PythonOperator(
    task_id='extract_transform_load',
    python_callable=extract_transform_load,
    provide_context=True,
    dag=dag,
)

extract_task
