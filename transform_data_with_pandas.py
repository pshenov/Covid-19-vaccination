import pandas as pd


pd.set_option('display.max_columns', 500)

df_covid = pd.read_csv('data/covid-19.csv')

df_covid_vaccinations = \
    df_covid[['location', 'total_vaccinations', 'new_vaccinations']].groupby('location').count().reset_index()
df_covid_vaccinations.drop([215], inplace=True)

df_vaccinations_locations = pd.read_csv('data/vaccinations_locations.csv')
df_vaccinations_locations = df_vaccinations_locations[['location', 'vaccines', 'last_observation_date']]

full_data = df_covid_vaccinations.merge(df_vaccinations_locations)
full_data.to_csv('data/full_data_vaccinations.csv')