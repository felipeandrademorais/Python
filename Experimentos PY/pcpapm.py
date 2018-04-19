import smtplib
import cv2
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#Captura Imagem Camera
cam = cv2.VideoCapture(0)
frame = cam.read()[1]
cv2.imwrite(filename='frame.jpg', img=frame)

#Dados E-mail
de = 'depto.ti@grupozanardo.com.br'
para = ['suporte.ti@grupozanardo.com.br']

#Corpo do E-mail
msg = MIMEMultipart()
msg['Subject'] = 'Image WebCam'
msg['From'] = de
msg['To'] = ','.join(para)
msg.preamble = 'Image WebCam'

# Abre a imagem e inclue no e-mail
fp = open('frame.jpg', 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

#Envia o e-mail
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('depto.ti@grupozanardo.com.br', 'Zanardo2016')
smtp.sendmail(de, para, msg.as_string())
smtp.quit()
