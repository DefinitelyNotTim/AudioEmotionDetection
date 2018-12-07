##  scikit_network.py:
##      Allows the AEDS software to make predictions about the user's
##      emotional state by comparing new vocal metrics against previously
##      stored metrics using the k-nearest neighbor algorithm.
##  Related Software Requirements: FR.8, FR.9
##  Authors: Bryan Jones and Mark Webb
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from profileManager import *


## compare_new(): Compares data pertaining to the new recording and compares
##  it against the data retrieved from the user profile using the k-nearest
##  neighbor algorithm to find the closest match for the new data.
## Inputs: Data conveying the vocal metrics from the recent audio recording,
##          and the user profile.
## Outputs: The predicted emotional state of the user.
## Authors: Bryan Jones and Mark Webb
## Related Software Requirements:
def compare_new(new_metrics, user_profile):
    # Changed the emotion data to use user profile data
    # Tim - 11/24
    emotion_data = user_profile.path
    df = pd.read_csv(emotion_data, header = None, sep = ',', names = ['Pitch', 'Tone', 'SPL', 'wordGap' , 'WordGapLen', 'Emotion'])

    data = df.values
    y = df['Emotion']
    X = df[['Pitch', 'Tone', 'SPL' , 'wordGap' , 'WordGapLen']]

    knn = KNeighborsClassifier(n_neighbors=1) #uses k nearest neighbor to find closest example

    knn.fit(X,y)

    new_metrics = new_metrics.reshape(1,-1)
    return(knn.predict(new_metrics))


