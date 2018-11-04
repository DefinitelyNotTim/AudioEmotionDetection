
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import wave

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
