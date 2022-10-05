from bs4 import BeautifulSoup
import pandas as pd
import requests

population_url = "https://en.wikipedia.org/wiki/List_of_cities_in_Mexico"
target_class = "wikitable sortable jquery-tablesorter"

response = requests.get(url = "https://en.wikipedia.org/wiki/List_of_cities_in_Mexico")
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
cities_by_population = soup.find_all('table',{'class':"wikitable"})[1]

cities_df=pd.read_html(str(cities_by_population))

cities_df=pd.DataFrame(cities_df[0])
print(cities_df.head(2))

cities_df.to_csv('Mexico_population.csv')