"""Script to crawl wikipedia for dog breeds using BeautifulSoup"""
from bs4 import BeautifulSoup
import pandas as pd
import requests

url ="https://en.wikipedia.org/wiki/List_of_cities_in_Mexico"
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

page_title = soup.findAll("h1",{"class":"title"})