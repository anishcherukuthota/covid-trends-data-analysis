import pandas as pd
from sklearn import linear_model

df = pd.read_csv("/home/anish/PycharmProjects/asdrp/data/final_data.csv", low_memory=False)

x = df[['Gender', 'Age', 'Ethnicity', 'Location']]
y = df['Income']

regr = linear_model.LinearRegression()
regr.fit(x, y)

pred_inc_m = regr.predict([[0,35,0,1]])
pred_inc_f = regr.predict([[1,35,0,1]])

print(pred_inc_m)
print(pred_inc_f)