from tkinter import *
import os
import sqlite3 as sql
import pickle

# ********************* GUI WINDOWS **************************

# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250+500+300")
    main_screen.title("Account Login")
    Label(text="Welcome to Canvas!", bg="salmon", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()

    # comment this out after making admin
    # Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()

# Designing window for registration
def register():
    # initialize screen dimensions
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x400+500+300")

    # create global String variables
    global username
    global password
    global firstname
    global lastname
    global usertype

    username = StringVar()
    password = StringVar()
    firstname = StringVar()
    lastname = StringVar()
    usertype = StringVar()

    global username_entry
    global password_entry
    global firstname_entry
    global lastname_entry
    global usertype_entry

    # GUI labels and entries
    Label(register_screen, text="Please enter details below", bg="white").pack()
    Label(register_screen, text="").pack()

    firstname_label = Label(register_screen, text="First Name * ")
    firstname_label.pack()
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.pack()

    lastname_label = Label(register_screen, text="Last Name * ")
    lastname_label.pack()
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    usertype_lable = Label(register_screen, text="Student/Teacher * ")
    usertype_lable.pack()
    usertype_entry = Entry(register_screen, textvariable=usertype)
    usertype_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="white", command=register_user).pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Go Back", width=10, height=1, command=delete_register_screen).pack()
def login():
    # initialize screen dimensions
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300+500+300")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    # create global String variables
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    # GUI labels, entries, and buttons
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Cancel", width=10, height=1, command=delete_login_screen).pack()
def login():
    # initialize screen dimensions
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300+500+300")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    # create global String variables
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    # GUI labels, entries, and buttons
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Cancel", width=10, height=1, command=delete_login_screen).pack()
def chooseview():
    if (curr_user.accType == "Student"):
        student_view()
        print("student")
    elif (curr_user.accType == "Teacher"):
        teacher_view()
        print("teacher")
    elif (curr_user.accType == "Admin"):
        admin_view()
        print("admin")

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100+500+300")
    Label(password_not_recog_screen, text="Invalid Username or Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()

def delete_login_screen():
    login_screen.destroy()

def delete_register_screen():
    register_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_admin_view():
    admin_view_screen.destroy()

def delete_course_screen():
    course_screen.destroy()

def delete_addstudent_screen():
    addstudent_screen.destroy()

def delete_student_view():
    student_view_screen.destroy()

def delete_teacher_view():
    teacher_view_screen.destroy()

def delete_studentdashboard_screen():
    studentdashboard_screen.destroy()

def delete_teacherdashboard_screen():
    teacherdashboard_screen.destroy()

def delete_gradeinput_screen():
    gradeinput_screen.destroy()

def delete_studentgrade_screen():
    studentgrade_screen.destroy()

def delete_postassignment_screen():
    postassignment_screen.destroy()

def delete_postannouncement_screen():
    postannouncement_screen.destroy()

def delete_viewannouncement_screen():
    viewannouncement_screen.destroy()

def delete_addfile_screen():
    addfile_screen.destroy()

def delete_getfile_screen():
    getfile_screen.destroy()
