import scrapy


class PopulationSpider(scrapy.Spider):
    name = 'population'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_cities_in_Mexico']

    def parse(self, response):
        population_table = response.xpath('//*[@id="mw-content-text"]/div[1]/table[2]//tr')
        city_pop = []
        headers = population_table[0]
        header = headers.xpath('th//text()')
        header_list = []
        for index, item in enumerate(header):
            if index in [4, 7]:
                continue
            header_list.append(item.extract())
            
        for row in population_table[1:]:
            table_data =[]
            columns = row.xpath('td//text()')
            for index, item in enumerate(columns):
                if index in [4, 7]:
                    continue
                table_data.append(item.extract())
            zip_data = dict(zip(header_list, table_data))
            city_pop.append(zip_data)
            yield zip_data
        
            
            
            
            #population_table.xpath('td//text()').extract_first()
            
        
            
            
        
