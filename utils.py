import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import pathlib
import emailAccount
import time

def ora():
    now=time.strftime("%H:%M:%S")
    return now

def data():
    now=time.strftime("%d/%m/%Y")
    return now

def leggiFoglioCSV(nomeF):
    f=open(nomeF,"r")
    m=[]
    for linea in f.readlines():
        col=linea.split(",")
        col = [item for item in col if item not in ['\n']]
        m.append(col)
    f.close()
    return m

def archivio(nomefile,attributo,contenuto):
    archivio=open(nomefile,attributo)
    archivio.write(contenuto)
    archivio.close()

def archivioR(nomefile):
    f=open(nomefile,'rb')
    contenuto=f.read()
    f.close()
    return contenuto

def sendEmailAllegato(oggetto,contenuto,dest,allegato):
        email=smtplib.SMTP_SSL(emailAccount.server,emailAccount.porta)
        email.ehlo()
        email.login(emailAccount.username,emailAccount.password)
        email.ehlo()
        print("Invio")
        msg=MIMEMultipart() 
        msg['Subject']=oggetto
        msg['From']=emailAccount.mitt
        msg['To']=dest
        msg.attach(MIMEText(contenuto,'plain'))
        part = MIMEBase('application','octet-stream')
        filename = allegato
        attachement = open(filename,'rb')
        part.set_payload((attachement).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+ filename)
        msg.attach(part)

        email.sendmail(emailAccount.mitt,dest,msg.as_string())
        email.quit
        return True

def sendEmail(oggetto,contenuto):
        email=smtplib.SMTP_SSL(emailAccount.server,emailAccount.porta)
        email.ehlo()
        email.login(emailAccount.username,emailAccount.password)
        email.ehlo()
        print("Invio")
        msg=MIMEText(contenuto,'html','utf-8')
        msg['Subject']=oggetto
        msg['From']=emailAccount.mitt
        msg['To']=emailAccount.dest
        email.sendmail(emailAccount.mitt,emailAccount.dest,msg.as_string())
        email.quit
        return True
