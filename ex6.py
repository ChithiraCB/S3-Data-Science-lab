from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
clf=DecisionTreeClassifier(max_depth=3)
clf.fit(x_train,y_train)
v=clf.predict(x_test)
print(v)
result=accuracy_score(y_test,v)
print("Accuracy : ",result)
report=classification_report(y_test,v,target_names=iris.target_names)
print("Classification report : ",report)


#to show the decision tree
fig=plt.figure(figsize=(10,8))
_=tree.plot_tree(clf,feature_names=iris.feature_names,class_names=iris.target_names,filled=True)
plt.show()