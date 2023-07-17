#import customtkinter as ctk #pip install customtkinter in the terminal
#from tkinter import * #shortcut - so it would not require to declare tkinter in every declaration of widgets
import tkinter as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os


def check_account(username):
    with open('user_info.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == f"Username: {username}":
                return True
    return False


def login():
    username = window.entry_field.get()
    password = window.entry_passfield.get()

    if check_account(username):
        messagebox.showinfo(title="Complete", message="Login complete.")
    else:
        messagebox.showinfo(title="Complete", message="Account not registered.")


def register():
    os.system("python register.py")

#create window
window = ttk.Tk()
window.title('Login System')# title the mainwindow
window.geometry('1000x650')
window.bind('<Escape>', lambda event: window.quit())#set escape as exit window

style = ttk.Style()


def frame_2():
    #create of frame where the widgets will be placed
    frame2 = ttk.Frame( master = window,width=200, bg = '#6387f2')
    frame2.pack(side='left', fill=ttk.BOTH,expand=ttk.YES)#place/display the frame

    start_mess = ttk.Label(frame2, text='Start your',bg = '#6387f2', fg='#ffffff', font=('montserrat', 20, 'bold'))
    with_mess = ttk.Label(frame2, text='Journey with us',bg = '#6387f2', fg='#ffffff', font=('montserrat', 20, 'bold'))
    create_mess = ttk.Label(frame2, text='create an account and Join our community',bg = '#6387f2', fg='#ffffff', font=('montserrat', 10))

    image = Image.open("SELL.png")
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(frame2, image=photo, bg='#6387f2')
    label.place(x=100, y=80)

    #place
    start_mess.place(x=50,y=300)
    with_mess.place(x=50,y=350)
    create_mess.place(x=50,y=400)


def frame_1():
    global entry_field, entry_passfield
    #frame 1
    frame1 = ttk.Frame( master = window,bg = '#FFFFFF', width=400)
    frame1.pack(side='right', anchor='n', fill=ttk.BOTH, expand=ttk.TRUE)#place/display the frame

    #creation of widgets
    login_label = ttk.Label(frame1, text='Welcome to Sellify',bg = '#FFFFFF', fg='#6387f2', font=('montserrat', 25, 'bold'))
    entry_label = ttk.Label(frame1, text='Username',bg = '#FFFFFF', fg='BLACK', font=('montserrat', 12))
    entry_field = ttk.Entry(frame1, width=25,font=('montserrat',12,),highlightcolor='#6387f2', highlightthickness=2)
    pass_label = ttk.Label(frame1, text='Password',bg = '#FFFFFF', fg='BLACK', font=('montserrat', 12))
    entry_passfield = ttk.Entry(frame1, show='*', width=25, font=('montserrat', 12),highlightcolor='#6387f2', highlightthickness=2)
    login_button = ttk.Button(frame1, text='   Login  ',width=27, bg = '#6387f2',foreground='#FFFFFF', font=('montserrat', 12),activebackground= '#4973f2',activeforeground='#a9a9a9', highlightbackground= 'BLACK',height=2,command=login)
    reg_button = ttk.Button(frame1, text='Register',foreground='#6387f2',highlightcolor='#ffffff',highlightthickness=3,highlightbackground='#ffffff', bg = '#ffffff',width=27, font=('montserrat', 12), command=register)



    #placing/displaying all the widget
    login_label.place(x= 125,y=130)
    entry_label.place(x= 150,y=205)
    pass_label.place(x= 150,y=285)
    entry_field.place(x= 155,y=240)
    entry_passfield.place(x= 155,y=320)
    login_button.place(x= 155,y=380)
    reg_button.place(x= 155,y=450)



frame_1()
frame_2()

window.mainloop() #looping of window so it would display


#master - will be the parent of that widget
#bg - color
#fg - font color
#title - window
#.geometry - size of window
#.configure - can be used to modify the widgets
#.Frame - frame equivalen to jframe in java
#Entry - Entry field same as jtext field
#Label - Label same as jlabel
#Button - button
#.grid - arrangement
#pack() - for displaying the widgets and frame/ like setVisible in java
#StringVar() = can store the same variable