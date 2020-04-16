import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.radiosdelperu.pe/'
        #'http://www.radiosdelperu.pe/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        #filex = open("")
        filename = 'scraper.txt'
        with open(filename, 'w') as f:
            print (response.css("a").extract())
            f.write(str(response.css("a")))
