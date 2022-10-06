
# Simple Scrapy Exercise

Follow the instructions below to create and run your first scrapy project

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

### Working with Scrapy
----------
### Install scrapy

~~~
pip install scrapy
~~~

With successful installation of the framework, we can now move towards creating our first project

**Create a new project**

Go to your working directory, and use the following command
~~~
scrapy startproject <Name of project>
~~~
<img width="207" alt="spiderdocs" src="https://user-images.githubusercontent.com/97254770/194343025-23968f82-177a-44b9-9883-e53de24a7d07.png">

On successful creation of the project, a new folder with all the necessary files will be created in a new folder

**veryfing website response**

Before moving on to working with spiders, we first need to check if the website we want to use is active

Access the Scrapy shell
~~~
scrapy shell
~~~

Using the 'fetch' command inside the shell, we will verify if the website is active, as well as downloading objects, it will be stored automatically on the 'response' variable

~~~
fetch('https://en.wikipedia.org/wiki/List_of_cities_in_Mexico')
~~~

you should see the following output if the attempt was successful, it means the website is working

~~~
[scrapy.core.engine] DEBUG: Crawled (200) <GET https://en.wikipedia.org/wiki/List_of_dog_breeds> (referer: None)
~~~

you can check the response variable on your shell

~~~
>>> response
<200 https://en.wikipedia.org/wiki/List_of_cities_in_Mexico>
>>> 
~~~

You can use the 'view' command to open the downloaded page on your browser, it will show you what you 'spider' would be looking at.

~~~
view(response)
~~~

**NOTE:** You can use this command to open and inspect the page for elements you would like to use with scrapy, take your time inspecting the page and elements for further practice

**Using selectors**

For this exercise, we are going to use selectors, upon further inspection of the page, we want to extract the information on cities in Mexico by population. Due to the class we need to use an xpath selector

**Creating your first 'spider'**

Change directory to your scrapy project folder, and under the **spiders** folder create a new file with your desired spider name

~~~
scrapy genspider <spider name> <allowed domain>
~~~

~~~
scrapy crawl population -o output.csv
~~~
To run your spider and write the results to a file you can run the above command

