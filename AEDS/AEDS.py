#Gui interface for Audio Emotional detection program CSC-450 Michael Knapp

from tkinter import *
import tkinter as tk
import pyaudio
import Recording
import emotionProcessor
import scikit_network
from tkinter import Menu
from tkinter import messagebox as mbox
from statistics import stdev
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
wave_output_filename = "test.wav"

# create the window for the GUI
# this class sets up the frame which is the entire window needed to fit the GUI buttons and lable's inside.

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(column = 1, row = 5)
        #self.Style().configure(background = "green")
        
        self.create_widgets()
        self.recorder=Recording.Recording(wave_output_filename, CHANNELS, RATE, CHUNK)
        self.processor=emotionProcessor.EmotionProcessor(wave_output_filename)
    
   # class widgets.. this is where the code for each off six buttons two lable's and two text boxes are held.
   # .pack()= makes the button fit to the entire collumn not just the size of the text inside the button.
   # grid= where is that button on lable located in the frame.
   # each button has a command atribute that connects the button with a function that controls what the button does.
   
    def create_widgets(self):
        self.startButton = Button(self, text = " Start: recording          " , justify = "center", command = self.recordAudio, bg = "lightgray",fg ="green")
        self.startButton.grid(row = 0, column = 0)

        self.stopButton = Button(self, text = " Stop: recording          " , justify = "center", command = self.endAudio, bg ="lightgray",fg = "red")
        self.stopButton.grid(row = 1, column = 0)
        
        self.playButton = Button(self, text = "Play Recorded Audio", justify = "center", command = self.playAudio, bg = "lightgray",fg = "green")
        self.playButton.grid(row = 2 , column = 0)

        self.saveButton = Button (self, text = "Save Audio                 ", justify = "center", command = self.saveAudio, bg = "lightgray")
        self.saveButton.grid(row = 3, column = 0)

        self.deleteButton = Button (self,text = "Delete Audio              ", justify = "center", command = self.deleteAudio, bg = "lightgray",fg = 'black')
        self.deleteButton.grid(row = 4, column = 0)

        self.processButton = Button(self,text = "Process Emotion       ", justify = "center", command = self.processAudio,bg = "lightgray", fg = "blue")
        self.processButton.grid(row = 5, column = 0)


        self.label = Label(self, text = "User Name:               ", font = 13, justify = "left",bg ="green2")
        self.label.grid(column = 1, row = 0)

        
        self.txt = Entry(self, width = 32)
        self.txt.grid(column = 1, row = 1)
        #not sure who put this in here but I removed them because we shouldn't need more than user at a time. 
        #this goes for both lable and entry box. 
        
        #self.label = Label(self, text = "User Name:")
        #self.label.grid(column = 2, row = 0)

        #self.text = Entry(self, width = 20)
        #self.text.grid(column = 3, row = 0)
        
        self.label = Label (self, text = "Predicted Emotion:    ",font = 13, justify = "left",bg = "green2")
        self.label.grid(column = 1, row = 2)

        self.text = Entry(self, width = 32)
        self.text.grid(column = 1, row = 3)

        chk_state = BooleanVar()
        chk_state.set(True) #set the state of the check button
        chk = Checkbutton(self, text='Check To Train Emotion', var=chk_state)
        chk.grid(column = 1, row = 4)

        if chk_state == True:
            menuBar = Menu(app)
            app.config(menu=menuBar)
            mbox.askyesnocancel('Yes or No or Cancel action Box', 'Is Predicted Emotion True?')
            msgMenu = Menu(menuBar, tearoff=0)
            msgMenu.add_command(label= "Close", command =_msgBox)
            menuBar.add_cascade(label = "File", menu=msgMenu)
            app.mainloop()
            
        # this is a pop to make sure if the check box for training the emotion (if the predictied emiotion is not correct) this should tell the NN that the classification isn't correct.  
        
        
        
# attaching the command of each button to the correct function that needs to fire when a button is pressed.
#can't test any further until the fuctions self.recorder.startAudio() errors because these are not valid functions yet.
# added pop window functions for recordAudio fuction adn the endAudio fuction. code that was pasted is at he bottom commented out just in case there are problems testing this that.../n
#            ....way we can go back and figure what is incorrect.  please leave this for now.
    def recordAudio(self):
        self.recorder.startAudio()
        app = tk.Tk()
        app.mainloop()
        return self
    def endAudio(self):
        self.recorder.stopAudio()
        app = tk.Tk()
        app.mainloop()
        return self
    def processAudio(self):
        pitch = self.processor.pitchProc()
        pitch = stdev(pitch)
        volume = self.processor.volumeProc()
        volume = stdev(volume)
        tone = self.processor.mfccProc()
        wordGap = self.processor.gapProc()
        dev_array = []
        for i in tone:
            temp = stdev(i)
            dev_array.append(temp)
        tone = stdev(dev_array)
        if(len(wordGap) != 0):
            wordGaplen = len(wordGap)
            wordGap = stdev(wordGap)
        else:
            wordGaplen = 0
            wordGap = 0
        user_profile = np.array([pitch, tone, volume, wordGap, wordGaplen])
        predicted = scikit_network.compare_new(user_profile)
        print(predicted)
        return self
    def playAudio(self):
        return self
    def saveAudio(self):
        return self
    def deleteAudio(self):
        return self
# all of this is part of the popwindow code added to endAudio function and the recordAudio buttons (left it here to make sure if we need to add another one you can cut and paste.       
"""menuBar = Menu(app)
app.config(menu=menuBar)

#display a Yes or No or Cancel Box
def _msgBox():
    mbox.askyesnocancel('Yes or No or Cancel action Box', 'Choose the Action')
#create the message menu
msgMenu = Menu(menuBar, tearoff=0)
msgMenu.add_command(label= "Close", command =_msgBox)
menuBar.add_cascade(label = "File", menu=msgMenu)
app.mainloop()"""




#modify root window
root = Tk()
root.title("Audio Control Interface")
root.geometry ("325x158") # the size of the whole frame
root["bg"] = "green2"
app = Application(root)

#kick off the event loop
root.mainloop()

