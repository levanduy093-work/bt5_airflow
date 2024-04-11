from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'duy',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    default_args=default_args,
    dag_id='dag_with_cron_expression_v02',
    start_date=datetime(2023, 1, 1),
    schedule_interval='0 7 * * Mon',
) as dag:
    task1 = BashOperator (
        task_id='first_task',
        bash_command='echo "Hello everyone! This is the test for cron expression"'
    )

    task1



