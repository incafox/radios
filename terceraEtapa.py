import scrapy
import os

class QuotesSpider(scrapy.Spider):
    name = "http://www.radiosdelperu.pe"
    start_urls = []
    file = open("segundaEtapa.txt","r")
    te = file.read().split(',')[1:-1]
    for e in te:
        print (e)
        if ("/radio/") in e:
            start_urls.append(name+e[2:-1])
    print (start_urls)

    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        print ("para cada response")
        print (response.url)
        nombre = str(response.url).replace('/','-')+ str('.txt')
        fileres = open(nombre,"w")
        lista = response.xpath("//body/div/div/div/ul/li/div/a")
        charac = 'href="'
        name = "http://www.radiosdelperu.pe"
        for e in lista:
            #print (type(e))
            se = str(e)
            start = se.find(charac)+len(charac)
            se = se[start:]
            end = se.find('"')
            fileres.write(name+se[:end]+"\n")
        fileres.close()
