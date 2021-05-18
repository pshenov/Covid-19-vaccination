import requests
import pandas as pd


URL_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
LOCATIONS_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv'


r = requests.get(URL_CSV)
with open('data/covid-19.csv', 'w', encoding='utf8') as covid_file:
    covid_file.write(r.text)

pd.set_option('display.max_columns', 500)

df_covid = pd.read_csv('data/covid-19.csv')

for column in df_covid.columns:
    if 'World' in column:
        df_covid.drop(columns=column, inplace=True)

df_covid_vaccinations = \
    df_covid[['location', 'total_vaccinations', 'new_vaccinations']].groupby('location').count().reset_index()
df_covid_vaccinations.drop([215], inplace=True)


r_locations = requests.get(LOCATIONS_CSV)
with open('data/vaccinations_locations.csv', 'w', encoding='utf8') as vaccinations_file:
    vaccinations_file.write(r_locations.text)

df_vaccinations_locations = pd.read_csv('data/vaccinations_locations.csv')
df_vaccinations_locations = df_vaccinations_locations[['location', 'vaccines', 'last_observation_date']]


full_data = df_covid_vaccinations.merge(df_vaccinations_locations)
print(full_data)
full_data.to_csv('data/full_data_vaccinations.csv')
