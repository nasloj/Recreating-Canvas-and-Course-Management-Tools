from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):

        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="User Login", command=self.user_login_btn)
        self.logbtn.grid(columnspan=2)
        self.logbtn2 = Button(self, text="Admin Login", command=self.admin_login_btn)
        self.logbtn2.grid(columnspan=2)

        self.pack()


    def user_login_btn(self):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "user" and password == "password1":
            New_Window = Tk("Welcome user!")
            New_Window.mainloop()
        elif  username != "user":
            tm.showerror("Incorrect Username")
        elif password != "password1":
            tm.showerror("Incorrect Password")
        else:
            tm.showerror("Login error", "Invalid User")

    def admin_login_btn(self):

        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "password2":
            New_Window = Tk("Welcome admin!")
            New_Window.mainloop()
        elif  username != "admin":
            tm.showerror("Incorrect Username")
        elif password != "password2":
            tm.showerror("Incorrect Password")
        else:
            tm.showerror("Login error", "Invalid User")


root = Tk()
lf = LoginFrame(root)
root.mainloop()