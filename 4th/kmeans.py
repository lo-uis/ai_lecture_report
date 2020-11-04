from sklearn import datasets
from sklearn.cluster import KMeans

sett = [[0,0], [0,1], [0,2], [4,0], [4,1], [4,2]] #set

num = 2 #define clasters

cls = KMeans(n_clusters = num) #Cluster
pred = cls.fit_predict(sett)

centers = cls.cluster_centers_ #Display the contents
for center in centers:
        print(center)