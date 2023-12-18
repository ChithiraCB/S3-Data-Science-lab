from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import pandas as pd

data=pd.read_csv('Salary_Data.csv')
x=data['YearsExperience'].values.reshape(-1,1)
y=data['Salary'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

nb=LinearRegression()
nb.fit(x_train,y_train)
print(nb.predict(x_test))
v=nb.predict(x_test)
result=r2_score(y_test,v)
print(result)
plt.scatter(x_test,y_test,color="black",label="datapoint")
plt.plot(x_test,v,color="blue",linewidth="3")
plt.xlabel('YearsExperience')
plt.ylabel('salary')
plt.legend()
plt.show()

