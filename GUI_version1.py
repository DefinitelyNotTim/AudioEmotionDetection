#Gui interface for Audio Emotional detection program CSC-450 Michael Knapp

from tkinter import *
import pyaudio
import Recording
import emotionProcessor

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
wave_output_filename = "test.wav"


#create the window for the GUI


class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(column = 2, row = 5)
        self.create_widgets()
        self.recorder=Recording.Recording(wave_output_filename, CHANNELS, RATE, CHUNK)
        self.processor=emotionProcessor.EmotionProcessor(wave_output_filename)
    

    def create_widgets(self):
        self.startButton = Button(self, text = " Start recording    " , justify = "left", command = self.recordAudio)
        self.startButton.grid()

        self.stopButton = Button(self, text = " Stop recording    " , justify = "left", command = self.endAudio)
        self.stopButton.grid()
        
        self.playButton = Button(self, text = "Play Recorded Audio", justify = "left", command = self.playAudio)
        self.playButton.grid()

        self.saveButton = Button (self, text = "Save Audio    ", justify = "left", command = self.saveAudio)
        self.saveButton.grid()

        self.deleteButton = Button (self,text = "Delete Audio   ", justify = "left", command = self.deleteAudio)
        self.deleteButton.grid()

        self.processButton = Button(self,text = "Process Emotion  ", justify = "left", command = self.processAudio)
        self.processButton.grid()

        self.txt = Entry(self, width = 20)
        self.txt.grid(column = 2, row = 0)

        self.label = Label(self, text = "User Name")
        self.label.grid(column = 1, row = 0)
        
        self.label = Label(self, text = "User Name:")
        self.label.grid(column = 2, row = 0)

        self.text = Entry(self, width = 20)
        self.text.grid(column = 3, row = 0)
        
        self.label = Label (self, text = "Emotion:")
        self.label.grid(column = 2, row = 1)

        self.text = Entry(self, width = 20)
        self.text.grid(column = 3, row = 1)

    def recordAudio(self):
        self.recorder.startAudio()
        return self
    def endAudio(self):
        self.recorder.stopAudio()
        return self
    def processAudio(self):
        self.processor.pitchProc()
        return self
    def playAudio(self):
        return self
    def saveAudio(self):
        return self
    def deleteAudio(self):
        return self
        
    


#modify root window
root = Tk()
root.title("Audio Control GUI")
root.geometry ("300x200")
app = Application(root)

#kick off the event loop
root.mainloop()

