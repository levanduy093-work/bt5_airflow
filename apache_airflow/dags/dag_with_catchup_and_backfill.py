from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'duy',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id='dag_with_catchup_and_backfill_v02',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    task1 = BashOperator (
        task_id='first_task',
        bash_command='echo "Hello everyone! This is the test for catchup"'
    )