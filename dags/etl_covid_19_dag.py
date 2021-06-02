import datetime as dt
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from download_data import df_data, df_locations
from transform_data_with_pandas import full_data
from private import database


default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2021, 5, 1),
}

@dag(
    default_args=default_args,
    schedule_interval='@daily',
    dag_id='etl_covid_19_dag'
)
def etl_pipeline():
    @task
    def download_data():
        URL_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
        URL_LOCATIONS_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv'
        df_data = pd.read_csv(URL_CSV)
        df_locations = pd.read_csv(URL_LOCATIONS_CSV)
        return df_data, df_locations


    @task
    def transform_data(df_data, df_locations):
        df_covid_vaccinations = \
            df_data[['location', 'total_vaccinations', 'new_vaccinations']].groupby('location').count().reset_index()
        df_covid_vaccinations.drop([226], inplace=True)
        df_locations = df_locations[['location', 'vaccines', 'last_observation_date']]
        full_data = df_covid_vaccinations.merge(df_locations)
        return full_data

    @task
    def insert_data_in_database(full_data):
        engine = sqlalchemy.create_engine(database)
        conn = engine.connect()
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            full_data.to_sql('covid_19_data', engine, index=False, if_exists='append')
        except:
            raise

    download_data() >> transform_data() >> insert_data_in_database()

main_dag = etl_pipeline()



