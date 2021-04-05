import json
#HOW TO MANAGE DICTIONARY
#+-+-+-+-+-+-+-+-+-+-+-+#
d = {
  "Chiave": "Codice",
  "Costo": 1.23,
  "Ricarico": 30,
  "Listino": 3.00
}
c = d.items()
print(c)
lista=list(c)
for i in range(len(lista)):
    print(lista[i])
c = d.keys()
print(c)
lista=list(c)
for i in range(len(lista)):
    print(lista[i])
c=d.values()
print(c)
lista=list(c)
for i in range(len(lista)):
    print(lista[i])
nd = {
    "dizionario":{"subDict":["ch1","ch2","ch3"],
                "other":"otherSub"
                },
    "numero":2,
    "codice":"codice"
}
c=nd.items()
print(c)
lista=list(c)
for i in range(len(lista)):
    print(lista[i])
c = nd.keys()
print(c)
lista=list(c)
for i in range(len(lista)):
    print(lista[i])
c=nd.values()
print(c)
lista=list(c)
for i in range(len(lista)):
    print(lista[i])
newD=lista[0]
c=newD.values()
print(c)
lista=list(c)
for i in range(len(lista)):
    print(lista[i])
nuovaLista=lista[0]
for i in range(len(nuovaLista)):
    print(nuovaLista[i])
print("Costruzione JSON")
with open("result.json", "w") as json_file:
    json.dump(nd, json_file)
json_string = json.dumps(nd)
print(json_string)
with open("result.json","r") as json_file:
    dictFromJSon=json.load(json_file)
print(dictFromJSon)
