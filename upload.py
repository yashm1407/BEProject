import hashlib
import base64
import hashlib
from random import randint
import smtplib
from email.message import EmailMessage
import imghdr
import string
from text_encryption import Encryption
from text_encryption import Decryption
from tkinter import *
import tkinter as tk
from Crypto.Cipher import AES
from PIL import Image ,ImageTk
from pymsgbox import *
from tkinter import messagebox as ms
from tkinter.filedialog import askopenfilename
import sqlite3

root=tk.Tk()
root.title('IMAGE AND TEXT ENCRYPTION USING AES ALGORITHM')
root.geometry('925x500+200+200')
root.configure(bg='#fff')
root.resizable(False,False)
heading1=Label(root,text='IMAGE AND TEXT ENCRYPTION',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading1.place(x=225,y=30)

s_file= ""
new_key = tk.IntVar()
new_key1 = tk.IntVar()
def upload_Image():
    global fn
    fileName = askopenfilename(initialdir='E:/', title='Select image for Encryption ',
                               filetypes=[("png", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName
    im1 = Image.open(imgpath) 

    md5_hash = hashlib.md5()
    with open(fn,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        a=md5_hash.hexdigest()

    db = sqlite3.connect('evaluation.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS img_database"
               "(name TEXT, key TEXT)")
    db.commit()
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        bad_chars = [',', '(', ')', "'"]
 
        c.execute('SELECT key FROM img_database WHERE key = ?', (a,))
        records = c.fetchall()
        listToStr = ' '.join([str(elem) for elem in records])
        delete_dict = {sp_character: '' for sp_character in string.punctuation}
        delete_dict[' '] = ''
        table = str.maketrans(delete_dict)
        test_string = listToStr.translate(table)
           
        if test_string == str(a):
               ms.showinfo('Error!', 'Image Already Exist !')
            
        else:
                conn = sqlite3.connect('evaluation.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        'INSERT INTO img_database(name, key) VALUES(?,?)',
                        (fileName, a))
                    conn.commit()
                    ms.showinfo('Success!', 'Stored Successfully !')
                    im1=im1.save("fn.png")
                    from subprocess import call
                    call(["python","main.py"])
                    
def upload_text():
    global fn
    fileName = askopenfilename(initialdir='E:/', title='Select image for Encryption ',
                               filetypes=[("all files", "*.*")])
    file1 = open(fileName,"r+") 
    fn=file1.read()
    
    md5_hash = hashlib.md5()
    with open(fileName,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        a=md5_hash.hexdigest()
  
    db = sqlite3.connect('evaluation.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS text_database"
               "(name TEXT, key TEXT)")
    db.commit()
    
    
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        bad_chars = [',', '(', ')', "'"]
        c.execute('SELECT key FROM text_database WHERE key = ?', (a,))
        records = c.fetchall()
        listToStr = ' '.join([str(elem) for elem in records])
        delete_dict = {sp_character: '' for sp_character in string.punctuation}
        delete_dict[' '] = ''
        table = str.maketrans(delete_dict)
        test_string = listToStr.translate(table)
        
        if test_string == str(a):
               ms.showinfo('Error!', 'This Text File Already Exist !')
            
        else:
                conn = sqlite3.connect('evaluation.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO text_database(name, key) VALUES(?,?)',
                        (fileName, a))
                    conn.commit()
                    ms.showinfo('Success!', 'Stored Successfully !')   
                    save_text = open("myfile.txt" , 'w')
                    save_text.write(fn)
                    save_text.close()
                    frame = tk.LabelFrame(root, text="", width=300, height=300, bd=5, font=('Microsoft YaHei UI Light',23),bg="white")
                    # frame.grid(row=0, column=0, sticky='nw')
                    frame.place(x=250, y=120)
                    def onClickDecrypt():
                        key=new_key1.get()
                        # Sender_Email = "varierakhil7009@gmail.com"
                        # Reciever_Email = "akhilvarier2000@gmail.com"

                        # Password ='Aiswarya'
                        # newMessage = EmailMessage()    #creating an object of EmailMessage class
                        # newMessage['Subject'] = "Test Email for Encryption Key" #Defining email subject
                        # newMessage['From'] = Sender_Email  #Defining sender email
                        # newMessage['To'] = Reciever_Email  #Defining reciever email
                        # newMessage.set_content('Encryption key is:'+str(key)) #Defining email body
                        # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        #         smtp.login(Sender_Email, Password)              
                        #         smtp.send_message(newMessage)
        
                        cipher=Decryption(fileName,key)
                        fh = open("cipher_decrypt_text.txt", "w")
                        fh.write(cipher)
                        fh.close()
                        T = Text(root, height = 5, width = 70)
                        T.place(x=370, y=500)
                        T.insert(tk.END, cipher)
                        ms.showinfo('Success!', 'Decryption Successful !')
                    
                    def onClickEncrypt():
                        key=new_key.get()
                        cipher=Encryption(fileName,key)
                        fh = open("cipher_encrpt_text.txt", "w")
                        fh.write(cipher)
                        fh.close()
                        T = Text(root, height = 5, width = 70)
                        T.place(x=370, y=500)
                        T.insert(tk.END, cipher)
                        ms.showinfo('Success!', 'Encryption Successful !') 
                        T.destroy()
                        frame1 = tk.LabelFrame(root, text="", width=300, height=300, bd=5, font=('Microsoft YaHei UI Light',23),bg="white")
                        # frame1.grid(row=0, column=0, sticky='nw')
                        frame1.place(x=250, y=120)
                    
                    
                        l2 = tk.Label(frame1, text="Enter Key :", width=12, font=('Microsoft YaHei UI Light',16), bg="white",bd=5)
                        l2.place(x=70, y=60)
                        t1 = tk.Entry(frame1, textvar=new_key1, width=20, font=('', 15),bd=5)
                        t1.place(x=30, y=130)
    
                        btn = tk.Button(frame1, text="Decrypt", bg='#57a1f8',font=('Microsoft YaHei UI Light',16),fg="white", width=9, height=1, command=onClickDecrypt)
                        btn.place(x=85, y=180)
                        
                    l2 = tk.Label(frame, text="Enter Key :", width=12, font=('Microsoft YaHei UI Light',16), bg="white",fg='#57a1f8',bd=5)
                    l2.place(x=70, y=60)
                    t1 = tk.Entry(frame, textvar=new_key, width=20, font=('', 15),bd=5)
                    t1.place(x=30, y=130)
                                        
                    btn = tk.Button(frame, text="Encrypt",font=('Microsoft YaHei UI Light',16),bg='#57a1f8',fg='white', width=9, height=1, command=onClickEncrypt)
                    btn.place(x=85, y=200)

                    
img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=100)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Welcome',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23))
heading.place(x=110,y=100)

Button(frame,width=39,pady=7,text='Select Image',bg='#57a1f8',fg='white',border=0,command=upload_Image).place(x=35,y=150)
Button(frame,width=39,pady=7,text='Select Text',bg='#57a1f8',fg='white',border=0,command=upload_text).place(x=35,y=190)

root.mainloop()
