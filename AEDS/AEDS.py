from tkinter import *
import tkinter as tk
import pyaudio
import Recording
import emotionProcessor
from tkinter import Menu
from tkinter import messagebox as mbox
import scikit_network
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
       
        self.startButton = Button(self, text = " Start: recording          " , justify = "center", command = self.recordAudio, bg = "lightgray")
        self.startButton.grid(row = 0, column = 0)
        
        # Stop button is added.
        
        self.stopButton = Button(self, text = " Stop: recording          " , justify = "center", command = self.endAudio, bg ="lightgray")
        self.stopButton.grid(row = 1, column = 0)
        
        
        # Label for the output below "user Id or name".
            
        self.label = Label(self, text = "User Name:               ", font = 13, justify = "left")
        self.label.grid(column = 1, row = 0)
    
        #output for the User id that is either chosen after the emotion is processed or just chosen still an option we are deciding on.
        self.user = StringVar()
        self.txt = Entry(self, textvariable = self.user, width = 32)
        self.txt.grid(column = 1, row = 1)
            
        # Label for the GUI that Says " predicted emotion".        
        self.label = Label (self, text = "Predicted Emotion:    ",font = 13, justify = "left")
        self.label.grid(column = 1, row = 2)
        
        # Output field for the label where the predicted emotion will be added when the NN processed the audio matrics hopefully correctly. 
        self.emotionalPrediction = StringVar()
        self.text = Entry(self, textvariable = self.emotionalPrediction, width = 32)
        self.text.grid(column = 1, row = 3)

        
        
    def recordAudio(self):
        self.recorder=Recording.Recording(wave_output_filename, CHANNELS, RATE, CHUNK)
        self.recorder.startAudio()
        self.emotionalPrediction.set("Recording...")
        return self
    # End audio also needs a popup button.
    
    def endAudio(self):
        self.recorder.stopAudio()
        self.emotionalPrediction.set(" ")

        pitch = self.processor.pitchProc()
        pitch = stdev(pitch)
        
        volume = self.processor.volumeProc()
        print(volume)
        volume = stdev(volume)
        
        tone = self.processor.mfccProc()
        dev_array = []
        for i in tone:
            temp = stdev(i)
            dev_array.append(temp)
        tone = stdev(dev_array)
        
        wordGap = self.processor.gapProc()
        if(len(wordGap) != 0):
            wordGaplen = len(wordGap)
            wordGap = stdev(wordGap)
        else:
            wordGaplen = 0
            wordGap = 0
            
        user_profile = np.array([pitch, tone, volume, wordGap, wordGaplen])
        
        predicted = scikit_network.compare_new(user_profile)
        self.emotionalPrediction.set(predicted[0])
        
        return self
    


# Modify root window.
root = Tk()
root.title("Audio Control Interface")

# The size of the whole frame.

root.geometry ("300x158") 

# Background for the whole GUI

app = Application(root)

#kick off the event loop
root.mainloop()

