
# Beautiful Soup Exercise

Follow the instructions below to create and run your first BeautifulSoup crawler

## Getting started
--------

### Create a virtual environment 

For virtual environment creation and python version management, pyenv is a good choice. 
You can find more information and installation guides on the following sites.

**NOTE :** It is not mandatory to use pyenv for this exercise, if you already have another virtual environment plugin, you can use that one instead.


**Pyenv** 

~~~
https://github.com/pyenv/pyenv
~~~

**pyenv-virtualenv**

~~~
https://github.com/pyenv/pyenv-virtualenv
~~~

**pyenv environment creation command**

~~~
pyenv virtualenv <python version> <env name>
~~~

### Working with BeautifulSoup
----------
### Install BeautifulSoup

~~~
pip install beautifulsoup4
~~~

**install 'requests'**

~~~
pip install requests
~~~

**install pandas**
to convert results to dataframe and have fun cleaning data

~~~
pip install pandas
~~~

We are going to extract data from  wikipedia page on Mexico's population by city, along with some more interesting statistics

**script structure**
~~~
from bs4 import BeautifulSoup
import pandas as pd
import requests
~~~
This will allow us to work on our data

~~~
response = requests.get(url = "https://en.wikipedia.org/wiki/List_of_cities_in_Mexico")
print(response.status_code)
~~~
This will allow us to test the connection to our desired target, the output from the above should return a status 200 code, that means the site is working!

Now, we need to **inspect** the elements from this particular page, we want to target the table with statistics on Mexico's population, so we should inspect that element to get the information we need to set up our crawler

With this we can execute the following bit of code:

~~~
soup = BeautifulSoup(response.text, 'html.parser')
cities_by_population = soup.find_all('table',{'class':"wikitable"})[1]
~~~
Since we have multiple objects that meet the criteria (wikitable), we need to specify that, in this case, we want to accss the second element that matches

~~~
cities_df=pd.read_html(str(cities_by_population))
cities_df=pd.DataFrame(cities_df[0])
cities_df.to_csv('Mexico_population.csv')
print(cities_df.head(2))
~~~
After running this, you will have a neatly arranged dataframe with the details from the table scrapped with BeautifulSoup, take a look at the data and you can clean it on the same script, to produce a better dataset to work with  after extracting the information!