# AudioEmotionDetection
Real-time human emotion detection and analysis through voice and speech pattern processing.
## Authors: 
Humberto Colin, Bryan Jones, Michael Knapp, Timmothy Lane, Alex Shanon, and Mark Webb

## Instructions To Run:
-To run the Audio Emotion Detection (AEDS) software, you will need to have python version 3.6.6 or Python 3.6.7 installed on
your computer. This software will not work with python 3.7 due to library dependencies. These versions of Python can be found at:
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
    
  -Once the above packages are installed, the AEDS software can be executed on the host machine
  -To run the AEDS software, simply execute the Python file labeled "AEDS_Interface_(Run_Me).py"
    -This file can be executed in numerous ways, depending on the host machine. The easiest methods include:
      -Using a command line argument (ie. "pyhon AEDS_Interface_(Run_Me).py").
      -Running the file through the IDLE Python interpreter.
      -Double clicking the file (only works if proper path associations are set on the host machine).
      
## Using the software
Once the software is running on your machine, a simple graphical user interface should be displayed. This interface only
contains two texts fields and two buttons.

    -User Name: This text field allows the user to enter in a their desired username. If no username is entered, the user will
     have their data stored in and compared against a generic file containing data from all nameless users. If the user does
     enter a username, a new user profile will be created for them, allowing the software to specify its prediction to data
     relating specifically to the user.

    -Predicted Emotion: This text field is used by the software to notify the user of its prediction and is not intended to be
     altered by the user.

    -Start Recording: This button will begin the process of capturing audio from the user's connected microphone. If the user
     wishes to enter a username, they must do so BEFORE hitting this button.

    -Stop Recording: This button prompts the software to stop recording, analyze the audio, compare it against previous audio
     recordings, and display the predicted emotion to the user. After hitting this button, a pop-up will be displayed to the
     user allowing them to indicate if the predicted emotion was correct. If the predicted emotion was correct, hit the yes
     button. If the predicted emotion was not correct, hit the no button and a drop-down menu will be displayed, allowing the
     user to select the correct emotion.
