# -*- coding: utf-8 -*-
"""Praktikum 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CfjA359uFS7ckrbpxh_PJreTGkvcRwVi
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv('kc_house_data.csv')

Y = dataset[['price']]

X = dataset.drop(['price','id','date'], axis=1)

X.info()

#list our columns
columns = X.columns
columns

#show first 5 records
X.head()

X.describe()

dataset = dataset.drop(['id','date'], axis = 1)

dataset.corr(method='pearson')

plt.subplots(figsize=(10,8))
sns.heatmap(dataset.corr())

x = X[['sqft_living']]
y = Y

plt.figure(figsize=(10,6))
plt.xlabel('House Sqft')
plt.ylabel('House Price')
plt.title('Price by Sqft_Living')
plt.scatter(x,y, marker='o', color='g')

from scipy import stats
sns.set(color_codes=True)

slope, intercept, r_value, p_value, std_err = stats.linregress(dataset['sqft_living'],dataset['price'])

f = plt.figure(figsize=(10,6))
data = dataset[['price', 'sqft_living']]
ax = sns.regplot(x='sqft_living', y='price', data=data,
                 scatter_kws={"color":"g"},
                 line_kws={'color':'r', 'label':"y={0:.1f}x+{1:.1f}".format(slope,intercept)})
ax.legend()

print(slope, intercept)

print(std_err)

x = X[['sqft_living']]
y = Y

xg = x.values.reshape(-1,1)
yg = y.values.reshape(-1,1)
xg = np.concatenate((np.ones(len(x)).reshape(-1,1),x), axis=1)

def computeCost(x, y, theta):
  m= len(y)
  h_x = x.dot(theta)
  j = np.sum(np.square(h_x - y))*(1/(2*m))
  return j

def gradientDescent(x, y, theta, alpha, iteration):
  print('Running Gradient Descent...')
  j_hist = []
  m = len(y)
  for i in range(iteration):
    j_hist.append(computeCost(x,y, theta))
    h_x = x.dot(theta)
    theta = theta - ((alpha/m) *((np.dot(x.T, (h_x-y) ))))
  return theta, j_hist

theta = np.zeros((2,1))
iteration = 2000
alpha = 0.001

theta, cost = gradientDescent(xg, yg, theta, alpha, iteration)
print('Theta found by Gradient Descent: slope = {} and intercept {}'. format(theta[1], theta[0]))

theta.shape

plt.figure(figsize=(10,6))
plt.title('$\\theta_0$ = {} , $\\theta_1$ = {}'.format(theta[0], theta[1]))
plt.scatter(x,y, marker='o', color='g')
plt.plot(x,np.dot(x.values, theta.T))
plt.show()

plt.plot(cost)
plt.xlabel('No. of iterations')
plt.ylabel('Cost')

from scipy import stats

xs = x.iloc[:,0]
ys = y.iloc[:,0]
#xs = np.concatenate((np.ones(len(x)).reshape(-1,1), x), axis=1)

slope, intercept, r_value, p_value, std_err = stats.linregress(xs, ys)

print('Slope = {} and Intercept = {}'.format(slope, intercept))
print('y = x({})  +{}'.format(slope, intercept))

plt.figure(figsize=(10,6))
plt.title('$\\theta_0$ = {} , $\\theta_1$ = {}'.format(intercept, slope))
plt.scatter(xs,y, marker='o', color='green')
plt.plot(xs, np.dot(x, slope), 'r')

xsl = x.values.reshape(-1,1)
ysl = y.values.reshape(-1,1)
xsl = np.concatenate((np.ones(len(xsl)).reshape(-1,1), xsl), axis=1)

from sklearn.linear_model import LinearRegression

slr = LinearRegression()
slr.fit(xsl[:,1].reshape(-1,1), ysl.reshape(-1,1))
y_hat = slr.predict(xsl[:,1].reshape(-1,1))

print('theta[0] = ', slr.intercept_)
print('theta[1] = ', slr.coef_)

thetas = np.array((slr.intercept_, slr.coef_)).squeeze()

plt.figure(figsize=(10,6))
plt.title('$\\theta_0$ = {} , $\\theta_1$ = {}'.format(thetas[0], thetas[1]))
plt.scatter(xsl[:,1],y, marker='x', color='g')
plt.plot(xsl[:,1], np.dot(xsl, thetas), 'r')