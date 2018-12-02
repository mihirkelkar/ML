from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_boston
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

boston = load_boston()
print (boston.keys())
print (boston.DESCR)


bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos["PRICE"] = boston.target
print(bos.head())
print(bos.describe())

X = bos.drop("PRICE", axis=1)
Y = bos["PRICE"]

#  split into test and train dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


lm = LinearRegression()
lm.fit(X_train, Y_train)

Y_pred = lm.predict(X_test)
plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.show()

mse = mean_squared_error(Y_test, Y_pred)
print(mse)
