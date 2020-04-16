from selenium import webdriver
import glob, os

directory = os.getcwd()
os.chdir(directory)
global_sources = open('global_sources.txt','w')
for file in glob.glob("*.txt"):
    if 'http' in file:
        print ('Analizando ... ')
        print(file)
        file = open(file,'r')
        print ('--- CONTENIDO ---')
        links = file.readlines()
        print (links)
        for link in links:
            os.system('python selenium-for-link.py '+ link )

        