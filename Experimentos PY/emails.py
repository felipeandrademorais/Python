#coding: utf-8

import smtplib
import time
from email.mime.text import MIMEText

tempo = 1
de = 'relacionamento@grupozanardo.com.br'
para = []
usuario = []

#importar lista e preencher a list "para"
with open('C:\Users\Felipe\Desktop\email.csv') as inputfile:
    for line in inputfile:
        para.append(line.strip().split('\n'))


#importar nome e usuario e preencher a list "usuario"
#with open('C:\Users\Felipe\Desktop\usuario.csv') as inputfile:
#    for line in inputfile:
#        usuario.append(line.strip().split('\n'))

#envia o e-mail
for x in range(0, len(para)):
    #Dados do E-mail
    msg = MIMEText("<p>Boa tarde,<br/></p><p>Preciso que todos me confirmem se tem usuários no Portal GPS e no Microsiga(Smart Client) <br/>"
                   "<a href='http://portal.gpssa.com.br/GPS/Login.aspx?ReturnUrl=%2fGPS%2fPortal.aspx'>Portal GPS</a>"
                   "<p>É muito importante que você tenha esses usuarios e senhas para que possamos efetuar os testes de folha...</p>"
                   "<p>Caso alguém não tenha usuario em alguns dos sistemas favor enviar e-mail para <a href='mailto:suporte.ti@grupozanardo.com.br'>suporte.ti</a> solicitando...</p>"
                   "<p>Atenciosamente<br/>Felipe Andrade de Morais<br/>Suporte TI </p>", 'html', 'utf-8')
    msg['From'] = de
    #msg['Cc'] = ','.join(['eliane.mendes@gpssa.com.br'])
    msg['Subject'] = 'Pesquisa Sistemas Onseg'

    raw = msg.as_string()

    time.sleep(tempo) #pausa para enviar próximo e-mail
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login('relacionamento@grupozanardo.com.br', 'Zanardo2016')
    smtp.sendmail(de, para[x], raw)
    smtp.quit()

