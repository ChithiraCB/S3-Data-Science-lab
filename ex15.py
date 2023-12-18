import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

ch=fetch_california_housing()
df=pd.DataFrame(data=ch.data,columns=ch.feature_names)
df['target']=ch.target
x=df.drop('target',axis=1)
y=df['target']
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)

lr=LinearRegression()
lr.fit(x_train,y_train)
v=lr.predict(x_test)
result=mean_squared_error(y_test,v)
print(result)