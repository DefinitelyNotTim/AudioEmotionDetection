#Gui interface for Audio Emotional detection program CSC-450 Michael Knapp

from tkinter import *

#create the window for the GUI


class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(column = 2, row = 5)
        self.create_widgets()
        #self.
    

    def create_widgets(self):
        self.button1 = Button(self, text = " Start recording    " , justify = "left",)
        self.button1.grid()
        

        self.button2 = Button(self, text = "Play Recorded Audio", justify = "left")
        self.button2.grid()

        self.button3 = Button (self, text = "Save Audio    ", justify = "left")
        self.button3.grid()

        self.button4 = Button (self,text = "Delete Audio   ", justify = "left")
        self.button4.grid()

        self.button5 = Button(self,text = "Process Emotion  ", justify = "left")
        self.button5.grid()

        self.txt = Entry(self, width = 20)
        self.txt.grid(column = 2, row = 0)

        self.label = Label(self, text = "User Name")
        self.label.grid(column = 1, row = 0)
        
        

#modify root window
root = Tk()
root.title("Audio Control GUI")
root.geometry ("300x200")
app = Application(root)

#kick off the event loop
root.mainloop()

