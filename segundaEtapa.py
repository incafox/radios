import scrapy
import os
import time
#execfile("scraper.py")
os.system("scrapy runspider scraper.py")

time.sleep(2)
file = open("scraper.txt","r")
file2 = open("segundaEtapa.txt","w")

temp = file.read().split(',')
#print (temp)
#for e in temp:
#    print (parser(e))

def parser(element):
    res = ''
    s = 'href="'
    if s in element:
        res = element[element.find(s)+len(s):]
        t = res.find('"')
        res = res[:t]
        if 'http' in res or "'" in res or len(res)<4:
            return 
        #if ('radio' in res) == False:
         #   return
    return res
temporal = []
for e in temp:
    print (parser(e))
    temporal.append(parser(e))

file2.write(str(temporal))
