import tkinter as tk
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os


window = tk.Tk()
window.geometry('925x600+200+200')
window.title("REGISTRATION FORM")
window.configure(bg='#fff')
window.resizable(False,False)

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
value = random.randint(1, 1000)

db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()

def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            window.destroy()

img = PhotoImage(file='login (1).png')
Label(window,image=img,bg='white').place(x=50,y=130)

lbl = Label(window, text="Registration Form",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
lbl.place(x=300, y=10)

l2 = Label(window, text="Full Name :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l2.place(x=450, y=84)
t1 = Entry(window, textvar=Fullname,width=31,fg='black',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t1.place(x=600, y=80, height=30)

l3 = Label(window, text="Address :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l3.place(x=450, y=134)
t2 = Entry(window, textvar=address, width=31,fg='black',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t2.place(x=600, y=130, height=30)

l5 = Label(window, text="E-mail :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l5.place(x=450, y=184)
t4 = Entry(window, textvar=Email, width=31,fg='black',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t4.place(x=600, y=180, height=30)

l6 = Label(window, text="Phone number :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l6.place(x=450, y=234)
t5 = Entry(window, textvar=Phoneno, width=31,fg='black',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t5.place(x=600, y=230, height=30)

l7 = Label(window, text="Gender :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l7.place(x=450, y=284)
Radiobutton(window, text="Male", padx=5, width=5, bg='white', font=('Microsoft YaHei UI Light',11), variable=var, value=1).place(x=600,y=280,height=30)
Radiobutton(window, text="Female", padx=20, width=4, bg='white', font=('Microsoft YaHei UI Light',11), variable=var, value=2).place(x=700, y=280,height=30)

l8 = Label(window, text="Age :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l8.place(x=450, y=334)
t6 = Entry(window, textvar=age, width=31,fg='black',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t6.place(x=600, y=330, height=30)

l4 = Label(window, text="User Name :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l4.place(x=450, y=384)
t3 = Entry(window, textvar=username, width=31,fg='black',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t3.place(x=600, y=380, height=30)

l9 = Label(window, text="Password :", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l9.place(x=450, y=434)
t9 = Entry(window, textvar=password, width=31,fg='black',show='*',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t9.place(x=600, y=430, height=30)

l10 = Label(window, text="Confirm Password:", fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',11))
l10.place(x=450, y=484)
t10 = Entry(window, textvar=password1, width=31,fg='black',show='*',border=0,bg='#57a1f8',font=('Microsoft YaHei UI Light',11))
t10.place(x=600, y=480, height=30)

btn = Button(window, text="Register",width=20,pady=7,bg='#57a1f8',fg='white',border=0,cursor="hand2", command=insert)
btn.place(x=450, y=534)

window.mainloop()