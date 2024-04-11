
from airflow.decorators import task, dag
from datetime import datetime, timedelta

default_args = {
    'owner': 'duy',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

@dag (
    dag_id='dag_with_taskflow_v04',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
)

def hello_world():
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Duy',
            'last_name': 'Le'
        }
    
    @task()
    def get_age():
        return 20
    
    @task()
    def get_address():
        return 'Go Vap, Ho Chi Minh City'
    
    @task()
    def greet(first_name, last_name, age, address):
        print(f"Hello everyone! My name is {first_name} {last_name}, and I am {age} years old, I'm living in {address}. Nice to meet you!")

    name_dict = get_name()
    age = get_age()
    address = get_address()

    greet(first_name=name_dict['first_name'],
        last_name=name_dict['last_name'],
        age=age,
        address=address)


greet_dag = hello_world()



