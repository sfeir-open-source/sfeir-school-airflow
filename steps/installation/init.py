import pandas as pd
from loguru import logger
import os
import sqlite3
from sqlalchemy import create_engine
from os import walk
import re

dataset_filenames_with_keys = {
    'olist_order_reviews_dataset': 'review_creation_date',
    'olist_orders_dataset': 'order_purchase_timestamp',
}


def split_file_by_year(df, key, filename):
    with logger.contextualize(task='split_file_by_year'):
        logger.debug('Add year and month column to dataframe {}', filename)
        # Transform the schema from string/object to datetime
        df[key] = pd.to_datetime(df[key])
        df['year'] = df[key].dt.year
        df['month'] = df[key].dt.month

        # Creat new file for each year
        for year in df[key].dt.year.unique():
            by_year_folder = f'./data/brazilian-ecommerce/by_year/{year}/'
            try:
                os.makedirs(by_year_folder, exist_ok=True)
            except OSError as error:
                logger.error(f'Fail to create folder {by_year_folder}: {error}')
            df_by_year = df[df.year.eq(year)]
            logger.debug('Export {} to {}', filename, by_year_folder)
            df_by_year.to_csv(f'{by_year_folder}/{filename}.csv')

            for month in df[key].dt.month.unique():
                by_month_folder = f'./data/brazilian-ecommerce/by_month/{year}_{month:02d}/'
                df_by_month = df_by_year[df_by_year.month.eq(month)]
                if df_by_month.size > 0:
                    try:
                        os.makedirs(by_month_folder, exist_ok=True)
                    except OSError as error:
                        logger.error(f'Fail to create folder {by_month_folder}: {error}')
                    logger.debug('Export {} to {}', filename, by_month_folder)
                    df_by_month.to_csv(f'{by_month_folder}/{filename}.csv')


##########################
# Load data in dataframe #
##########################
RAW_DATA_PATH = 'data/brazilian-ecommerce/'
filenames = next(walk(RAW_DATA_PATH), (None, None, []))[2]  # [] if no file

logger.info('Create SQLite engine')
# Generating engine to make it possible to connect the query into the defined database.
engine = create_engine('sqlite:///Brazilian_ecommerce.sqlite', echo=False)

logger.info('Load data in dataframe and in SQLite ')
for filename in filenames:
    logger.info('Process {} file', filename)
    df = pd.read_csv(os.path.join(RAW_DATA_PATH, filename))
    dataset_name = os.path.splitext(filename)[0]
    key = dataset_filenames_with_keys.get(dataset_name)

    if key:
        split_file_by_year(df, key, dataset_name)

    m = re.search('olist_(.+?)_dataset', dataset_name)
    table_name = m.group(1) if m else filename
    logger.info('Import {} to {}', dataset_name, table_name)
    df.to_sql(name=table_name, con=engine, if_exists='replace')

#####################
# Dump data to file #
#####################
logger.info('Dump database')
con = engine.raw_connection()
os.makedirs('db', exist_ok=True)
with open('db/brazilian-ecommerce.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)
