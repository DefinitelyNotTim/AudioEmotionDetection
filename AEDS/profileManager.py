## profileManager.py: Contains the profileManager class that allows access
##  and manipulations of user profiles for the Audio Emotion Detection System
##  Contains the following methods:
##      __init(self, userName)__: Initialization method
##      accessProfile(self): Accesses uer profiles
##      writeToProfile(self, newMetrics, Emotion): Updates user profiles
##      generateProfile(self): Creates new user profiles
##  More information regarding these methods are detailed above each method.
##  Unless otherwise specified, every method within this class was written by Timmothy Lane
##  Related Software Requirements: FR.2, FR.7, FR.8

from pathlib import Path
import os.path
from pandas import *
import csv


class profileManager:


## Initalization class for the profile manager, which is called every time 
##  a new profile object is created.
##  This method sets the file name and file path associated with a user
##  profile.
##  Related Software Requirements: FR.7
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
##  Related Software Requirements: FR.8
    def accessProfile(self):
        # Use the path attribute to create a Path for the file
        self.file = Path(self.path)
        # If the file associated with the user  profile exists
        if self.file.exists():
            # Create a dataframe holding the information of the user profile using pandas
            self.oldMetrics = pandas.read_csv(self.path, header = None, sep = ',', names = ['Pitch', 'Tone', 'SPL', 'wordGap' , 'WordGapLen', 'Emotion'])
        # If a file does not exist for the user profile
        else:
            # Generate a new file for the user profile
            self.generateProfile()
            # Create a dataframe holding the information of the user profile using pandas
            self.oldMetrics = pandas.read_csv(self.path, header = None, sep = ',', names = ['Pitch', 'Tone', 'SPL', 'wordGap' , 'WordGapLen', 'Emotion'])



##  Method that allows writing to the .csv associated with the user.
##  Inputs: the new audio metrics and the corrosponding emotion
##  Outputs: None
##  The method updates the row of the user profile with the corrosponding emotion
##      with the new metrics
##  Related Software Requirements: FR.2
##  NOTE: This method overwrites the previous data and was depreciated for the
##      new method "addtoProfile," which instead appends to the profile. This method
##      was included for educational purposes.
    def writeToProfile(self, newMetrics, emotion):
        self.accessProfile()
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Pitch"] = newMetrics[0]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "Tone"] = newMetrics[1]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "SPL"] = newMetrics[2]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "wordGap"] = newMetrics[3]
        self.oldMetrics.loc[self.oldMetrics['Emotion'] == emotion, "WordGapLen"] = newMetrics[4]
        self.oldMetrics.to_csv(self.path, index = False, header = 0)
        return self.path

## Method for genereating a new .csv file for a new user.
##  Creates a new .csv and sets it's values to the same values
##  found in the generic user profile.
##  Related Software Requirements: FR.7
    def generateProfile(self):
        # Create a dataframe holding the information of the generic profile using pandas
        generic = pandas.read_csv("profiles/generic.csv", header = None, sep = ',', names = ['Pitch', 'Tone', 'SPL', 'wordGap' , 'WordGapLen', 'Emotion'])
        # Write the dataframe to a new .csv file that will be associated with the
        #   current user profile
        generic.to_csv(self.path, index = False, header = 0)
        return self.path
		
##	Method that allows for data to be appended to a user profile while not overwriting
##		previous data
##	Written By: Bryan Jones
##  Related Software Requirements: FR.2
    def addtoProfile(self, newMetric, emotion):
        with open(self.path, 'a') as f:
            fields = [newMetric[0], newMetric[1],newMetric[2],newMetric[3],newMetric[4], emotion]
            writer = csv.writer(f)
            writer.writerow(fields)
        

    


