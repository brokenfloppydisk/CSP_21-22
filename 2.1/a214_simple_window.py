#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.messagebox as mb

uname = "admin"
pwd = "SuperSecretPassword123!"

def test_my_button():
    frame_auth.tkraise()

def check_login():
    entered_uname = str(ent_uname.get())
    entered_pwd = str(ent_pass.get())

    if (entered_uname==uname and entered_pwd==pwd):
        frame_auth.tkraise()
        lbl_success.config(text=("Password: " + entered_pwd))
    else:
        mb.showinfo("Login Failed","Incorrect Credentials Entered")
        

# main window
root = tk.Tk()
root.title("Authorization")
root.wm_geometry("200x150")

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_uname = tk.Label(frame_login, text="Username:")
lbl_uname.pack()

ent_uname = tk.Entry(frame_login, bd=3)
ent_uname.pack(pady=5,padx=35)

lbl_pass = tk.Label(frame_login, text="Password:")
lbl_pass.pack(padx=35)

ent_pass = tk.Entry(frame_login, bd=3)
ent_pass.pack(pady=5, padx=35)

btn_login = tk.Button(frame_login, text="Login", command=check_login)
btn_login.pack(pady=5, padx=35)

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_success = tk.Label(frame_auth, text="Password: ")
lbl_success.pack()

frame_login.tkraise()

root.mainloop()