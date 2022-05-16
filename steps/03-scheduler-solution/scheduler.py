from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator

with DAG(
        'scheduler',
        default_args={
            'depends_on_past': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=10),
        },
        description='scheduler-example',
        schedule_interval=timedelta(minutes=1),
        start_date=datetime(2022, 6, 6),
        catchup=True,
        tags=['example'],
) as dag:
    t1 = BashOperator(
        task_id='print_date',
        bash_command='echo "{{ ds }}"',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t1 >> t2
