import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
print(df.isnull().sum())

#Cleaned Data
#Separating target and features

df=df.replace({'diagnosis':{'M':1, 'B':0}})
#df=df.replace('B', 0)
features=df.loc[:, 'radius_mean':'fractal_dimension_mean']
target=df['diagnosis']
print(features.head())

#Checking Shape of data
print(target.shape)
print(features.shape)

print(features.head())