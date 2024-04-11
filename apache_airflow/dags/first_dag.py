


from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'duy',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id='first_dag_v3',
    default_args=default_args,
    description='This is my first DAG in Airflow for testing',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
) as dag:
    task_1 = BashOperator (
        task_id='first_task',
        bash_command='echo "Hello everyone! This is my first DAG in Airflow"'
    )

    task_2 = BashOperator (
        task_id='second_task',
        bash_command='echo "This seems like my task 1 is working fine"'
    )

    task_3 = BashOperator (
        task_id='third_task',
        bash_command='echo "This seems like my task 2 is working fine"'
    )

    task_1.set_downstream(task_2)
    task_1.set_downstream(task_3)

