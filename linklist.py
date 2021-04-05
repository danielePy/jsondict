from bs4 import BeautifulSoup
import urllib3
import sys
import json
url = sys.argv[1]
jsFile=sys.argv[2]
avanza=int(sys.argv[3])
http = urllib3.PoolManager()
listaIndirizzi=[]
urlList=url.split('.')
num=int(urlList[3])
num2=int(urlList[2])
listaIndirizzi.append(url)
for i in range(avanza):
    if num<255:
        num+=1
        indirizzo=urlList[0]+"."+urlList[1]+"."+str(num2)+"."+str(num)
    else:
        num=0
        num2+=1
        indirizzo=urlList[0]+"."+urlList[1]+"."+str(num2)+"."+str(num)
    listaIndirizzi.append(indirizzo)
for i in range(avanza):
    try:
        response = http.request('GET', listaIndirizzi[i])
        print("INDIRIZZO \n"+listaIndirizzi[i])
        zuppa=BeautifulSoup(response.data)
        linkA=zuppa.findAll('a')
        listaPagine=[]
        for tag in linkA:
            link = tag["href"]
            listaPagine.append(link)
            print(listaPagine)
    except:
        print("Nessuna risposta \n"+listaIndirizzi[i])

    dizionario={}
    dizionario[url]=listaPagine
    with open(jsFile,"w") as json_file:
        json.dump(dizionario, json_file)
