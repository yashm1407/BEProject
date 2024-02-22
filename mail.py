import smtplib
from email.message import EmailMessage
import imghdr

Sender_Email = "varierakhil7009@gmail.com"
Reciever_Email = "akhilvarier2000@gmail.com"

Password ='0'
newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Test Email from Encrypting Data" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email





newMessage.set_content('') #Defining email body
with open('abc.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name
newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
