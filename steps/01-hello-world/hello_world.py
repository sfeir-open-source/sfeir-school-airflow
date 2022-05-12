from airflow import DAG # IMPORTANT

# from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

with DAG(
        'hello_world',
        description='A simple Hello World',
        start_date=datetime(2021, 1, 1),
        catchup=False,
) as dag:
    t1 = BashOperator( # changer en pythonoperator
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t3 = BashOperator( # bloc à écrire au choix avec un python ou un bash
        task_id='hello',
        depends_on_past=False,
        bash_command='echo "hello_world"',
    )

    t1 >> t2 >> t3
