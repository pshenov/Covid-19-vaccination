import sqlalchemy
from sqlalchemy.orm import sessionmaker
from private import database
from transform_data_with_pandas import full_data

# Create a connection to the database and use the pandas method to write the data to the database
engine = sqlalchemy.create_engine(database)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

try:
    full_data.to_sql('covid_19_data', engine, index=False, if_exists='append')
except:
    raise