from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from scipy.io import wavfile
from scipy.fftpack import fft
import wave
import numpy
import math
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav


class EmotionProcessor(object):
    def __init__(self, fname):
        self.fname= fname
        


    def __enter__(self):
        return self
    def __exit__(self, exception, value, traceback):
        self.close()

#mfccProc: extracts the MFCCs from given audio
# Creates 2d arrays for storage of the fbank feature, mfcc features
#   and the delta of MFCC features
    def mfccProc(self):
        (rate,sig) = audioBasicIO.readAudioFile(self.fname)
        #Create 2d array for MFCC features
        mfcc_feat = mfcc(sig,samplerate = 44100, nfft = 1103)
        #Create 2d array for the delta of MFCC features
        d_mfcc_feat = delta(mfcc_feat, 2)
        #Create 2d array for the log of fbank features
        fbank_feat = logfbank(sig,rate)
        
        #print statements for debug process
##        print("MFCC (tone) Metrics:")
##        print(fbank_feat[0])
##        print(mfcc_feat[0])
##        print(d_mfcc_feat[0])
        return(mfcc_feat)
    
        
    def pitchProc(self):
        [Fs,x] = audioBasicIO.readAudioFile(self.fname)
        info=audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
        return info[0][1]
		
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
        return(freqArray)
