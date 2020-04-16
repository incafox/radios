from bs4 import BeautifulSoup
from requests import get

file = open('global_sources.txt','r')
finalFile = open('sources.json','w')
finalFile.write('{\n')
lines = file.readlines()
lines = list(set(lines))
for line in lines:
    temp = line.split('>>')
    linkRadio = temp[0].replace(' ','')
    linkStream = temp[1].replace("\n","").replace(' ','')
    print (linkRadio,linkStream)
    nombreRadio = linkRadio.split('/')[-1]
    nombreRadio = nombreRadio.replace('-',' ')
    print (nombreRadio)
    nombreRadio = nombreRadio.replace("radio","")
    if ("blob" in linkStream): linkStream = ""
    url = linkRadio
    response = get(url)
    #print(response.text[:500])
    html_soup = BeautifulSoup(response.text, 'html.parser')
    #html_soup.select_one()
    movie_containers = html_soup.find_all('div', class_ = 'thumb')
    #print (movie_containers)
    movie_containers = str(movie_containers)
    temp = movie_containers.find("src=")+5
    imagsrc = movie_containers[temp:]
    imagsrc = imagsrc[:imagsrc.find("/>")-1]
    print ("***************\n"+imagsrc+"\n***************")
    finalFile.write('\t"' + nombreRadio + '" : {\n')
    finalFile.write('\t\t' + '"link"' + ' : "' + linkRadio +'",\n' )
    finalFile.write('\t\t' + '"source"' + ' : "' + linkStream[:]+ '",\n' )
    finalFile.write('\t\t' + '"image"' + ' : "' + imagsrc+ '"\n\t\t},\n' )
    #finalFile.write('\t\t' + '}')
finalFile.write('\n}' )