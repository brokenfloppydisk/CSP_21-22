# a213_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restricted app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "What was the name of your high school?"
answer = "CAMS"
my_auth.set_authentication(question, answer)
user = "admin"
passw = "Sup3rStr0ngP@ssw0rd9000"
my_auth.set_authorization(user, passw)

# start the GUI
my_auth.mainloop()
