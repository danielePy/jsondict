import json
#Da stimoli esterni il software allarga le proprie conoscenze

def caricaCoscienza(nomeCoscienza):
    with open(nomeCoscienza,"r") as json_file:
        dictFromJSon=json.load(json_file)
    return dictFromJSon

def memorizza(valori,dict,nomeCoscienza):
    chiave=valori[0]
    lista=[]
    for i in range(len(valori)):
        if i>0:
            lista.append(valori[i])
    dict[chiave]=lista
    with open(nomeCoscienza,"w") as json_file:
            json.dump(dict, json_file)
    with open(nomeCoscienza,"r") as json_file:
        dictFromJSon=json.load(json_file)
    return dictFromJSon

def elabora(valori,ch,keys,dict):
    chiave=keys[ch]
    risposta=dict[chiave]
    return risposta

def ricerca(ingresso,dict,nomeCoscienza):
    keys=list(dict.keys())
    valori=ingresso.split(' ')
    trovato=False
    r=''
    for i in range(len(keys)):
        for c in range(len(valori)):
            if keys[i]==valori[c]:
                trovato=True
                ch=i
    if not(trovato):
        dict=memorizza(valori,dict,nomeCoscienza)
    else:
        r=elabora(valori,ch,keys,dict)
    return r


if __name__ == "__main__":
    dict=caricaCoscienza("result.json")
    dato=input(">")
    print(ricerca(dato,dict,"result.json"))
