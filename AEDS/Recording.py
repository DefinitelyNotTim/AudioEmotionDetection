import pyaudio
import wave
'''
The recording class was originally written by Humberto and heavily edited by Alex to allow for variable recording time, easily processed formatting,
and stopping the recording on demand.
Related Software Requirements: FR.1, HI.1, CI.1
'''
wave_output_filename = "user_recording.wav"

class Recording(object):
    def __init__(self, fname, channels, rate, CHUNK):
        self.fname= fname
        self.channels=channels
        self.rate=rate
        self.CHUNK=CHUNK
        self._p = pyaudio.PyAudio()
        self.wavefile = self._prep_file(self.fname)
        self._stream = None


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
        self.close()
        return self
    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback

    
    def close(self):
        self._stream.close()
        self._p.terminate()
        self.wavefile.close()
        

    def _prep_file(self, fname):
        waveFile = wave.open(self.fname,'wb')
        waveFile.setnchannels(self.channels)
        waveFile.setsampwidth(self._p.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(self.rate)
        return waveFile
