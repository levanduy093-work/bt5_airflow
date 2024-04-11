

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'duy',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

def greet(ti):
    name = ti.xcom_pull(key='name', task_ids='get_name')
    age = ti.xcom_pull(key='age', task_ids='get_age')
    address = ti.xcom_pull(key='address', task_ids='get_address')
    print(f"Hello everyone! My name is {name}, and I am {age} years old, I'm living in {address}. Nice to meet you!")

def get_name(ti):
    ti.xcom_push(key='name', value='Duy')
    ti.xcom_push(key='age', value=25)
    ti.xcom_push(key='address', value='Go Vap, Ho Chi Minh City')

with DAG (
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v06',
    description='This is our first DAG in Airflow using PythonOperator',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
) as dag:
    task1 = PythonOperator (
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name': 'Duy', 'age': 25, 'address': 'Go Vap, Ho Chi Minh City'}
    )

    task2 = PythonOperator (
        task_id='get_name',
        python_callable=get_name
    )

    task3 = PythonOperator (
        task_id='get_age',
        python_callable=get_name
    )

    task4 = PythonOperator (
        task_id='get_address',
        python_callable=get_name
    )

    [task2, task3, task4] >> task1
    


