# AudioEmotionDetection
Real-time human emotion detection and analysis through voice and speech pattern processing
## Authors: 
Humberto Colin, Bryan Jones, Michael Knapp, Timmothy Lane, Alex Shanon, and Mark Webb

## Instructions To Run:
-To run the Audio Emotion Detection (AEDS) software, you will need to have python version 3.6.6 or Python 3.6.7 installed on your
 computer. This software will not work with python 3.7 due to library dependencies. These versions of Python can be found at:
 https://www.python.org/downloads/
 
 -Once the correct version of Python is installed on your computer, you will need to install multiple python packages that the
  software depends on. You can install these packages using different methods. The easiest method to install these packages
  would be using Python's built in package manager, PIP. PIP installs can be performed through the command line argument:
  "python -m pip install <package name>"
  More details about installing python packages can be found at:
  https://packaging.python.org/tutorials/installing-packages/
  
  -The packages that must be installed to run the AEDS software include:
    
    -pyAudioAnalysis
      -More information on this library and installation can be found at:
      https://github.com/tyiannak/pyAudioAnalysis
      
     -pyaudio
      -More information on this library and installation can be found at:
      https://people.csail.mit.edu/hubert/pyaudio/
    
    -numpy
      -More information on this library and installation can be found at:
      http://www.numpy.org/
      https://docs.scipy.org/doc/numpy-1.15.1/reference/
    
    -pydub
      -More information on this library and installation can be found at:
      https://github.com/jiaaro/pydub
   
    -pandas
      -More information on this library and installation can be found at:
      https://pandas.pydata.org/
   
    -scikit-learn
      -NOTE: To install sklearn, -U must be used in the command line argument. ie: "pip install -U scikit-learn"
      -More information on this library and installation can be found at:
      https://scikit-learn.org/stable/install.html
   
    -python_speech_features
      -More information on this library and installation can be found at:
      https://github.com/jameslyons/python_speech_features
   
    -libmagic
      -libmagic version 0.4.14 must be installed. This can be done with the command line argument:
      "python -m pip install python-magic-bin==0.4.1.4"
      
    NOTE: For certain packages above the installation process in the corresponding links must be used instead of standard
    PIP installations.
