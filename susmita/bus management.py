import os
import sys
from tkinter import*
import tkinter.messagebox
 
class bus_login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("700x450")
        self.root.title("Bus Management System Login ")
        self.root.configure(background="#737373")
        
        Title = Label(self.root,text="                    Bus Management System Login                       ",font=("times",20,"bold"),bg="black",fg="White",relief=GROOVE)
        Title.place(x=12,y=10)
 
        login_frame =Frame(root,bg="black", bd=5, width=300, height=200,padx=1,relief=GROOVE)
        login_frame.place(x=195,y=120)
 
        def authenticate(username, password):
            if len(username)!=0 and len(password)!=0:
                if username == "Username" and password == "Password":
                    tkinter.messagebox.showinfo("Bus Management System Login","Welcome")
                    root.destroy()
                    return
                else:
                    tkinter.messagebox.showerror("Bus Management System Login","Invalid username or password!")
                    self.txt_Password
                    return
            elif(len(username)==0):
                tkinter.messagebox.showerror("Bus Management System Login","Please enter username!")
                self.txt_username
                return
            else:
                tkinter.messagebox.showerror("Bus Management System Login","Please enter password!")
                self.txt_Password
                return
 
        
        def exit():
            exit=tkinter.messagebox.askyesno("Bus Management System Login","You want to exit.")
            if exit >0:
                root.destroy()
                return
 
        self.lbl_username=Label(login_frame,font=('times',10,'bold'),text="Username:",bg="black",fg="white")
        self.lbl_username.place(x=20,y=10)
        self.txt_username=Entry(login_frame,bg="black",fg="white")
        self.txt_username.place(x=100,y=10)
 
        self.lbl_Password=Label(login_frame,font=('times',10,'bold'),text="Password :",bg="black",fg="white")
        self.lbl_Password.place(x=20,y=40)
        self.txt_Password=Entry(login_frame,bg="black",fg="white")
        self.txt_Password.place(x=100,y=40)
 
        self.btn_exit=Button(login_frame,text='Exit',font=('times',10,'bold'),bg="black",fg="white",width=7,bd=2,relief=GROOVE,command=exit)
        self.btn_exit.place(x=170,y=130)
 
        self.btn_login=Button(login_frame,text='Log In',font=('times',10,'bold'),bg="black",fg="white",width=7,bd=2,relief=GROOVE,command=lambda:authenticate(self.txt_username.get(), self.txt_Password.get()))
        self.btn_login.place(x=50,y=130)
        
       
if __name__ =='__main__':
    root = Tk()
    application = bus_login(root)
    root.mainloop()