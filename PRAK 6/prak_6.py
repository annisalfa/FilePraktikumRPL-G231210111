# -*- coding: utf-8 -*-
"""Prak_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v5nuSF3LDfLdk--U8TFWu2NS2bZ2MHyt
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
sns.set(color_codes=True)

df = pd.read_csv("data.csv")
df.head(5)

df.tail

df.dtypes

df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
df.head(5)

df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode", "highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Harga"})
df.head(5)

df.shape

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

df.count

df = df.drop_duplicates()
df.head(5)

df.count()

print(df.isnull().sum())

df = df.dropna()
df.count()

print(df.isnull().sum())

sns.boxplot(x=df['Harga'])

sns.boxplot(x=df['HP'])

sns.boxplot(x=df['Cylinders'])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape

df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');

plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c, cmap="BrBG", annot=True)
c

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Harga'])
ax.set_xlabel('HP')
ax.set_ylabel('Harga')
plt.show()