from airflow import DAG # IMPORTANT

from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def return_true():
  return True

def hello_world():
  print("Hello World")
  return

with DAG(
        'hello_world',
        description='A simple Hello World',
        start_date=datetime(2021, 1, 1),
        catchup=False,
) as dag:
    t1 = PythonOperator(
        task_id='true',
        python_callable=return_true
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t3 = BashOperator(
        task_id='hello',
        depends_on_past=False,
        bash_command='echo "hello_world"',
    )

    t4 = PythonOperator(
      task_id="print_hello_world",
      python_callable=hello_world
    )

    t1 >> t2 >> t3 >> t4
