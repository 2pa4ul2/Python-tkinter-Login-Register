#import customtkinter as ctk #pip install customtkinter in the terminal
#from tkinter import * #shortcut - so it would not require to declare tkinter in every declaration of widgets
import tkinter as ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def login():
   username = 'paul'
   password = 'paul'
   if username == entry_field.get() and password == entry_passfield.get():
        messagebox.showinfo(title= "Complete", message="Login complete.")
   else:
        messagebox.showinfo(title= "Complete", message="Login incomplete.")

#create window
window = ttk.Tk()
window.title('Login System')# title the mainwindow

window_width = 1280
window_height = 720
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width/2-window_width/2)
top = int(display_height/2-window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

window.configure(bg = '#0b0c10') #color
window.minsize(1280,720) #set minsize
window.resizable('false','false')
window.bind('<Escape>', lambda event: window.quit())#set escape as exit window

#create of frame where the widgets will be placed
frame1 = ttk.Frame( master = window,bg = '#1f2533', width=650)
frame1.pack(side='right', anchor='n', fill=ttk.BOTH, expand=ttk.TRUE)#place/display the frame
frame2 = ttk.Frame( master = window,bg = '#84ceeb')
frame2.pack(side='left', fill=ttk.BOTH, expand=ttk.YES)#place/display the frame

#creation of widgets
login_label = ttk.Label(frame1, text='Login Account',bg = '#1f2533', fg='#ffffff', font=('montserrat', 40, 'bold'))
entry_label = ttk.Label(frame1, text='Username',bg = '#1f2533', fg='#ffffff', font=('montserrat', 16))
entry_field = ttk.Entry(frame1, font=('montserrat', 16,))
pass_label = ttk.Label(frame1, text='Password',bg = '#1f2533', fg='#ffffff', font=('montserrat', 16))
entry_passfield = ttk.Entry(frame1, show='*', font=('montserrat', 16))
login_button = ttk.Button(frame1, text='   Login  ', bg = '#66fcf1', font=('montserrat', 16), command=login)
reg_button = ttk.Button(frame1, text='Register', bg = '#fff', font=('montserrat', 16), command=login)

entry_field.config()

#placing/displaying all the widget
login_label.pack(pady=80)
entry_label.pack(pady=10)
entry_field.pack()
pass_label.pack(pady=10)
entry_passfield.pack()
login_button.pack(pady=20)
reg_button.pack()

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