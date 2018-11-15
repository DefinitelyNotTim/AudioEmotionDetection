# Audio Emotion Detection System

An emotion processing system that prompts the user to record audio through the initial GUI with the deafult microphone on the system. Extracts metrics pertaining to the audio file specifically Pitch, Sound Pressure Level, Tone and the Gap between consecutive words. The system then users the k-nearest neighbor to identify closest emotion that has been stored in a csv file and displays it to the user.  

## Instalation

Run the setup.py from the command line from both the pyAudioAnalysis and python_speech_features

    >>py setup.py