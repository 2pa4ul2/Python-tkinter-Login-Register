#import customtkinter as ctk #pip install customtkinter in the terminal
#from tkinter import * #shortcut - so it would not require to declare tkinter in every declaration of widgets
import tkinter as ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def register():
    # Get input values
    first_name = Fname_entry.get()
    last_name = Lname_entry.get()
    username = entry_user.get()
    password = entry_passfield.get()

    # Validate input values
    if not first_name or not last_name or not username or not password:
        messagebox.showinfo(title="Incomplete", message="Please fill in all fields.")
        return

    # Create a text file with the input information
    try:
        with open('user_info.txt', 'w') as file:
            file.write(f"First Name: {first_name}\n")
            file.write(f"Last Name: {last_name}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")
        messagebox.showinfo(title="Complete", message="Registration complete. User info saved.")
    except Exception as e:
        messagebox.showinfo(title="Error", message="An error occurred while saving user info.")

#create window
window = ttk.Tk()
window.title('Login System')# title the mainwindow
window.geometry('1000x650')
window.bind('<Escape>', lambda event: window.quit())#set escape as exit window


#create of frame where the widgets will be placed
frame1 = ttk.Frame(master = window,bg = '#84ceeb')
frame1.pack(side='right', anchor='n', fill=ttk.BOTH, expand=ttk.TRUE)#place/display the frame
frame2 = ttk.Frame(  master = window,bg = '#1f2533', width=650)
frame2.pack(side='left', fill=ttk.BOTH, expand=ttk.YES)#place/display the frame

#creation of widgets
login_label = ttk.Label(frame2, text='Register Account',bg = '#1f2533', fg='#ffffff', font=('montserrat', 40, 'bold'))

Fname_label = ttk.Label(frame2, text='First',bg = '#1f2533', fg='#ffffff', font=('montserrat', 16))
Fname_entry = ttk.Entry(frame2, font=('montserrat', 16,))
Lname_label = ttk.Label(frame2, text='Last',bg = '#1f2533', fg='#ffffff', font=('montserrat', 16))
Lname_entry = ttk.Entry(frame2, font=('montserrat', 16,))

entry_label = ttk.Label(frame2, text='Username',bg = '#1f2533', fg='#ffffff', font=('montserrat', 16))
entry_user = ttk.Entry(frame2, font=('montserrat', 16,))
pass_label = ttk.Label(frame2, text='Password',bg = '#1f2533', fg='#ffffff', font=('montserrat', 16))
entry_passfield = ttk.Entry(frame2, show='*', font=('montserrat', 16))
reg_button = ttk.Button(frame2, text='Register', bg = '#fff', font=('montserrat', 16), command=register)


#placing/displaying all the widget
login_label.pack(pady=30)
Fname_label.pack(pady=10)
Fname_entry.pack()
Lname_label.pack(pady=10)
Lname_entry.pack()
entry_label.pack(pady=10)
entry_user.pack()
pass_label.pack(pady=10)
entry_passfield.pack()
reg_button.pack(pady=20)

window.mainloop() #looping of window so it would display