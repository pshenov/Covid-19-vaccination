import pandas as pd


URL_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
URL_LOCATIONS_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv'

# Download dataframes with general data on Covid-19 and vaccination data
df_data = pd.read_csv(URL_CSV)
df_locations = pd.read_csv(URL_LOCATIONS_CSV)
