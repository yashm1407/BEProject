from tkinter import *
from tkinter import messagebox as ms
from PIL import ImageTk 
import sqlite3

class login_system:
    def __init__(self,root):
        self.root = root
        self.root.title("log in ")
        self.root.geometry('925x500+200+200')
        self.root.configure(bg='#fff')
        self.root.resizable(False,False)

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.bg1_icon=ImageTk.PhotoImage(file=r'login.png')
        Label(self.root,image=self.bg1_icon,bg='white').place(x=50,y=120)

        login_frame = Frame(self.root,width=350,height=350,bg='white')
        login_frame.place(x=480,y=70)

        title=Label(login_frame, text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        title.place(x=100,y=5)
        def on_enter(e):
            txtuser.delete(0,'end')
        
        def on_leave(e):
            name=txtuser.get()
            if name=='':
                txtuser.insert(0,'Username')
        
        txtuser=Entry(login_frame,textvariable=self.username,width=31,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        txtuser.place(x=30,y=80,height=30)
        txtuser.insert(0,'Username')
        txtuser.bind('<FocusIn>',on_enter)
        txtuser.bind('<FocusOut>',on_leave)

        def on_enter(e):
            txtpass.delete(0,'end')

        def on_leave(e):
            name=txtpass.get()
            if name=='':
                txtpass.insert(0,'Password')


        txtpass=Entry(login_frame,textvariable=self.password,width=31,fg='black',border=0,bg='white',show='*',font=('Microsoft YaHei UI Light',11))
        txtpass.place(x=30,y=150, height=30)
        txtpass.insert(0,'Password')
        txtpass.bind('<FocusIn>',on_enter)
        txtpass.bind('<FocusOut>',on_leave)

        Button(login_frame,width=20,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=self.login,cursor="hand2").place(x=30,y=204)
       
    def login(self):
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()
        db = sqlite3.connect('evaluation.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                       "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            msg = ""
            ms.showinfo("messege", "Login sucessfully")
            root.destroy()
            from subprocess import call
            call(['python','upload.py'])
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')
        
    def new_user(self):
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created Successfully !')
            self.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

    def registration(self):
        root.destroy()
        from subprocess import call
        call(["python", "registration.py"])

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
root = Tk()
obj = login_system(root)
root.mainloop()