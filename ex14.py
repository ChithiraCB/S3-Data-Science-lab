import numpy as np
from sklearn.linear_model import LinearRegression

x=np.array([12,23,34]).reshape(-1,1)
y=np.array([78,90,9])
model=LinearRegression()
model.fit(x,y)
slope=model.coef_[0]
intercept=model.intercept_
print(slope)
print(intercept)