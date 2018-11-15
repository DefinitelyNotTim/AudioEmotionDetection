#Create Yes or No or Cancel Box in Python GUI Application
#This GUI asks the user if they want to save the recorded audio

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mbox

app = tk.Tk()
#Title for the GUI
app.title("Save Audio Recording")

#lable for the box

ttk.Label(app, text = "Would you like to save your box needs to be connected..").grid(column=0,row=0,padx = 20,pady = 30)

#Create a Menu Bar
# the lower code is the pop window when we hit the record button.needs to be connected
#should just be a small edit on the command = ??
#copy paste the rest... wanted everyone to see how it worked.

menuBar = Menu(app)
app.config(menu=menuBar)

#display a Yes or No or Cancel Box
def _msgBox():
    mbox.askyesnocancel('Yes or No or Cancel action Box', 'Choose the Action')
#create the message menu
msgMenu = Menu(menuBar, tearoff=0)
msgMenu.add_command(label= "Close", command =_msgBox)
menuBar.add_cascade(label = "File", menu=msgMenu)
app.mainloop()
