import requests


URL_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
URL_LOCATIONS_CSV = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv'


r_data = requests.get(URL_CSV)
with open('data/covid-19.csv', 'w', encoding='utf8') as covid_file:
    covid_file.write(r_data.text)


r_locations = requests.get(URL_LOCATIONS_CSV)
with open('data/vaccinations_locations.csv', 'w', encoding='utf8') as vaccinations_file:
    vaccinations_file.write(r_locations.text)