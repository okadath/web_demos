import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
 
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

# zipurl = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip'
# with urlopen(zipurl) as zipresp:
#     with ZipFile(BytesIO(zipresp.read())) as zfile:
#         zfile.extractall('/tmp/Bike-Sharing-Dataset')
        
bikes_hour_df_raw = pd.read_csv('hour.csv')
bikes_day_df_raw = pd.read_csv('/tmp/Bike-Sharing-Dataset/day.csv')

#usando tmp da normalizados
print(bikes_hour_df_raw['cnt'].describe())
print(bikes_hour_df_raw.head())

bikes_hour_df = bikes_hour_df_raw.drop(['casual', 'registered'], axis=1) 

fig,ax = plt.subplots(1)
ax.plot(sorted(bikes_hour_df['cnt']), color='blue', marker='.')
ax.xaxis.set_visible(False)
ax.set_ylabel("Sorted Rental Counts", fontsize=12)
fig.suptitle('Recorded Bike Rentals Counts', fontsize=16)


