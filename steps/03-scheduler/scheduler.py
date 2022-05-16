from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator

with DAG(
        'scheduler',
        default_args={
            'depends_on_past': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        description='scheduler-example',
        schedule_interval="* * * * *",
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=['example'],
) as dag:

  # TODO : écrire un dag qui se lance toutes les minutes

  # TODO 2 : ce même dag doit afficher la date du jour

  # TODO 3 : il faut maintenant que ce dag rattrappe les 6 derniers jours

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t1 >> t2
