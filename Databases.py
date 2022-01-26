from tkinter import *

from User import User


def login(username, password):
   user = Userz()
   if user.lgn(username, password) == True:
       print("Login Successful")
       root.withdraw()


root = Tk()
root.geometry("1000x600")
root.configure(background='white')
root.resizable(0, 0)
# app = Login(root)
Label(bg="#4687FB", height=40, width=70).place(x=0, y=0)
Label(bg="white", height=1, width=70).place(x=0, y=545)
Label(bg="#64E8FF", height=5, width=70).place(x=0, y=550)
l1 = Label(bg="#4687FB", anchor=CENTER, fg="white", text="CANVAS", font=('lucida sans unicode', 34), height=2,
          width=8).place(x=100, y=200)
username = Entry(fg='black', bd=2, font=('lucidasansunicode'))
username.place(x=580, y=250)
password = Entry(fg='black', bd=2, font=('lucidasansunicode'),show="*")
password.place(x=580, y=300)
Button(command=lambda:login(username.get(), password.get()),text="Login", bg='#4687FB', fg='white', bd=0, height=1, width=12, font=('lucidatypewriter', 11)).place(x=580,
                                                                                                             y=350)
root.mainloop()


def main():
   print("hi")

main()
# button = tk.Button(root, text="Login", bg='#4687FB', fg='white', bd=0, )
# button.pack()
