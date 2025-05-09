# -*- coding: utf-8 -*-
"""cluster_evaluation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gm9XEODkb7QLYUoLpo3AoGMQfHRmBffU
"""

import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from sklearn.metrics import confusion_matrix

data_path = 'vectorised.csv' # path of the dataset
preproc_path = 'preprocessed.csv' # path of the preprocessed dataset for labels

data = pd.read_csv(data_path) # loads the dataset
labels = pd.read_csv(preproc_path)['status'] # loads the preprocessed dataset for the labels
labels = [0 if i == 'invalid' else 1 for i in labels] # encodes valid to 1 and invalid to 0

cluster_labels = [] # provide the list or array of labels assigned by the KMeans clustering model.

''' !!! warning don't run the further code without providing the pred_labels !!! '''
# silhouette_score = silhouette_score(data, cluster_labels) # overall silhouette score
# print(silhouette_score)

# ind_sihouette_score = silhouette_samples(data, cluster_labels) # individual silhouette score of all data points
# ind_sihouette_score = np.round(ind_sihouette_score*10000)/10000 # rounding off to 4 digits after decimal
# print(ind_sihouette_score)

# conf_matrix = confusion_matrix(labels, cluster_labels) # gives confusion matrix
# print(conf_matrix)