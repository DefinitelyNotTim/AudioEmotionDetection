#Gui interface for Audio Emotional detection program CSC-450 Michael Knapp

from tkinter import *
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
record_seconds = 10
wave_output_filename = "test.wav"


#create the window for the GUI


class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(column = 2, row = 5)
        self.create_widgets()
        #self.
    

    def create_widgets(self):
        self.startButton = Button(self, text = " Start recording    " , justify = "left", command = self.recordAudio)
        self.startButton.grid()
        
        self.playButton = Button(self, text = "Play Recorded Audio", justify = "left")
        self.playButton.grid()

        self.saveButton = Button (self, text = "Save Audio    ", justify = "left")
        self.saveButton.grid()

        self.deleteButton = Button (self,text = "Delete Audio   ", justify = "left")
        self.deleteButton.grid()

        self.processButton = Button(self,text = "Process Emotion  ", justify = "left")
        self.processButton.grid()

        self.txt = Entry(self, width = 20)
        self.txt.grid(column = 2, row = 0)

        self.label = Label(self, text = "User Name")
        self.label.grid(column = 1, row = 0)
        
    def recordAudio(self):
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        print("recording...")

        frames = []

        for i in range (0, int(RATE/CHUNK*record_seconds)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("done recording")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        waveFile = wave.open(wave_output_filename,'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(p.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

#modify root window
root = Tk()
root.title("Audio Control GUI")
root.geometry ("300x200")
app = Application(root)

#kick off the event loop
root.mainloop()

