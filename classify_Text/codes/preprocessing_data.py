import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import wordcloud
#이는 IPython 에서 제공하는 Rich output 에 대한 표현 방식
#%matplotlib inline #이 문구는 주피터에서만 되기 때문에 아래의 문구로 대체한다.
plt.show()

DATA_IN_PATH = '../data/'
print("file size : ")
for file in os.listdir(DATA_IN_PATH):
    if 'txt' in file:
        print(file.ljust(30)+str(round(os.path.getsize(DATA_IN_PATH+file)/ 1000000, 2))+'MB')

train_data = pd.read_csv(DATA_IN_PATH + 'ratings_train.txt', header = 0, delimiter = '\t',quoting=3)
print(train_data.head())
print("total number of training data : {}".format(len(train_data)))
train_length = train_data['document'].astype(str).apply(len) #각 데이터에 대한 길이 값 추출
print(train_length.head())

#drawing histogram 전체 데이터에 대해 길이에 대한 히스토그램을 그린다.
plt.figure(figsize=(12, 5))
plt.hist(train_length, bins=200, alpha=0.5, color='r', label='word')
plt.yscale('log', nonpositive='clip')
plt.title('Log-Histogram of length of review')
plt.xlabel('Length of review')
plt.ylabel('Number of review')
plt.show()

