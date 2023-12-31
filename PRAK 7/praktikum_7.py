# -*- coding: utf-8 -*-
"""praktikum 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TJAP5VZUB3FpVPFrlx42euRTEqPv8yeB
"""

# Commented out IPython magic to ensure Python compatibility.
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('loans.csv', index_col='client_id')

df.head()

df.shape

df.info()

df.dtypes

df['loan_id'] = df['loan_id'].astype('object')
df['repaid'] = df['repaid'].astype('category')

df['loan_start'] = pd.to_datetime(df['loan_start'], format='%Y-%m-%d')
df['loan_end'] = pd.to_datetime(df['loan_end'], format='%Y-%m-%d')

df.dtypes

df.describe()

df.describe(exclude=[np.number])

df.isnull().sum()

df['loan_amount'].plot(kind='box')
plt.show()

df['rate'].plot(kind='box')
plt.show()

df['SQRT_RATE'] = df['rate']**0.5

df['sqrt_rate'] = np.sqrt(df['rate'])

df.head()

print("The skewness of the original data is {}".format(df.rate.skew()))
print('The Skewness of the SQRT transformed data is {}'.format(df.SQRT_RATE.skew()))

print('')

print("The kurtosis of the original data is {}".format(df.rate.kurt()))
print("The Kurtosis of the SQRT transformed data is {}".format(df.SQRT_RATE.kurt()))

# plotting the distribution
fig, axes = plt.subplots(1,2, figsize=(15,5))
sns.distplot(df['rate'], ax=axes[0])
sns.distplot(df['sqrt_rate'], ax=axes[1])

plt.show()

df['Log Rate'] = np.log(df['rate'])

df.head()

print("The skewness of the original data is {}".format(df.rate.skew()))
print('The Skewness of the SQRT transformed data is {}'.format(df.SQRT_RATE.skew()))
print("The skewness of the LOG transformed data is {}". format(df['Log Rate'].skew()))

print('')

print("The kurtosis of the original data is {}".format(df.rate.kurt()))
print("The Kurtosis of the SQRT transformed data is {}".format(df.SQRT_RATE.kurt()))
print("The Kurtosis of the LOG transformed data is {}". format(df['Log Rate'].kurt()))

# plot grafik
fig, axes = plt.subplots(1,3,figsize=(15,5))

sns.distplot(df['rate'], ax=axes[0])
sns.distplot(df['SQRT_RATE'], ax=axes[1])
sns.distplot(df['Log Rate'], ax=axes[2])

plt.show()

# Menggunakan fungsi Lambda
df['LOG_Rate'] = df['rate'].apply(lambda x:np.log(x))

df.head()

df1 = pd.read_csv('loans.csv', index_col='client_id')
df1.head()

# loan_id
df1['loan_id'] = df1['loan_id'].astype('object')

# repaid
df1['repaid'] = df1['repaid'].astype('category')

# loan_start
df1['loan_start'] = pd.to_datetime(df1['loan_start'], format='%Y-%m-%d')

# loan_end
df1['loan_end'] = pd.to_datetime(df1['loan_end'], format='%Y-%m-%d')

import scipy.stats as stats

# Membuat variabel baru dengan Z-Score setiap catatan
df1['ZR'] = stats.zscore(df1['rate'])

df1.head()

# Kombinasi Batas Bawah dan Batas Atas
df1[(df1['ZR']<-3) | (df1['ZR']>3)]

df1[(df1['ZR']<-3) | (df1['ZR']>3)].shape[0]

df2 = df1[(df1['ZR']>-3) & (df1['ZR']<3)].reset_index()
df2.head()

df1.shape

df2.shape

df3 = df2.copy()

df3.drop(columns = ['ZR'], inplace=True)
df3.head()

# Mencari Kuantil
Q1 = df3.rate.quantile(0.25)
Q2 = df3.rate.quantile(0.50)
Q3 = df3.rate.quantile(0.75)

# IQR : Rentang Inter-Kuartil
IQR = Q3 - Q1

# Batas Bawah:
LC = Q1 - (1.5*IQR)

# Batas Atas:
UC = Q3 + (1.5*IQR)

display(LC)
display(UC)

# Plot
sns.distplot(df3.rate)
plt.axvline(UC, color='r')
plt.axvline(LC, color='r')
plt.axvline(Q1, color='g')
plt.axvline(Q3, color='g')
plt.show()

# Temukan jumlah Pencilan berdasarkan IQR
df3[(df3.rate<LC) | (df3.rate>UC)].reset_index(drop=True)

df3[(df3.rate<LC) | (df3.rate>UC)].shape[0]

# Simpan data bersih berdasarkan IQR
df4 = df3[(df3.rate>LC) & (df3.rate<UC)]
df4.head()

df3.shape

df4.shape

# Diagram Kotak untuk rate --- berdasarkan Metode IQR
sns.boxplot(df1.rate)
plt.show()

# Diagram Kotak untuk rate --- berdasarkan data yang telah dibersihkan dengan Z-Score
sns.boxplot(df2.rate)
plt.show()

# Diagram Kotak untuk rate --- berdasarkan data yang telah dibersihkan dengan IQR
sns.boxplot(df4.rate)
plt.show()

# untuk Rate
avg_rate = df3['rate'].mean()
avg_rate

std_rate = df3['rate'].std()
std_rate

# Langkah 1 : transformasi menggunakan Z-score
df3['Z_Score_Rate'] = (df3['rate'] - avg_rate)/std_rate

df3.head()

# memeriksa apakah skewness dan kurtosis setelah scaling atau tidak
# Untuk Rate
print("The Skewness for the real original data is {}.".format(df3.rate.skew()))
print("The Kurtosis for the real original data is {}.".format(df3.rate.kurt()))

print('')

print("The Skewness for the Z-score Scaled column is {}.".format(df3.Z_Score_Rate.skew()))
print("Kurtosis for the Z-score Scaled column is {}.".format(df3.Z_Score_Rate.kurt()))

# Untuk Loan_amount
avg_LA = df3['loan_amount'].mean()
avg_LA

std_LA = df3['loan_amount'].std()
std_LA

# Langkah 1 : transformasi menggunakan Z-score
df3['Z_Score_LA'] = (df3['loan_amount'] - avg_LA)/std_LA

df3.head()

# memeriksa apakah skewness dan kurtosis setelah scaling atau tidak
# Untuk Loan_amount
print("The Skewness for the real original data is {}.".format(df3.loan_amount.skew()))
print("The Kurtosis for the real original data is {}.".format(df3.loan_amount.kurt()))

print('')

print("The Skewness for the Z-score Scaled column is {}.".format(df3.Z_Score_LA.skew()))
print("Kurtosis for the Z-score Scaled column is {}.".format(df3.Z_Score_LA.kurt()))

# Distribusi dari kolom-kolom
fig, axes = plt.subplots(2,2, figsize=(15,5))

sns.distplot(df3['rate'], ax=axes[0,0])
sns.distplot(df3['Z_Score_Rate'], ax=axes[0,1])
sns.distplot(df3['loan_amount'], ax=axes[1,0])
sns.distplot(df3['Z_Score_LA'], ax=axes[1,1])

plt.show()

# Loans data:
df4 = df3.copy()
df4.drop(columns=['Z_Score_Rate'], inplace=True)
df4.head()

from sklearn.preprocessing import StandardScaler

df4_num = df[['loan_amount', 'rate']]
df4_num.head()

SS = StandardScaler()

scaled_x = SS.fit_transform(df4_num)
scaled_x

#ForeRate:
min_rate = df4.rate.min()
min_rate

max_rate = df4.rate.max()
max_rate

df4['Min_Max_R'] = (df4['rate'] - min_rate)/ (max_rate - min_rate)

# memeriksa apakah skewness dan kurtosis setelah scaling atau tidak
# Untuk Rate
print("Skewness untuk data asli adalah {}.".format(df4.rate.skew()))
print("Skewness untuk kolom yang telah diubah dengan Z-score adalah {}.".format(df3.Z_Score_Rate.skew()))
print("Skewness untuk Min Max Scaled Data adalah {}.".format(df4.Min_Max_R.skew()))


print('')

print("Kurtosis untuk data asli adalah {}.".format(df4.rate.kurt()))
print("Kurtosis untuk kolom yang telah diubah dengan Z-score adalah {}.".format(df3.Z_Score_Rate.kurt()))
print("Kurtosis untuk Min Max Scaled Data adalah {}.".format(df4.Min_Max_R.kurt()))

# Distribusi dari kolom-kolom
# Untuk Rate
fig, axes = plt.subplots(1,3, figsize=(15,5))

sns.distplot(df3['rate'], ax=axes[0])
sns.distplot(df3['Z_Score_Rate'], ax=axes[1])
sns.distplot(df4['Min_Max_R'], ax=axes[2])

plt.tight_layout()
plt.show()

# Untuk Loan_amount
min_LA = df4.loan_amount.min()
min_LA

max_LA = df4.loan_amount.max()
max_LA

df4['Min_Max_LA'] = (df4['loan_amount'] - min_LA)/ (max_LA - min_LA)

# memeriksa apakah skewness dan kurtosis setelah scaling atau tidak
# Untuk Rate
print("Skewness untuk data asli adalah {}.".format(df4.loan_amount.skew()))
print("Skewness untuk kolom yang telah diubah dengan Z-score adalah {}.".format(df3.Z_Score_LA.skew()))
print("Skewness untuk Min Max Scaled Data adalah {}.".format(df4.Min_Max_LA.skew()))


print('')

print("Kurtosis untuk data asli adalah {}.".format(df4.loan_amount.kurt()))
print("Kurtosis untuk kolom yang telah diubah dengan Z-score adalah {}.".format(df3.Z_Score_LA.kurt()))
print("Kurtosis untuk Min Max Scaled Data adalah {}.".format(df4.Min_Max_LA.kurt()))

# Distribusi dari kolom-kolom
# Untuk Loan_Amount
fig, axes = plt.subplots(1,3, figsize=(15,5))

sns.distplot(df3['loan_amount'], ax=axes[0])
sns.distplot(df3['Z_Score_LA'], ax=axes[1])
sns.distplot(df4['Min_Max_LA'], ax=axes[2])

plt.tight_layout()
plt.show()

from sklearn.preprocessing import MinMaxScaler

MS = MinMaxScaler()

MinMaxScaled = MS.fit_transform(df4_num)
MinMaxScaled

#loans data:
df_loans = df3.copy()

df_loans.drop(columns=['Z_Score_Rate'], inplace=True)
df_loans.drop(columns=['Z_Score_LA'], inplace=True)

df_loans.head()

df_loans.dtypes

# Repaid juga merupakan kolom kategori dan membuat dummy untuk loan_type
df_loans.repaid.head()

dummy_cat = pd.get_dummies(df_loans['loan_type'], drop_first=True)
dummy_cat.head()

from sklearn.preprocessing import OneHotEncoder

OE_tips = OneHotEncoder(drop='first').fit(df_loans[['loan_type']])
OE_tips.categories_

from sklearn.preprocessing import LabelEncoder

LE = LabelEncoder()

LE_tips = LE.fit(df_loans[['loan_type']])

LE_tips.classes_

LE_tips.transform(['other', 'cash', 'home', 'credit'])

LE_tips.inverse_transform([1, 2, 3, 0])

import datetime as dt

df_loans['loan_tenure'] =  df_loans['loan_end'] - df_loans['loan_start']

df_loans.head()

df_loans.dtypes

df_loans['loan_tenure'] = df_loans['loan_tenure'].dt.days
df_loans['loan_tenure']

# Jangka waktu dalam jumlah Tahun
df_loans['loan_tenure'] = df_loans['loan_tenure']/365
df_loans['loan_tenure']

from sklearn.model_selection import train_test_split

# Membagi variabel X dan Y
Y = df_loans['loan_amount']
X = df_loans.drop('loan_amount', axis=1)

# Variabel Independen
X.head()

# Variabel Dependen atau Target
Y.head()

# Membagi dataset menjadi 80% Data Pelatihan dan 20% Data Pengujian
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,train_size=0.8, random_state=0)

# random_state ---> adalah seed -- memperbaiki pemilihan sampel untuk dataset Pelatihan & Pengujian
# periksa dimensi subset pelatihan & pengujian untuk
print("Bentuk X_train adalah:", X_train.shape)
print("Bentuk X_test adalah:", X_test.shape)

print('')
print("Bentuk Y_train adalah:", Y_train.shape)
print("Bentuk Y_test adalah:", Y_test.shape)

# median untuk y_train
median_y_train = Y_train.median()

# median untuk y_test
median_y_test = Y_test.median()

print('Median untuk variabel Y Train adalah:', median_y_train)

print('Median untuk variabel Y Test adalah:', median_y_test)