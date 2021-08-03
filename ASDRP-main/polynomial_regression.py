import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv("./Data/final_data.csv", low_memory=False)

x = df[['Gender', 'Age', 'Ethnicity', 'Location']]
y = df['Income']

x_train = x[:-20]
x_test = x[-20:]
y_train = y[:-20]
y_test = y[-20:]
poly_fit = PolynomialFeatures(degree=6)

X_poly = poly_fit.fit_transform(x_train)
pr_model = LinearRegression()
pr_model.fit(X_poly, y_train)
y_pred = pr_model.predict(X_poly)

y_new = pr_model.predict(poly_fit.fit_transform(x_test))
plt.plot(x_test,y_new,color='blue',linewidth=3)

plt.show()
#'''
