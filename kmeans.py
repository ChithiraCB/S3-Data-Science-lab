from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
import matplotlib.pyplot as  plt

cancer=load_breast_cancer()
x=cancer.data
y=cancer.target
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(x)

label=kmeans.labels_
centroids=kmeans.cluster_centers_

plt.scatter(x[:,0],x[:,1],cmap='viridis',marker='o',c=label,edgecolor="black")
plt.scatter(centroids[:,0],centroids[:,1],s=200,marker="x",c="red",label="centroids")
plt.xlabel(cancer.feature_names[0])
plt.ylabel(cancer.feature_names[1])

plt.show()

