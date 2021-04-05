import string
import time
import datetime
import simpleBinanceFut
import graffunz
import dateparser

def pp(h,l,c):
    ap=(h+l+c)/3
    s1=(2*ap)-h
    r1=(2*ap)-l
    s2=ap-(r1-s1)
    r2=(ap-s1)+r1
    s3=s2-(h-l)
    r3=r2+(h-l)
    return r3,r2,r1,ap,s1,s2,s3

def calcPP(coppia,periodo,tf):
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date.today()
    pdateObj=start_date - periodo*day_delta
    pdate=pdateObj.strftime("%d-%b-%y")
    print(pdate)
    dati = simpleBinanceFut.fbin_candlestick(coppia,tf)
    i=0
    diffMaxMinPrec=0
    diffApChPrec=0
    c=len(dati)
    vx=[]
    vy=[]
    for i in range(c):
        vx.append(dati[i][0])
        ap=float(dati[i][1])#ap=float(dati[i][1])
        ch=float(dati[i][4])#ch=float(dati[i][2])
        max=float(dati[i][2])#max=float(dati[i][2])
        min=float(dati[i][3])#min=float(dati[i][3])
        media=(ap+ch)/2
        vy.append(media)
        diffMaxMin=max-min
        diffApCh=abs(ap-ch)
        if diffMaxMin > diffMaxMinPrec and diffApCh > diffApChPrec:
            diffMaxMinPrec=diffMaxMin
            diffApChPrec=diffApCh
            candelaPivot=i
        i=i+1
    r3,r2,r1,ap,s1,s2,s3=pp(float(dati[candelaPivot][2]),float(dati[candelaPivot][3]),float(dati[candelaPivot][4]))
    contenuto="Pivot Point\n R3: {0:.5f}".format(float(r3))
    contenuto=contenuto+"\n R2: {0:.5f}".format(float(r2))
    contenuto=contenuto+"\n R1: {0:.5f}".format(float(r1))
    contenuto=contenuto+"\n AP: {0:.5f}".format(float(ap))
    contenuto=contenuto+"\n S1: {0:.5f}".format(float(s1))
    contenuto=contenuto+"\n S2: {0:.5f}".format(float(s2))
    contenuto=contenuto+"\n S3: {0:.5f}".format(float(s3))
    graffunz.disegnaPP(vx,vy,r3,r2,r1,ap,s1,s2,s3,tf,coppia)
    return contenuto,vx,vy,r3,r2,r1,ap,s1,s2,s3

def calcPP(coppia,periodo,tf):
    day_delta = datetime.timedelta(days=1)
    start_date = datetime.date.today()
    pdateObj=start_date - periodo*day_delta
    pdate=pdateObj.strftime("%d-%b-%y")
    print(pdate)
    dati = simpleBinanceFut.fbin_candlestick(coppia,tf)
    i=0
    diffMaxMinPrec=0
    diffApChPrec=0
    c=len(dati)
    vx=[]
    vy=[]
    for i in range(c):
        vx.append(dati[i][0])
        ap=float(dati[i][1])#ap=float(dati[i][1])
        ch=float(dati[i][4])#ch=float(dati[i][2])
        max=float(dati[i][2])#max=float(dati[i][2])
        min=float(dati[i][3])#min=float(dati[i][3])
        media=(ap+ch)/2
        vy.append(media)
        diffMaxMin=max-min
        diffApCh=abs(ap-ch)
        if diffMaxMin > diffMaxMinPrec and diffApCh > diffApChPrec:
            diffMaxMinPrec=diffMaxMin
            diffApChPrec=diffApCh
            candelaPivot=i
        i=i+1
    r3,r2,r1,ap,s1,s2,s3=pp(float(dati[candelaPivot][2]),float(dati[candelaPivot][3]),float(dati[candelaPivot][4]))
    contenuto=" Pivot Point\n R3: {0:.5f}".format(float(r3))
    contenuto=contenuto+"\n R2: {0:.5f}".format(float(r2))
    contenuto=contenuto+"\n R1: {0:.5f}".format(float(r1))
    contenuto=contenuto+"\n AP: {0:.5f}".format(float(ap))
    contenuto=contenuto+"\n S1: {0:.5f}".format(float(s1))
    contenuto=contenuto+"\n S2: {0:.5f}".format(float(s2))
    contenuto=contenuto+"\n S3: {0:.5f}".format(float(s3))
    #graffunz.disegnaPP(vx,vy,r3,r2,r1,ap,s1,s2,s3,tf,coppia)
    return contenuto,vx,vy,r3,r2,r1,ap,s1,s2,s3,dati


def analisiAsset(coppia,periodo,tf):
    oP,hP,lwP,lP,wAP=simpleBinanceFut.fbin_24h_statisticheprezzo(coppia)
    basestr="Prezzo di apertura: "+str(oP)+"\nPrezzo massimo: "+str(hP)+"\nPrezzo minimo: "+str(lwP)+"\nPrezzo medio: "+str(wAP)+"\n"
    basestr=basestr+"Prezzo: "+str(lP)
    timeframe=['1d','4h','1h']
    tipo=['lungo','medio','breve']
    for c in range(len(timeframe)):
        trend=scopriTrend(coppia,timeframe[c],tipo[c])
        basestr=basestr+"\nAttualmente su time frame "+timeframe[c]+" "+trend+"\n"
        basestr=basestr+"\n"
    return basestr,lP

def verificaMA(mab,mam,mas):
    if (mam>mab) and (mas>mam):
        risultato="Trend Rialzista"
    elif (mam<mab) and (mas<mam):
        risultato="Trend Ribassista"
    else:
        risultato="Nessun trend ben definito"
    return risultato

def scopriTrend(coppia,tf,tipo):
    vect = simpleBinanceFut.fbin_candlestick(coppia,tf)
    if tipo=='lungo':
        mab=MA(vect,112)
        mam=MA(vect,56)
        mas=MA(vect,28)
    elif tipo=='medio':
        mab=MA(vect,56)
        mam=MA(vect,28)
        mas=MA(vect,9)
    else:
        mab=MA(vect,56)
        mam=MA(vect,14)
        mas=MA(vect,9)
    risultato=verificaMA(mab,mam,mas)
    risultato="rilevato"+risultato
    return risultato

def MA(dati,periodo):
    prezzi=list(range(0,len(dati)))
    i=0
    c=len(prezzi)-1
    for i in range(len(prezzi)):
        prezzi[c]=float(dati[i][4])
        i=i+1
        c=c-1
    i=1
    c=0
    ris=0
    for i in range(periodo):
        ris=ris+prezzi[i+c]
        i=i+1
    ris=ris/periodo
    return ris

def MAlist(dati,periodo,pmedia):
    ma=[]
    k=0
    p=0
    totale=periodo+pmedia
    ribalta=[]
    c=len(dati)-1
    for i in range(len(dati)):
        ribalta.append(dati[c][4])
        c-=1
    for i in range(totale):
        for c in range(pmedia):
            p=p+float(ribalta[i+c])
        k=p/pmedia
        p=0
        ma.append(k)
    for i in range(pmedia):
        ma.remove(ma[i])
    return ma

def percentuale_prezzo_volumi_candele(dati):
    cahm=4 #chiusura apertura high min
    x=[]
    for i in range(len(dati)):
        parsing=str(dati[i][0])
        data=dateparser.parse(parsing)
        x.append(data)
    przPrc=0
    prz=[]
    vlmPrc=0
    vlm=[]
    cndPrc=0
    cnd=[]
    for i in range(len(dati)):
        cnd.append(float(dati[i][cahm]))
        przA=float(dati[i][cahm])
        if przPrc==0:
            przPrc=przA
            vlmPrc=float(dati[i][5])
            calcP=((przA-przPrc)/przPrc)*100 #evito divisione per 0 ed essendo il primo della lista non c'è differenza di %
            przPrc=przA
            prz.append(calcP)
            przA=float(dati[i][5])
            calcP=((przA-vlmPrc)/vlmPrc)*100
            vlmPrc=przA
            vlm.append(calcP)
        else:
            calcP=((przA-przPrc)/przPrc)*100 #evito divisione per 0 ed essendo il primo della lista non c'è differenza di %
            przPrc=przA
            prz.append(calcP)
            przA=float(dati[i][5])
            calcP=((przA-vlmPrc)/vlmPrc)*100
            calcP=((vlmPrc-przA)/przA)*100
            vlmPrc=przA
            vlm.append(calcP)

    return x,prz,vlm,cnd

def volume(dati,periodo,apartireda):
    x=[]
    daesaminare=len(dati)-(periodo-apartireda)
    fine=len(dati)-apartireda
    for i in range(periodo):
        x.append(i)
    p=[]
    c=[]
    iP=0.0
    daesaminare=len(dati)-(periodo-apartireda)
    prec=0
    vPrec=0
    vP=0
    volP=[]
    pzzPerc=[]
    volPerc=[]
    candPerc=[]
    pzzPrec=0
    volPrec=0
    cPrec=0
    while daesaminare<fine:
        if float(dati[daesaminare][1])<float(dati[daesaminare][4]):#candelapositiva
            p.append(float(dati[daesaminare][4]))
            medio=(float(dati[daesaminare][4])+float(dati[daesaminare][3])+float(dati[daesaminare][2])+float(dati[daesaminare][1]))/4
            if medio < prec:
                iP+=1
                if float(dati[daesaminare][5])<vPrec:
                    vP-=1
                else:
                    vP-=1.5
            else:
                iP+=1.5
            c.append(iP)
            volP.append(vP)
            prec=medio
            vPrec=float(dati[daesaminare][5])
        else:#candela negativa
            p.append(float(dati[daesaminare][4]))
            medio=(float(dati[daesaminare][4])+float(dati[daesaminare][3])+float(dati[daesaminare][2])+float(dati[daesaminare][1]))/4
            if medio > prec:
                iP-=1
                if float(dati[daesaminare][5])>vPrec:
                    vP+=1
                else:
                    vP+=1.5
            else:
                iP-=1.5
            c.append(iP)
            volP.append(vP)
            prec=medio
            vPrec=float(dati[daesaminare][5])
        daesaminare+=1
    vPrec=0
    volP2=[]
    vP=0
    daesaminare=len(dati)-periodo-apartireda
    while daesaminare<fine:
        if float(dati[daesaminare][5])<vPrec:
            vP+=1
            vPrec=float(dati[daesaminare][5])
        else:
            vP-=1
            vPrec=float(dati[daesaminare][5])
        volP2.append(vP)
        daesaminare+=1
    return x,c,p,volP,volP2

def RSI(dati,periodo_rsi):#RSI = 100 – [ 100 / ( 1 + RS )] chiusure rialzo e chiusure ribasso
    x=[]
    rsi=[]
    mh=[]
    ml=[]
    c=len(dati)
    media=0
    for i in range(len(dati)):
        parsing=str(dati[i][0])
        data=dateparser.parse(parsing)
        x.append(data)
    for i in range(len(dati)):
        for c in range(periodo_rsi):
            if (i+periodo_rsi)<len(dati):
                media=media+float(dati[i+c][2])
        media=media/periodo_rsi
        mh.append(media)
    for i in range(len(dati)):
        for c in range(periodo_rsi):
            if (i+periodo_rsi)<len(dati):
                media=media+float(dati[i+c][3])
        media=media/periodo_rsi
        ml.append(media)
    parziale=[]
    for i in range(periodo_rsi):
        rsi.append(100 - (100/2))
    for i in range(len(mh)-periodo_rsi):
        rapporto=mh[i]/ml[i]
        parziale.append(rapporto)
    for i in range(len(parziale)):
        parz = 100 - (100/(1+parziale[i]))
        rsi.append(parz)
    return x,rsi
