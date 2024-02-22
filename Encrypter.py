import base64
import hashlib
from AESCipher import AESCipher
from PIL import Image
from random import randint
import smtplib
from email.message import EmailMessage
import imghdr

class Encrypter:
    def __init__(self, text,key):
        self.text = text
        self.key =  key
   
    def encrypt_image(self):
        aes = AESCipher(self.key)
        cipher = aes.encrypt(self.text)
        #message = aes.decrypt(cipher)
        # Sender_Email = "varierakhil7009@gmail.com"
        # Reciever_Email = "akhilvarier2000@gmail.com"

        # Password ='Aiswarya'
        # newMessage = EmailMessage()    #creating an object of EmailMessage class
        # newMessage['Subject'] = "Test Email for Encryption Key" #Defining email subject
        # newMessage['From'] = Sender_Email  #Defining sender email
        # newMessage['To'] = Reciever_Email  #Defining reciever email
        # newMessage.set_content('Encryption key is:'+str(self.key)) #Defining email body
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #     smtp.login(Sender_Email, Password)              
        #     smtp.send_message(newMessage)
        return cipher

