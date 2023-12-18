from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
import matplotlib.pylab as plt
from sklearn.tree import plot_tree

cancer=load_breast_cancer()
x=cancer.data
y=cancer.target
x_test,x_train,y_test,y_train=train_test_split(x,y,random_state=42,test_size=0.2)
clf=DecisionTreeClassifier(max_depth=3)
clf.fit(x_train,y_train)
print(clf.predict(x_test))
v=clf.predict(x_test)
result=accuracy_score(y_test,v)
print("accuracy_score is",result)
report=classification_report(y_test,v,target_names=cancer.target_names)
print("classification report")
print(report)
plt.figure(figsize=(10,18))
plot_tree(clf,filled=True,feature_names=cancer.feature_names,class_names=cancer.target_names,rounded=True)
plt.show()