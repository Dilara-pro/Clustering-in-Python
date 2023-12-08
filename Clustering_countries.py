# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:25:05 2023

@author: Huawei
"""

from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from matplotlib import pyplot as plt
import pandas as pd
from scipy.cluster.vq import whiten
import os

directory = 'C:\\Users\\Huawei\\.spyder-py3\\model_girdileri'  
filename = 'Country_Distance.csv'
file_path = os.path.join(directory, filename)
country = pd.read_csv(file_path)

norm_country = whiten(country.iloc[:,1:22])
distance_matrix = linkage(norm_country, method = 'complete', metric = 'euclidean')
cluster_labels = fcluster(distance_matrix, 3, criterion='maxclust')

dn = dendrogram(distance_matrix, labels=range(1,21))
plt.show()

from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from matplotlib import pyplot as plt
import pandas as pd
from scipy.cluster.vq import whiten
import os

directory = 'C:\\Users\\Huawei\\.spyder-py3\\model_girdileri'  
filename = 'Country_City.csv'
file_path = os.path.join(directory, filename)
country_city = pd.read_csv(file_path)

norm_country_city = whiten(country_city.iloc[:,1:22])
distance_matrix_city = linkage(norm_country_city, method = 'single', metric = 'euclidean')
cluster_labels = fcluster(distance_matrix_city, 3, criterion='maxclust')

dn = dendrogram(distance_matrix_city, labels=range(1,21))


































