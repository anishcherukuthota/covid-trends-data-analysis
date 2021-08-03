import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv("./Data/final_data.csv", low_memory=False)


x = df[['Gender', 'Age', 'Ethnicity', 'Location']]
y = df['Income']
x_train = x[:-20]
x_test = x[-10:]
y_train = y[:-20]
y_test = y[-10:]
# print(x_test)

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)



pred_inc_m = regr.predict(x_test)

plt.scatter(x_test[-10:], y_test[-10:], color='black')
plt.plot(x_test,pred_inc_m,color='blue',linewidth=1)

plt.show()