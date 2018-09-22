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

class Recording(object):
    def __init__(self, fname, channels, rate, CHUNK):
        self.fname= fname
        self.channels=channels
        self.rate=rate
        self.CHUNK=CHUNK
        self._p = pyaudio.PyAudio()
        self.wavefile = self._prep_file(self.fname)
        self._stream = None

    #I'm not sure sure what these next two functions are for unless they have something to do with creating and destroying the object, they never seem to run. However, when I was looking into how to do this callback online this is how they recommended that I organize the code


    def __enter__(self):
        return self
    def __exit__(self, exception, value, traceback):
        self.close()
        
    def startAudio(self):
        

        self._stream = self._p.open(format=pyaudio.paInt16,channels= self.channels,rate=self.rate,input=True,frames_per_buffer=self.CHUNK, stream_callback=self.get_callback())
        print("recording...")

        self._stream.start_stream()
        return self
    def stopAudio(self):
        self._stream.stop_stream()
        print("done recording")
        return self
    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    
    def close(self):
        self._stream.close()
        self._p.terminate()
        self.waveFile.close()
        

    def _prep_file(self, fname):
        waveFile = wave.open(wave_output_filename,'wb')
        waveFile.setnchannels(self.channels)
        waveFile.setsampwidth(self._p.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(self.rate)
        return waveFile
    

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(column = 2, row = 5)
        self.create_widgets()
        self.recorder=Recording(wave_output_filename, CHANNELS, RATE, CHUNK)
        #self.
    

    def create_widgets(self):
        self.startButton = Button(self, text = " Start recording    " , justify = "left", command = self.recordAudio)
        self.startButton.grid()

        self.stopButton = Button(self, text = " Stop recording    " , justify = "left", command = self.endAudio)
        self.stopButton.grid()
        
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
        self.recorder.startAudio()
        return self
    def endAudio(self):
        self.recorder.stopAudio()
        return self
        
        
    


#modify root window
root = Tk()
root.title("Audio Control GUI")
root.geometry ("300x200")
app = Application(root)

#kick off the event loop
root.mainloop()

