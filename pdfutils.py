from fpdf import FPDF

def elabora(titolo,sottotitolo,orientazione,lista):
    pdf=FPDF()
    pdf.add_page(orientation=orientazione)
    pdf.set_font("Arial","B", size=15)
    pdf.cell(w=0,h=10,txt=titolo, ln= 2, align='C')
    pdf.set_font("Arial","U", size=12)
    pdf.set_text_color(0,0,255)
    pdf.cell(w=0,h=0,txt=sottotitolo, ln= 2, align='C',link="https://danieleporcaripython.blogspot.com/p/support-my-work-my-crypto-wallet.html")
    pdf.set_font("Arial", size=10)
    pdf.cell(w=0,h=20,txt="", ln=2, align='C')
    pdf.set_text_color(0,0,0)
    primo=True
    col=lista.split(",")
    m=[]
    for l in col:
        c2=l.split(":")
        m.append(c2)
    i=0
    for i in range(len(m)):
        if m[i][0]=='img':
            pdf.add_page(orientation=orientazione)
            immagine=str(m[i][1])
            pdf.image(immagine,x=1,y=1,w=300,h=200)
        elif m[i][0]=='txt':
            f=open(str(m[i][1]),"r")
            fl=f.read()
            f.close()
            pdf.set_font("Arial", size=12)
            if primo:
                pdf.write(5,fl)
            else:
                pdf.add_page(orientation=orientazione)
                pdf.write(5,fl)
            primo=False
        elif m[i][0]=='xls':
            print(m[i][1])
        else:
            print("comando non riconosciuto")
        i+=1
    pdf.output(titolo+".pdf")

def makePDF(analisi,grafico,titolo):
    pdf = FPDF()
    pdf.add_page(orientation = 'L')
    pdf.set_font("Arial", size=10)
    pdf.cell(w=0,h=0,txt = "https://danieleporcaripyhton.blogspot.com",  ln = 1, align = 'C',link="https://danieleporcaripython.blogspot.com")
    pdf.set_font("Arial", size=15)
    pdf.cell(w=0,h=10,txt="Analisi automatica su dati forniti da API Binance Futures Perpetual", ln= 2, align='C')
    pdf.set_font("Arial", size=12)
    pdf.write(5,analisi)
    pdf.add_page(orientation = 'L')
    pdf.image(grafico,x=1,y=1,w=300,h=200)
    titolocompleto=titolo+".pdf"
    pdf.output(titolocompleto)

if __name__ == "__main__":
    sottotitolo="https://danieleporcaripython.blogspot.com"
    elabora("Prova2",sottotitolo,"L","txt:testo1.txt")
