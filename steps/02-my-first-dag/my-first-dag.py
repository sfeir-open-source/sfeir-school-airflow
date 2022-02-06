from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='hello_sfeir_school',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['sfeir_school'],
) as dag:

    def echo_hello():
      print('Hello Sfeir School !')

    echo = PythonOperator(
      task_id="hello_sfeir",
      python_callable=echo_hello
    )

    # TODO: ecrire une tâche qui demande "comment vas tu ?"

    echo
