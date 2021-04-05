import json
import sys
#Write and read json file with json library and dict
def makeJSON(jsFile):
    dict={}
    while True:
        chiave=input("Chiave> ")
        if chiave=='#e':
            break
        valori=input("Valori> ")
        lista=valori.split(' ')
        dict[chiave]=lista
    with open(jsFile,"w") as json_file:
        json.dump(dict, json_file)

def readJSON(jsFile):
    dict={}
    try:
        with open(jsFile,"r") as json_file:
            dict=json.load(json_file)
    except:
        print("File non trovato")
    return dict

def understandvalues(dict):
    n=0
    f=0.0
    l=[]
    d={}
    klist=list(dict.keys())
    for i in range(len(klist)):
        val=dict[klist[i]]
        if type(val)==type(l):
            print("Lista")
        elif type(val)==type(n) or type(val)==type(f):
            print("numero")
        elif type(val)==type(d):
            print("dizionario")

if __name__ == "__main__":
    comandi="Ho to use: ej3.py (r or w) (file name) \nr read json file\nw write json file"
    try:
        if sys.argv[1]=='r':
            d=readJSON(sys.argv[2])
            understandvalues(d)
            print(d)
        elif sys.argv[1]=='w':
            makeJSON(sys.argv[2])
        else:
            print(comandi)
    except:
        print(comandi)
