import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


data = pd.read_excel("ENB2012_data.xlsx")
relevant_columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']
label = "Y1"

x = data[relevant_columns].values
y = data[label].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

print(data.describe())
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print(pd.DataFrame(regressor.coef_, relevant_columns, columns=['Coefficient']))

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(30)
df1.plot(kind='bar', figsize=(8, 8))
plt.grid(which='major', linestyle='-', linewidth='0.3', color='green')
plt.show()