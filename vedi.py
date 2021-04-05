from PIL import Image, ImageFilter
import imagehash
import matplotlib.pyplot as plt
import requests
import json
import simpleBinanceFut

def binanceList(coppia,intervallo):
    coppia=coppia.upper()
    indirizzo='https://fapi.binance.com/fapi/v1/klines?symbol='+coppia+'&interval='+intervallo+'&limit=30'
    r=requests.get(indirizzo)
    file=r.text
    lista=json.loads(file)
    x=[]
    y=[]
    for i in range(len(lista)):
        x.append(lista[i][0])
        y.append(float(lista[i][4]))
    return x,y

def disegnaGrafico(x,y,asset):
    ok=False
    fig=plt.figure(figsize=(14,14))
    plt.plot(x,y,color='black')
    nome=asset+"PG.png"
    plt.savefig(nome)
    return nome

def togliCornice(immagine,asset):
    ok=False
    img=Image.open(immagine)
    w,h=img.size
    l=180
    t=172
    r=w-159
    b=h-163
    nome=asset+"Confronto.png"
    img.crop((l, t, r, b)).save(nome)
    img.close()
    return nome

def confronto(attuale,base,base2):
    tazza=True
    img = Image.open(base)
    image_one_hash = imagehash.whash(img)
    img2 = Image.open(attuale)
    image_two_hash = imagehash.whash(img2)
    similarity = image_one_hash - image_two_hash
    img.close()
    img2.close()
    if similarity>20:
        img=Image.open(base2)
        image_one_hash = imagehash.whash(img)
        similarity2 = image_one_hash - image_two_hash
        if similarity>similarity2:
            similarity=similarity2
        tazza=False
    img.close()
    img2.close()
    return similarity,tazza

def confrontoTestaSpalle():
    ok=False
    return ok

def eseguiRicercaTazza(asset):
    ris4h=""
    ris1h=""
    x,y=binanceList(asset,'4h')
    nomeGraf=disegnaGrafico(x,y,asset)
    grafOk=togliCornice(nomeGraf,asset)
    similarity,cup=confronto(grafOk,'tazza.png','tazza2.png')
    if cup==True:
        ris4h="Possibile pattern grafico tazza su TF 4H\n "
    elif cup==False:
        similarity,cup=confronto(grafOk,'tazza3.png','tazza4.png')
        if cup==True:
            ris4h="Possibile pattern grafico tazza su TF 4H\n "
    else:
        ris4h="Non ho trovato pattern grafico su 4H\n "
    x,y=binanceList(asset,'1h')
    nomeGraf=disegnaGrafico(x,y,asset)
    grafOk=togliCornice(nomeGraf,asset)
    similarity,cup=confronto(grafOk,'tazza.png','tazza2.png')
    if cup==True:
        ris1h="Possibile pattern grafico tazza su TF 1H\n "
    elif cup==False:
        similarity,cup=confronto(grafOk,'tazza3.png','tazza4.png')
        if cup==True:
            ris1h="Possibile pattern grafico tazza su TF 1H\n "
    else:
        ris1h="Non ho trovato pattern grafico su 1H\n "
    return ris4h,ris1h,cup,nomeGraf

def eseguiRicercaTS(asset):
    risultato=""
    ris1h=""
    x,y=binanceList(asset,'4h')
    nomeGraf=disegnaGrafico(x,y,asset)
    grafOk=togliCornice(nomeGraf,asset)
    similarity,cup=confronto(grafOk,'tes.png','tes2.png')
    if cup==True:
        risultato="Possibile pattern grafico testa e spalle su TF 4H\n "
    elif cup==False:
        similarity,cup=confronto(grafOk,'tes3.png','tes4.png')
        if cup==True:
            risultato="Possibile pattern grafico testa e spalle su TF 4H\n "
    else:
        risultato="Non ho trovato pattern grafici\n "
    x,y=binanceList(asset,'1h')
    nomeGraf=disegnaGrafico(x,y,asset)
    grafOk=togliCornice(nomeGraf,asset)
    similarity,cup=confronto(grafOk,'tes3.png','tes4.png')
    if cup==True:
        ris1h="Possibile pattern grafico testa e spalle su TF 1H\n "
    elif cup==False:
        similarity,cup=confronto(grafOk,'tes3.png','tes4.png')
        if cup==True:
            ris1h="Possibile pattern grafico testa e spalle su TF 1H\n "
    else:
        ris1h="Non ho trovato pattern grafici\n "
    return risultato,ris1h,cup,nomeGraf
