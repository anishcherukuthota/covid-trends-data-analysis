import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/home/anish/PycharmProjects/asdrp/data/final_data.csv", low_memory=False)

x = df[['Gender', 'Age', 'Ethnicity', 'Location']]
y = df['Income']

poly_fit = PolynomialFeatures(degree=6)

X_poly = poly_fit.fit_transform(x)
pr_model = LinearRegression()
pr_model.fit(X_poly, y)
y_pred = pr_model.predict(X_poly)

y_new = pr_model.predict(poly_fit.fit_transform([[0,35,0,1]]))
print(y_new)
y_new = pr_model.predict(poly_fit.fit_transform([[1,35,0,1]]))
print(y_new)
#'''