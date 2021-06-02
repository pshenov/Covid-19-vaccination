import pandas as pd
from download_data import df_data, df_locations

# Increasing the maximum value for displaying the dataframe
pd.set_option('display.max_columns', 500)

# Grouping the dataset and deleting the wrong value.
df_covid_vaccinations = \
    df_data[['location', 'total_vaccinations', 'new_vaccinations']].groupby('location').count().reset_index()
df_covid_vaccinations.drop([226], inplace=True)


df_locations = df_locations[['location', 'vaccines', 'last_observation_date']]

# Merging two datasets
full_data = df_covid_vaccinations.merge(df_locations)

