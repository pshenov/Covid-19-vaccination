import sqlalchemy
from sqlalchemy.orm import sessionmaker
from private import database
from transform_data_with_pandas import df_covid_vaccinations, df_vaccinations_locations


engine = sqlalchemy.create_engine(database)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

try:
    df_covid_vaccinations.to_sql('covid_19_data', engine, index=False, if_exists='append')
    df_vaccinations_locations.to_sql('covid_19_vaccinations', engine, index=False, if_exists='append')
except:
    raise