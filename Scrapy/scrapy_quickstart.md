
# Simple Scrapy Exercise

Follow the instructions below to create and run your first scrapy project. We are going to use a dedicated page for beginner and advanced web scrapers alike: https://toscrape.com/ Remember to practice ethically and always follow robots.txt rules

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
fetch('http://books.toscrape.com/')
~~~

you should see the following output if the attempt was successful, it means the website is working

~~~
[scrapy.core.engine] DEBUG: Crawled (200) <GET http://books.toscrape.com/> (referer: None)
~~~

you can check the response variable on your shell

~~~
>>> response
<200 http://books.toscrape.com/>
>>> 
~~~

You can use the 'view' command to open the downloaded page on your browser, it will show you what you 'spider' would be looking at.

~~~
view(response)
~~~

![page](https://user-images.githubusercontent.com/97254770/194413180-1f81d07e-dfc2-4cdc-9f87-1e4cc462ea48.png)


**NOTE:** You can use this command to open and inspect the page for elements you would like to use with scrapy, take your time inspecting the page and elements for further practice

**Using selectors**

For this exercise, we are going to use selectors, upon further inspection of the page, we want to extract the information on a sandbox bookstore. Take some time to open and inspect the elements of interest to determine how are we going to build the scraper 
![books](https://user-images.githubusercontent.com/97254770/194354037-acd38dc7-9dd0-4b33-b874-188a8736006e.png)

Once we identify what we want to extract, we can use selectors to extract directly or simply test if we are on the right track
~~~
>>> response.css('title::text')
[<Selector xpath='descendant-or-self::title/text()' data='\n    All products | Books to Scrape -...'>]
~~~

We can extract the data from the above with the following method
~~~
>>> response.css('title::text').extract()
['\n    All products | Books to Scrape - Sandbox\n']
~~~
We can further clean the otput by removing newlines, spaces or unwanted characters, this step can be done from the shell, on the spider script, or after extracting the data, with some exploration and cleaning. 

![interest](https://user-images.githubusercontent.com/97254770/194364631-3ca98390-770a-41a9-9a89-b650c26bcb55.png)


Inspect carefully the element, in this case the book listing, to identify what sort of data would be relevant to have to keep a database of books from best to worst rated, or sorted by price. After identifying what you want to extract, we can move on to test on the scrapy shell if you want, or directly to the spider code!

**Creating your first 'spider'**

Change directory to your scrapy project folder, and under the **spiders** folder create a new file with your desired spider name

~~~
scrapy genspider <spider name> <allowed domain>
~~~
take a look at the default spider generated in your repository, here you will input the necessary code to parse the web content and be able to write it to a file. 

Using selectors in the shell and then writing to the script is recommended, as you will have a clear idea of what to expect. 

**For Example:**
the css selector is a good choice, and we also have the xpath selector to locate elements in xml docs. More information on the types and how to construct them can be found here:

~~~
https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors
~~~
Using the Xpath selector, lets say that you want to get the book titles in the page
~~~
>>> response.xpath('//h3/a/text()').extract()
['A Light in the ...', 'Tipping the Velvet', 'Soumission', 'Sharp Objects', 'Sapiens: A Brief History ...', 'The Requiem Red', 'The Dirty Little Secrets ...', 'The Coming Woman: A ...', 'The Boys in the ...', 'The Black Maria', 'Starving Hearts (Triangular Trade ...', "Shakespeare's Sonnets", 'Set Me Free', "Scott Pilgrim's Precious Little ...", 'Rip it Up and ...', 'Our Band Could Be ...', 'Olio', 'Mesaerion: The Best Science ...', 'Libertarianism for Beginners', "It's Only the Himalayas"]
~~~
You can assign this selector to a variable to reference it down the line

~~~
titles = response.xpath('//h3/a/text()').extract()
~~~
Try doing this for every element you would like to extract for your data, and check the output on the shell, if it is what you expected, you can use that specific xpath to construct your items later on. 

**Additional step**
For the sake of simplicity, we will not delve too deep into Scrapy's capabilities. I recommend reading the official documentation to expand on your web crawler and adjust it. 

~~~
https://docs.scrapy.org/en/latest/
~~~
On this exercise we can make use of **item containers** this feature makes it easier to manipulate data and store it in a convenient way for later use or writing to a file, to make use of item containers, simply navigate to the items.py folder scrapy created for the project.

<img width="314" alt="items" src="https://user-images.githubusercontent.com/97254770/194413849-db9250c5-ff12-4cba-a677-ade8a9eacd80.png">


The name of the container must match the name for you variables for it to properly work.

We can then import the module onto your spider to take advantage of its capabilities, as you can also introduce specific data transformation functions for your variables.

<img width="665" alt="item_spider" src="https://user-images.githubusercontent.com/97254770/194413922-0f069929-b461-4fd6-972c-2b28cf89b4fb.png">

~~~
scrapy crawl <spider name> -o output.json
~~~
To run your spider and write the results to a file you can run the above command

## Adding Pagination
----------------
If you scroll to the bottom of the page, you will see we have 50 pages, by inspecting the 'next' button we get the following, and we can access this by specifying the xml attribute


~~~
response.css('.next a').attrib['href']
~~~

this will yield the current page, and we can use this to set up our spider in a way that it can jump from the current page to the next until the last one is reached

~~~
jump_page = response.css('.next a').attrib['href']
        if jump_page is not None:
            yield response.follow(jump_page, callback = self.parse)
~~~
When you run your spider with the above, you will see that it goes through all 50 pages before exiting and saving the results!