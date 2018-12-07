import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from profileManager import *


def compare_new(new_metrics, user_profile):
    #emotion_data = "data.csv"
    # Changed the emotion data to use user profile data
    # Tim - 11/24
    emotion_data = user_profile.path
    df = pd.read_csv(emotion_data, header = None, sep = ',', names = ['Pitch1','Pitch2','Pitch3','Pitch4','Pitch5','Pitch6','Pitch7','Pitch8','Pitch9','Pitch10',
         'Tone1','Tone2','Tone3','Tone4','Tone5','Tone6','Tone7','Tone8','Tone9','Tone10',
          'SPL1','SPL2','SPL3','SPL4','SPL5','SPL6','SPL7','SPL8','SPL9','SPL10',
          'wordGap','WordGapLen'])

    data = df.values
    y = df['Emotion']
    X = df['Pitch1','Pitch2','Pitch3','Pitch4','Pitch5','Pitch6','Pitch7','Pitch8','Pitch9','Pitch10',
         'Tone1','Tone2','Tone3','Tone4','Tone5','Tone6','Tone7','Tone8','Tone9','Tone10',
          'SPL1','SPL2','SPL3','SPL4','SPL5','SPL6','SPL7','SPL8','SPL9','SPL10',
          'wordGap','WordGapLen']

    knn = KNeighborsClassifier(n_neighbors=1) #uses k nearest neighbor to find closest example

    knn.fit(X,y)

    new_metrics = new_metrics.reshape(1,-1)
    return(knn.predict(new_metrics))


