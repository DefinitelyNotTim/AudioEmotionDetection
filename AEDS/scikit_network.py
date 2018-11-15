import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


def compare_new(new_metrics):
    emotion_data = "data.csv"
    df = pd.read_csv(emotion_data, header = None, sep = ',', names = ['Pitch', 'Tone', 'SPL', 'wordGap' , 'WordGapLen', 'Emotion'])

    data = df.values
    y = df['Emotion']
    X = df[['Pitch', 'Tone', 'SPL' , 'wordGap' , 'WordGapLen']]

    knn = KNeighborsClassifier(n_neighbors=1) #uses k nearest neighbor to find closest example

    knn.fit(X,y)

    new_metrics = new_metrics.reshape(1,-1)
    return(knn.predict(new_metrics))



