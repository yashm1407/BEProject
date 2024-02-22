from tkinter import *
from tkinter import messagebox as ms


root=Tk()
root.title('Image And Text Deduplication')
root.geometry('925x500+200+200')
root.configure(bg='#fff')
root.resizable(False,False)

def Login():
    from subprocess import call
    call(["python","Login1.py"])

def Register():
    from subprocess import call
    call(["python","registration.py"])

heading1=Label(root,text='File Encryption System',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading1.place(x=300,y=30)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=100)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Welcome',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23))
heading.place(x=110,y=100)

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=Login).place(x=35,y=150)
Button(frame,width=39,pady=7,text='Register',bg='#57a1f8',fg='white',border=0,command=Register).place(x=35,y=190)

root.mainloop()