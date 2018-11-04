from pydub import AudioSegment
from pydub.silence import split_on_silence
import wave
from statistics import *

print("starting")




sound_file = AudioSegment.from_wav("english.wav")
audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=100,
    # consider it silent if quieter than -16 dBFS
    silence_thresh=-20)


waveAry = []
chunkLengthArray = []

for i, chunk in enumerate(audio_chunks):
    #print("loop1")
    out_file = ".//splitAudio//chunk{0}.wav".format(i)
    #print ("exporting", out_file)
    waveAry.append(chunk)

    
for i in waveAry:
    #print(i)
    #print(len(i))
    chunkLengthArray.append(len(i))
    
    



print(chunkLengthArray)
print(mean(chunkLengthArray))
print(stdev(chunkLengthArray))
print("finished")
