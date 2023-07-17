#import customtkinter as ctk #pip install customtkinter in the terminal
#from tkinter import * #shortcut - so it would not require to declare tkinter in every declaration of widgets
import tkinter as ttk
from tkinter import messagebox
from PIL import Image, ImageTk

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
    global entry_user, entry_passfield,Lname_entry,Fname_entry
    #frame 1
    frame1 = ttk.Frame( master = window,bg = '#FFFFFF', width=400)
    frame1.pack(side='right', anchor='n', fill=ttk.BOTH, expand=ttk.TRUE)#place/display the frame

    #creation of widgets
    login_label = ttk.Label(frame1, text='Welcome to Sellify',bg = '#FFFFFF', fg='#6387f2', font=('montserrat', 25, 'bold'))

    Fname_label = ttk.Label(frame1, text='First Name',bg = '#FFFFFF', fg='BLACK', font=('montserrat', 12))
    Fname_entry = ttk.Entry(frame1, width=27,font=('montserrat',12,),highlightcolor='#6387f2', highlightthickness=2)

    Lname_label = ttk.Label(frame1, text='Last Name', bg='#FFFFFF', fg='BLACK', font=('montserrat', 12))
    Lname_entry = ttk.Entry(frame1, width=27, font=('montserrat', 12,), highlightcolor='#6387f2', highlightthickness=2)

    entry_label = ttk.Label(frame1, text='Username', bg='#FFFFFF', fg='BLACK', font=('montserrat', 12))
    entry_user = ttk.Entry(frame1, width=27, font=('montserrat', 12,), highlightcolor='#6387f2', highlightthickness=2)

    pass_label = ttk.Label(frame1, text='Password',bg = '#FFFFFF', fg='BLACK', font=('montserrat', 12))
    entry_passfield = ttk.Entry(frame1, show='*', width=27, font=('montserrat', 12),highlightcolor='#6387f2', highlightthickness=2)

    confirm_label = ttk.Label(frame1, text='Confirm Password',bg = '#FFFFFF', fg='BLACK', font=('montserrat', 12))
    confirm_pass = ttk.Entry(frame1, show='*', width=27, font=('montserrat', 12), highlightcolor='#6387f2',highlightthickness=2)

    login_button = ttk.Button(frame1, text='   Login  ',width=27, bg = '#6387f2',foreground='#FFFFFF', font=('montserrat', 12),activebackground= '#4973f2',activeforeground='#a9a9a9', highlightbackground= 'BLACK',height=2)
    reg_button = ttk.Button(frame1, text='Register',foreground='#6387f2',highlightcolor='#ffffff',highlightthickness=3,activebackground= '#4973f2',highlightbackground='#ffffff', bg = '#ffffff',width=27, font=('montserrat', 12))



    #placing/displaying all the widget
    login_label.place(x= 125,y=80)

    Fname_label.place(x= 150,y=140)
    Lname_label.place(x=150, y=200)
    entry_label.place(x=150, y=260)
    pass_label.place(x=150, y=320)
    confirm_label.place(x=150, y=380)

    Fname_entry.place(x= 150,y=170)
    Lname_entry.place(x= 150,y=230)
    entry_user.place(x= 150,y=290)
    entry_passfield.place(x= 150,y=350)
    confirm_pass.place(x=150, y=410)

    login_button.place(x= 150,y=450)
    reg_button.place(x= 149,y=510)



frame_1()
frame_2()

window.mainloop()