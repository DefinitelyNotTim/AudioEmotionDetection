from pydub import AudioSegment
from pydub.silence import split_on_silence
import wave

sound_file = AudioSegment.from_wav("a-z.wav")
audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second
    min_silence_len=100,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-16
)
waveAry = []
LengthOfEachChunk = []
for i, chunk in enumerate(audio_chunks):

    out_file = ".//splitAudio//chunk{0}.wav".format(i)
    print "exporting", out_file
    waveAry += chunk
for i in waveAry():
    frames  = i.getnframes()
    rate = i.getframerate()
    duration = frames / rate
    
    LengthOfEachChunk.append(duration)
    print(LengthOfEachChunck)
    
    
    
