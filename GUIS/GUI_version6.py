#Gui interface for Audio Emotional detection program CSC-450 Team:1.
#All needed lib's are below most need pip install. 

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

# Hardcoded Variables 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
wave_output_filename = "test.wav"

# Code to create the window for the GUI.
# this class sets up the frame which is the entire window needed to fit the GUI buttons and lable's inside.

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(column = 1, row = 5)
               
        self.create_widgets()
        self.recorder=Recording.Recording(wave_output_filename, CHANNELS, RATE, CHUNK)
        self.processor=emotionProcessor.EmotionProcessor(wave_output_filename)
    
   # class widgets.. this is where the code for each off six buttons two lable's and two text boxes are held.
   # Grid not pack is used.
   # grid= where is that button on lable located in the frame.
   # each button has a command atribute that connects the button with a function that controls what the button does.
   
    def create_widgets(self):
       
        #Start button is added. 
       
        self.startButton = Button(self, text = " Start: recording          " , justify = "center", command = self.recordAudio, bg = "lightgray",fg ="green")
        self.startButton.grid(row = 0, column = 0)
        
        # Stop button is added.
        
        self.stopButton = Button(self, text = " Stop: recording          " , justify = "center", command = self.endAudio, bg ="lightgray",fg = "red")
        self.stopButton.grid(row = 1, column = 0)
        
        #Play Recording button is added.
        
        self.playButton = Button(self, text = "Play Recorded Audio", justify = "center", command = self.playAudio, bg = "lightgray",fg = "green")
        self.playButton.grid(row = 2 , column = 0)
        
        #Save button is added.

        self.saveButton = Button (self, text = "Save Audio                 ", justify = "center", command = self.saveAudio, bg = "lightgray")
        self.saveButton.grid(row = 3, column = 0)
        
        #Button for Delete Audio.
        
        self.deleteButton = Button (self,text = "Delete Audio              ", justify = "center", command = self.deleteAudio, bg = "lightgray",fg = 'black')
        self.deleteButton.grid(row = 4, column = 0)
        
        #Button for Process Emotion. 
        
        self.processButton = Button(self,text = "Process Emotion       ", justify = "center", command = self.processAudio,bg = "lightgray", fg = "blue")
        self.processButton.grid(row = 5, column = 0)

        # Label for the output below "user Id or name".
            
        self.label = Label(self, text = "User Name:               ", font = 13, justify = "left",bg ="green2")
        self.label.grid(column = 1, row = 0)
    
        #output for the User id that is either chosen after the emotion is processed or just chosen still an option we are deciding on.
        
        self.txt = Entry(self, textvariable = user, width = 32)
        self.txt.grid(column = 1, row = 1)
            
        # Label for the GUI that Says " predicted emotion".        
        self.label = Label (self, text = "Predicted Emotion:    ",font = 13, justify = "left",bg = "green2")
        self.label.grid(column = 1, row = 2)
        
        # Output field for the label where the predicted emotion will be added when the NN processed the audio matrics hopefully correctly. 
        
        self.text = Entry(self, textvariable = emotionalPrediction, width = 32)
        self.text.grid(column = 1, row = 3)

        chk_state = BooleanVar()
        # Set the state of the check button.
        chk_state.set(True) 
        chk = Checkbutton(self, text='Check To Train Emotion', var=chk_state)
        chk.grid(column = 1, row = 4)
        
        
        # This is a pop to make sure if the check box for training the emotion (if the predictied emiotion is not correct) this should tell the NN that the classification isn't correct.  
        
        if chk_state == True:
            menuBar = Menu(app)
            app.config(menu=menuBar)
            mbox.askyesnocancel('Yes or No or Cancel action Box', 'Is Predicted Emotion True?')
            msgMenu = Menu(menuBar, tearoff=0)
            msgMenu.add_command(label= "Close", command =_msgBox)
            menuBar.add_cascade(label = "File", menu=msgMenu)
            app.mainloop()
                   
        # attaching the command of each button to the correct function that needs to fire when a button is pressed.
        #additonal popup is used below for Record Audio button on the GUI above.

    def recordAudio(self):
        self.recorder.startAudio()
        app = tk.Tk()
        menuBar = Menu(app)
        app.config(menu=menuBar)
        mbox.askyesnocancel('Yes or No or Cancel action Box', 'Choose the Action')
        msgMenu = Menu(menuBar, tearoff=0)
        msgMenu.add_command(label= "Close", command =_msgBox)
        menuBar.add_cascade(label = "File", menu=msgMenu)
        app.mainloop()
        return self
    # End audio also needs a popup button.
    
    def endAudio(self):
        self.recorder.stopAudio()
        app = tk.Tk()
        menuBar = Menu(app)
        app.config(menu=menuBar)
        mbox.askyesnocancel('Yes or No or Cancel action Box', 'Choose the Action')
        msgMenu = Menu(menuBar, tearoff=0)
        msgMenu.add_command(label= "Close", command =_msgBox)
        menuBar.add_cascade(label = "File", menu=msgMenu)
        app.mainloop()
        return self
    
    # Calling fuctions for each button on the GUI.
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



# Modify root window.
root = Tk()
root.title("Audio Control Interface")

# The size of the whole frame.

root.geometry ("325x158") 

# Background for the whole GUI

root["bg"] = "green2"
app = Application(root)

#kick off the event loop
root.mainloop()

