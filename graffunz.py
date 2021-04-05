import matplotlib.pyplot as plt
import dateparser
import cv2 as cv

def disegnaRSI(x,rsi,coppia):
    fig=plt.figure(figsize=(30,15))
    plt.title("http://danieleporcaripython.blogspot.com\n\n"+coppia+"- RSI - ")
    plt.ylabel("%RSI")
    plt.xlabel("data e ora")
    plt.plot(x,rsi,color='black')
    plt.show()
    plt.close()

def percentuale_prezzo_volumi_candele(x,prz,vlm,cnd,imgP,imgV):
    fig=plt.figure(figsize=(10,10))
    y=[]
    for i in range(len(x)):
        y.append(0)
    plt.plot(x,y,'r--')
    plt.plot(x,prz,'black')
    plt.savefig(imgP)
    plt.close()
    fig2=plt.figure(figsize=(10,10))
    plt.plot(x,y,'b--')
    plt.plot(x,vlm,'green')
    plt.savefig(imgV)
    plt.close()
    fondi(imgP,imgV)


def fondi(imgP,imgV):
    img1 = cv.imread(imgP)
    img2 = cv.imread(imgV)
    img = cv.addWeighted(img1, 0.6, img2, 0.6, 0)#img = cv.add(img1,img2)
    cv.imshow('FUSIONE',img)
    cv.waitKey(0)

def disegnaVolumi(x,c,p,v,v2):
    fig=plt.figure(figsize=(30,15))
    y=[]
    for i in range(len(x)):
        y.append(0)
    print(x)
    plt.title("http://danieleporcaripython.blogspot.com\n\n- INDICATOR - ")
    plt.subplot(211)
    plt.ylabel("Prezzi")
    plt.xlabel("data")
    plt.plot(x,y,'black')
    plt.plot(x,c,'red')
    plt.plot(x,v,'green')
    plt.plot(x,v2,'blue')
    plt.subplot(212)
    plt.ylabel("volumi")
    plt.xlabel("data")
    plt.plot(x,p,'black')
    plt.show()
    plt.close()

def disegnaPP(xms,yprezzi,r3s,r2s,r1s,APs,s1s,s2s,s3s,tf,coppia):
    r3=[]
    r2=[]
    r1=[]
    AP=[]
    s1=[]
    s2=[]
    s3=[]
    x=[]
    for i in range(len(xms)):
        parsing=str(xms[i])
        data=dateparser.parse(parsing)
        x.append(data)
    for i in range(len(x)):
        r3.append(r3s)
        r2.append(r2s)
        r1.append(r1s)
        AP.append(APs)
        s1.append(s1s)
        s2.append(s2s)
        s3.append(s3s)
    fig=plt.figure(figsize=(30,15))
    plt.title("http://danieleporcaripython.blogspot.com\n\n"+coppia+"- Pivot Point Resistenze e Supporti - ")
    plt.ylabel("Prezzi")
    plt.xlabel(tf)
    plt.plot(x, yprezzi, color = 'black')
    plt.plot(x,r3,color='red')
    pr="r3 - {0:.4f}".format(float(r3s))
    plt.text(x[0],r3[0],pr)
    plt.plot(x,r2,color='red')
    pr="r2 - {0:.4f}".format(float(r2s))
    plt.text(x[0],r2[0],pr)
    plt.plot(x,r1,color='red')
    pr="r1 - {0:.4f}".format(float(r1s))
    plt.text(x[0],r1[0],pr)
    plt.plot(x,AP,color='blue')
    pr="AP - {0:.4f}".format(float(APs))
    plt.text(x[0],AP[0],pr)
    plt.plot(x,s1,color='green')
    pr="s1 - {0:.4f}".format(float(s1s))
    plt.text(x[0],s1[0],pr)
    plt.plot(x,s2,color='green')
    pr="s2 - {0:.4f}".format(float(s2s))
    plt.text(x[0],s2[0],pr)
    plt.plot(x,s3,color='green')
    pr="s3 - {0:.4f}".format(float(s3s))
    plt.text(x[0],s3[0],pr)
    nomegrafico=coppia+".png"
    plt.savefig(nomegrafico)
    plt.show()
    plt.close()
    #plt.show()

#disegnaPP([1,2,3,4,5,6],[9,7,4,6,8,5],11,6,5,4,3,2,1,"4H")
