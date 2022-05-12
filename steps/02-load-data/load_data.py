from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
        dag_id='load_review_data',
        description='Create table and load data into it',
        start_date=datetime(2021, 1, 1),
        schedule_interval="@once",
        catchup=False
) as dag:
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id="postgres_instance",
        sql="""
            CREATE TABLE order_reviews (
                "index" INTEGER  NOT NULL PRIMARY KEY,
                review_id VARCHAR(32) NOT NULL,
                order_id VARCHAR(32) NOT NULL,
                review_score INTEGER  NOT NULL,
                review_comment_title VARCHAR(128),
                review_comment_message VARCHAR(512) NOT NULL,
                review_creation_date TIMESTAMP NOT NULL,
                review_answer_timestamp TIMESTAMP NOT NULL,
                year INTEGER  NOT NULL,
                month INTEGER  NOT NULL
            );
        """
    )

    load_data_in_orders_reviews = PostgresOperator(
        task_id='load_order_reviews',
        postgres_conn_id="postgres_instance",
        sql="sql/order_reviews_{}.sql",
    )

    fetch_2016_reviews = PostgresOperator(
        task_id='fetch_2016_reviews',
        postgres_conn_id="postgres_instance",
        sql="""
            SELECT count(*) FROM order_reviews;
        """
    )

    create_table >> load_data_in_orders_reviews >> fetch_2016_reviews
