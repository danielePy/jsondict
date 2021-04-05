import pdfutils
import trFunzNew
import simpleBinanceFut
import utils
import vedi

def readAsset(testo):
    f=open(testo,"r")
    m=[]
    for linea in f.readlines():
        rows=linea.split(":")
        m.append(rows)
    f.close()
    listaAsset=[]
    for i in range(len(m)):
        lista = m[i][1].split(",")
        lista = [item for item in lista if item not in ['\n']]
        listaAsset.append(lista)
    vettoreAssetUnivoco=[]
    for i in range(len(listaAsset)):
            for c in range(len(listaAsset[i])):
                dato=listaAsset[i][c]
                if len(vettoreAssetUnivoco)>0:
                    trovato=False
                    for z in range(len(vettoreAssetUnivoco)):
                        if dato==vettoreAssetUnivoco[z]:
                            trovato=True
                    if not(trovato):
                        vettoreAssetUnivoco.append(dato)
                else:
                    vettoreAssetUnivoco.append(dato)
    return vettoreAssetUnivoco

def invioPdf(testo):
    f=open(testo,"r")
    m=[]
    for linea in f.readlines():
        rows=linea.split(":")
        m.append(rows)
    f.close()
    listaAsset=[]
    for i in range(len(m)):
        lista = m[i][1].split(",")
        lista = [item for item in lista if item not in ['\n']]
        for c in range(len(lista)):
            coppia=lista[c]
            oggetto="Analisi "+coppia
            contenuto="Questa email ti è stata spedita perchè qualcuno ti ha registrato a questo servizio.\n Se non vuoi più ricevere le analisi rispondi a questa email esprimendo il tuo dissenso al servizio.\n"
            dest=m[i][0]
            allegato=coppia+".pdf"
            utils.sendEmailAllegato(oggetto,contenuto,dest,allegato)

asset=readAsset("listaemailprova.dat")
for i in range(len(asset)):
    tf="1d"
    periodo=60
    baseAnal,lP=trFunzNew.analisiAsset(asset[i],periodo,tf)
    ok=False
    c=0
    timeFrame=['4h','1h']
    while not(ok) and c<=1:
        pivot,r3,r2,r1,ap,s1,s2,s3=trFunzNew.calcPP(asset[i],periodo,tf)
        if float(lP)>float(r3) or float(lP)<float(s1):
            tf=timeFrame[c]
            ok=False
        else:
            ok=True
        c+=1
        analisi=baseAnal+"\n"+pivot+"\n"
        nomefile=asset[i]+".txt"
        f=open(nomefile,"w")
        f.write(analisi)
        f.close()
        immagine=asset[i]+".png"
        contenuti="txt:"+nomefile+",img:"+immagine
        ris,ris2,tazza,nGT=vedi.eseguiRicercaTazza(asset[i])
        if tazza==True:
            ris=ris+ris2+"\nLa profondità della tazza, riportata dal basso verso l'alto alla rottura del manico, ci dice il massimo obiettivo raggiungibile.\n"
            nomefile="tazza.txt"
            f=open(nomefile,"w")
            f.write(ris)
            f.close()
            contenuti=contenuti+",txt:"+nomefile+",img:"+nGT
        ris,ris2,ts,nGT=vedi.eseguiRicercaTS(asset[i])
        if ts==True:
            ris=ris+ris2+"Il testa e spalle è una figura di inversione. L'obiettivo si calcola misurando dalla testa alla neckline e riportandolo dalla neckline verso il basso.\n"
            nomefile="ts.txt"
            f=open(nomefile,"w")
            f.write(ris)
            f.close()
            contenuti=contenuti+",txt:"+nomefile+",img:"+nGT
        titolo=asset[i]
        pdfutils.elabora(titolo,"https://danieleporcaripython.blogspot.com","L",contenuti)
invioPdf("listaemailprova.dat")
