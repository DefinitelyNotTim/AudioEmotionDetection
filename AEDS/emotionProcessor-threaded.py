## emotionProcessor-threaded.py
##	This is a variation of the emotionProcessor class.
##	The main difference between the two classes is that this
##		class utilizes python's threading module to collect the
##		audio metrics.
##	Since this proved to offer little to no performance gains
##		while still expending extra resources, this class was not
##		utilized in the final build of the software. This class
##		may, however, prove to be useful to future researchers
##		looking to improve the performance of the AEDS softare.
##	This class is included purely for educational purposes.
##	All alterations made to this class from emotionProcessor.py
##		were made by Timmothy Lane.

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
from pydub import AudioSegment
from pydub.silence import split_on_silence
from statistics import *
import numpy as np
import multiprocessing
from multiprocessing import *
import threading



class EmotionProcessor(object):
    def __init__(self, fname):
        self.fname= fname
        
    def __enter__(self):
        return self
    
    def __exit__(self, exception, value, traceback):
        self.close()

#mfccProc: extracts the MFCCs from given audio
# Written by Timmothy Lane
# Creates 2d arrays for storage of the fbank feature, mfcc features
#   and the delta of MFCC features
# Written By: Timmothy Lane
    def mfccProc(self):
        (rate,sig) = audioBasicIO.readAudioFile(self.fname)
        #Create 2d array for MFCC features
        mfcc_feat = mfcc(sig,samplerate = 44100, nfft = 1103)
        #Create 2d array for the delta of MFCC features
        d_mfcc_feat = delta(mfcc_feat, 2)
        #Create 2d array for the log of fbank features
        fbank_feat = logfbank(sig,rate)        
        return(mfcc_feat)


    def mfccProc2(self, results_dict):
        (rate,sig) = audioBasicIO.readAudioFile(self.fname)
        #Create 2d array for MFCC features
        mfcc_feat = mfcc(sig,samplerate = 44100, nfft = 1103)
        #Create 2d array for the delta of MFCC features
        d_mfcc_feat = delta(mfcc_feat, 2)
        #Create 2d array for the log of fbank features
        fbank_feat = logfbank(sig,rate)
        dev_array = []
        for i in mfcc_feat:
            temp = stdev(i)
            dev_array.append(temp)
        tone = stdev(dev_array)
        results_dict["tone"] = tone
        return(mfcc_feat)






        
    def pitchProc(self):
        [Fs,x] = audioBasicIO.readAudioFile(self.fname)
        info=audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
        return info[0][1]

    def pitchProc2(self, results_dict):
        print("pitchProc2")
        [Fs,x] = audioBasicIO.readAudioFile(self.fname)
        info=audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
        results_dict["pitch"] = info[0][1]
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

    def volumeProc2(self, results_dict):
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
        results_dict["volume"] = freqArray
        return(freqArray)




    
## gapProc: function that allows the extraction of the gaps between
## consecutive words.
## Inputs: self
## Output: an array containing the lengths of every gap between words
## Written By: Michael Knapp and Timmothy Lane
    def gapProc(self):
    #def gapProc(self , lowest):
        sound_file = AudioSegment.from_wav(self.fname)
        audio_chunks = split_on_silence(sound_file, 
            # must be silent for at least 100ms
            min_silence_len=1,
            # consider it silent if quieter than -16 dBFS
            silence_thresh=5)

        # List made to store all of the silence .wav chunks
        waveAry = []
        # List made to store the lengths of the silence chunks
        chunkLengthArray = []

        for i, chunk in enumerate(audio_chunks):
            out_file = ".//splitAudio//chunk{0}.wav".format(i)
            #waveAry.append(chunk)
            chunkLengthArray.append(len(chunk))
    
        #If there were no silences, set the mean variable to 0
        if len(chunkLengthArray) == 0:
            avgChunkLength = 0
            stdevChunkLength = 0
        # If thee is exactly 1 silence, set the stdev to 0
        #   and the average chunk length to the value of the only silence
        elif len(chunkLengthArray) == 1:
            stdevChunkLength = 0
            avgChunkLength = chunkLengthArray[0]
        # Otherwise calculate the mean gap and stdev of the gaps and store
        #   them in variables
        else:
            avgChunkLength = mean(chunkLengthArray)
            stdevChunkLength = stdev(chunkLengthArray)
        # Return the array containing the lengths of the gaps
        return(chunkLengthArray)

## gapProc: function that allows the extraction of the gaps between
## consecutive words.
## Inputs: self
## Output: an array containing the lengths of every gap between words
## Written By: Michael Knapp and Timmothy Lane
    def gapProc2(self, results_dict):
    #def gapProc(self , lowest):
        sound_file = AudioSegment.from_wav(self.fname)
        audio_chunks = split_on_silence(sound_file, 
            # must be silent for at least 100ms
            min_silence_len=1,
            # consider it silent if quieter than -16 dBFS
            silence_thresh=5)

        # List made to store all of the silence .wav chunks
        waveAry = []
        # List made to store the lengths of the silence chunks
        chunkLengthArray = []

        for i, chunk in enumerate(audio_chunks):
            out_file = ".//splitAudio//chunk{0}.wav".format(i)
            #waveAry.append(chunk)
            chunkLengthArray.append(len(chunk))
    
        #If there were no silences, set the mean variable to 0
        if len(chunkLengthArray) == 0:
            avgChunkLength = 0
            stdevChunkLength = 0
        # If thee is exactly 1 silence, set the stdev to 0
        #   and the average chunk length to the value of the only silence
        elif len(chunkLengthArray) == 1:
            stdevChunkLength = 0
            avgChunkLength = chunkLengthArray[0]
        # Otherwise calculate the mean gap and stdev of the gaps and store
        #   them in variables
        else:
            avgChunkLength = mean(chunkLengthArray)
            stdevChunkLength = stdev(chunkLengthArray)
        # Return the array containing the lengths of the gaps
        results_dict["wordGap"] = chunkLengthArray
        return(chunkLengthArray)






##  collectMetrics:
##  Collects the audio metrics using the above methods,
##  places them into a pandas array, and returns them
##  for use by the software
##  Written by: Bryan Jones
    def collectMetrics(self):
        print("Collecting Metrics")
        queue = Queue()
        results_dict = {"pitch":[], "volume":[],"tone":[],"wordGap":[], "wordGaplen":[]}
        process_list = []
         
        print("Creating process")
        p1 = threading.Thread(target = self.pitchProc2, args=(results_dict,))
        process_list.append(p1)
        p2 = threading.Thread(target = self.volumeProc2, args=(results_dict,))
        process_list.append(p2)
        p3 = threading.Thread(target = self.mfccProc2, args=(results_dict,))
        process_list.append(p3)
        p4 = threading.Thread(target = self.gapProc2, args=(results_dict,))
        process_list.append(p4)


#        p5 = Process()
        print("Starting process")
        for process in process_list:
            process.start()
        #p1.start()

        print("Ending Processes")        
        for proc in process_list:
            proc.join()

        
        #pitch = self.pitchProc()
        pitch = results_dict["pitch"]
        pitch = stdev(pitch)
        
        #volume = self.volumeProc()
        volume = results_dict["volume"]
        volume = stdev(volume)
        
        '''tone = self.mfccProc()
        dev_array = []
        for i in tone:
            temp = stdev(i)
            dev_array.append(temp)
        tone = stdev(dev_array)'''
        
        tone = results_dict["tone"]
        
        #wordGap = self.gapProc()
        wordGap = results_dict["wordGap"]
        if(len(wordGap) != 0):
            wordGaplen = len(wordGap)
            wordGap = stdev(wordGap)
        else:
            wordGaplen = 0
            wordGap = 0
            
        user_profile = np.array([pitch, tone, volume, wordGap, wordGaplen])
        return(user_profile)
        
