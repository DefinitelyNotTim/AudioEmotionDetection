
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from scipy.io import wavfile
from scipy.fftpack import fft
import wave
import numpy
import math

class EmotionProcessor(object):
    def __init__(self, fname):
        self.fname= fname
        


    def __enter__(self):
        return self
    def __exit__(self, exception, value, traceback):
        self.close()
        
    def pitchProc(self):
        [Fs,x] = audioBasicIO.readAudioFile(self.fname)
        info=audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
        print(info[0][1])
        return self
		
    def volumeProc(self):
        freq, snd = wavfile.read(self.fname)
        snd = snd/(2.**15)
        s1 = snd[:]
        n = len(s1)
        p = fft(s1) #take the fourier transform
        unique = int(math.ceil((n+1)/2.0))
        p = p[0:unique]
        p=abs(p)
        p = p/float(n)
        p=p**2
        if n%2>0:
            p[1:len(p)]=p[1:len(p)]*2
        else:
            p[1:len(p)-1]=p[1:len(p)-1]*2
        freqArray = numpy.arange(0,unique,1.0)*(freq/n)
        #numpy.set_printoptions(threshold = numpy.nan)
        #rms_val = sqrt(mean(s1**2))
        print(freqArray)
        return self
