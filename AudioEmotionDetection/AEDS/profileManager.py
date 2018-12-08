## profileManager.py: Contains the profileManager class that allows access
##  and manipulations of user profiles for the Audio Emotion Detection System
##  Contains the following methods:
##      __init(self, userName)__: Initialization method
##      accessProfile(self): Accesses uer profiles
##      writeToProfile(self, newMetrics, Emotion): Updates user profiles
##      generateProfile(self): Creates new user profiles
##  More information regarding these methods are detailed above each method.
##  Unless otherwise specified, every method within this class was written by Timmothy Lane

from pathlib import Path
import os.path
from pandas import *
import csv


class profileManager:


## Initalization class for the profile manager, which is called every time 
##  a new profile object is created.
##  This method sets the file name and file path associated with a user
##  profile.
    def __init__(self, userName):
        #If receieved userName is empty or null
        if userName == "" or userName == None:
            #set the file path and name to match the generic file
            self.fileName = "generic.csv"
            self.path = "profiles/"+self.fileName
        #If a userName is provided
        else:
            #Set the file name and path to match the user name
            self.fileName = userName +".csv"
            self.path = "profiles/"+self.fileName



## Method that accesses a user profile .csv file.
##  Checks to see if a user profile .csv exists, and
##   calls the generateProfile method if one does not.
##  Creates a dataframe from the user profile so that
##   the metrics can be easier accessed.
    def accessProfile(self):
        # Use the path attribute to create a Path for the file
        self.file = Path(self.path)
        #print(self.file)       #print statement for debugging
        # If the file associated with the user  profile exists
        if self.file.exists():
            # Create a dataframe holding the information of the user profile using pandas
            self.oldMetrics = pandas.read_csv(self.path, header = None, sep = ',', names = ['Pitch1','Pitch2','Pitch3','Pitch4','Pitch5','Pitch6','Pitch7','Pitch8','Pitch9','Pitch10',
        'Tone1','Tone2','Tone3','Tone4','Tone5','Tone6','Tone7','Tone8','Tone9','Tone10',
        'SPL1','SPL2','SPL3','SPL4','SPL5','SPL6','SPL7','SPL8','SPL9','SPL10',
        'wordGap','WordGapLen','Emotion'])
        # If a file does not exist for the user profile
        else:
            # Generate a new file for the user profile
            self.generateProfile()
            # Create a dataframe holding the information of the user profile using pandas
            self.oldMetrics = pandas.read_csv(self.path, header = None, sep = ',', names = ['Pitch1','Pitch2','Pitch3','Pitch4','Pitch5','Pitch6','Pitch7','Pitch8','Pitch9','Pitch10',
        'Tone1','Tone2','Tone3','Tone4','Tone5','Tone6','Tone7','Tone8','Tone9','Tone10',
        'SPL1','SPL2','SPL3','SPL4','SPL5','SPL6','SPL7','SPL8','SPL9','SPL10',
        'wordGap','WordGapLen','Emotion'])



##  Method that allows writing to the .csv associated with the user.
##  Inputs: the new audio metrics and the corrosponding emotion
##  Outputs: None
##  The method updates the row of the user profile with the corrosponding emotion
##      with the new metrics
    def writeToProfile(self, newMetrics, emotion):
        self.accessProfile()
        #print(self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion])
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch1"] = newMetrics[0]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch2"] = newMetrics[1]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch3"] = newMetrics[2]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch4"] = newMetrics[3]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch5"] = newMetrics[4]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch6"] = newMetrics[5]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch7"] = newMetrics[6]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch8"] = newMetrics[7]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch9"] = newMetrics[8]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch10"] = newMetrics[9]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone1"] = newMetrics[10]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone2"] = newMetrics[11]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone3"] = newMetrics[12]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone4"] = newMetrics[13]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone5"] = newMetrics[14]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone6"] = newMetrics[15]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone7"] = newMetrics[16]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone8"] = newMetrics[17]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone9"] = newMetrics[18]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone10"] = newMetrics[19]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL1"] = newMetrics[20]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL2"] = newMetrics[21]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL3"] = newMetrics[22]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL4"] = newMetrics[23]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL5"] = newMetrics[24]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL6"] = newMetrics[25]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL7"] = newMetrics[26]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL8"] = newMetrics[27]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL9"] = newMetrics[28]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL10"] = newMetrics[29]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "wordGap"] = newMetrics[30]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "WordGapLen"] = newMetrics[31]
        #print(self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion])
        self.oldMetrics.to_csv(self.path, index = False, header = 0)
        return self.path

## Method for genereating a new .csv file for a new user.
##  Creates a new .csv and sets it's values to the same values
##  found in the generic user profile.
    def generateProfile(self):
        # Create a dataframe holding the information of the generic profile using pandas
        generic = pandas.read_csv("profiles/generic.csv", header = None, sep = ',', names = ['Pitch1','Pitch2','Pitch3','Pitch4','Pitch5','Pitch6','Pitch7','Pitch8','Pitch9','Pitch10',
        'Tone1','Tone2','Tone3','Tone4','Tone5','Tone6','Tone7','Tone8','Tone9','Tone10',
        'SPL1','SPL2','SPL3','SPL4','SPL5','SPL6','SPL7','SPL8','SPL9','SPL10',
        'wordGap','WordGapLen','Emotion'])
        # Write the dataframe to a new .csv file that will be associated with the
        #   current user profile
        generic.to_csv(self.path, index = False, header = 0)
        return self.path
    def addtoProfile(self, newMetric, emotion):
        with open(self.path, 'a') as f:
            fields = [newMetric[0], newMetric[1],newMetric[2],newMetric[3],newMetric[4],newMetric[5],
            newMetric[6], newMetric[7],newMetric[8],newMetric[9],newMetric[10],newMetric[11],newMetric[12],
            newMetric[13], newMetric[14],newMetric[15],newMetric[16],newMetric[17],newMetric[18],newMetrics[19],
            newMetric[20], newMetric[21],newMetric[22],newMetric[23],newMetric[24],newMetric[25],newMetrics[26],
            newMetric[27], newMetric[28],newMetric[29],newMetric[30],newMetric[31],emotion]
            writer = csv.writer(f)
            writer.writerow(fields)
        

    


