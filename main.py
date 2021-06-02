import requests
import pandas as pd


URL_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
URL_LOCATIONS_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv'


df_data = pd.read_csv(URL_CSV)

pd.set_option('display.max_columns', 500)

df_covid_vaccinations = \
    df_data[['location', 'total_vaccinations', 'new_vaccinations']].groupby('location').count().reset_index()
df_covid_vaccinations.drop([215], inplace=True)


df_locations = pd.read_csv(URL_LOCATIONS_CSV)

df_vaccinations_locations = df_locations[['location', 'vaccines', 'last_observation_date']]


full_data = df_covid_vaccinations.merge(df_vaccinations_locations)
print(full_data)
full_data.to_csv('data/full_data_vaccinations.csv')
