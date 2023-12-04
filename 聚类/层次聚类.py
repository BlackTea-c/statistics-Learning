


import numpy as np

train_data=np.array([[1,2],[3,4],[5,6],[0,1],[2,2],[1,6]])

class agglomerative_clustering():
   def __init__(self):
       #存储结构还tm是个二叉树啊!!!
       self.category=[]


   def distance_D(self,X): #计算样本之间的距离，书上例题14.1直接给出了距离矩阵D.
       D=np.zeros((len(X),len(X)))
       for i in range(len(X)):
           for j in range(len(X)):
               D[i][j]=np.sum((X[i]-X[j])**2)**(1/2)
       return D


   def distance_i_j(self,Di,Dj,D):#eg. Di=[1,3] Dj=[2,5]
       #计算类i与类j的距离

       min_distance=10000
       for i in Di:
           for j in Dj:
               if D[i][j]<=min_distance:
                   min_distance=D[i][j]

       return min_distance
   def clustering(self,data):
       D=self.distance_D(data)


       stop=False
       G=[[i] for i in range(len(data))] #G=[[0],[1],[2].....] #当前类
       G_i_j={} #类i,j的距离
       for i in range(len(G)):
           for j in range(len(G)):
               if i<j:
                   G_i_j[D[i][j]]=[i,j]
       G_drop=[]#通过聚类抛弃的，不再计入的，就是说已经是G中某个元素的子集，那么就可以drop掉,不参与后面的距离计算
       while(stop==False): #D的迭代

           min_value=min(G_i_j)
           G_new = G_i_j[min_value]
           G.append(G_new)
           for index in  range(len(G)-1):
               for x in G[index]:
                   if x in G_new:
                       G_drop.append(index)

           G_i_j={}
           for i in range(len(G)):
               for j in range(len(G)):
                   if i<j and i not in G_drop:
                       G_i_j[self.distance_i_j(G[i],G[j],D)]=G[i]+G[j]

           if len(G[-1])==len(data):
               stop=True


       return G
   def clustering_D(self,D):


       stop=False
       G=[[i] for i in range(len(D))] #G=[[0],[1],[2].....] #当前类
       G_i_j={} #类i,j的距离
       for i in range(len(G)):
           for j in range(len(G)):
               if i<j:
                   G_i_j[D[i][j]]=[i,j]
       G_drop=[]#通过聚类抛弃的，不再计入的，就是说已经是G中某个元素的子集，那么就可以drop掉,不参与后面的距离计算
       while(stop==False): #D的迭代

           min_value=min(G_i_j)
           G_new = G_i_j[min_value]
           G.append(G_new)
           for index in  range(len(G)-1):
               for x in G[index]:
                   if x in G_new:
                       G_drop.append(index)

           G_i_j={}
           for i in range(len(G)):
               for j in range(len(G)):
                   if i<j and i not in G_drop:
                       G_i_j[self.distance_i_j(G[i],G[j],D)]=G[i]+G[j]

           if len(G[-1])==len(D):
               stop=True


       return G

cluster=agglomerative_clustering()

D=np.array([[0,7,2,9,3],[7,0,5,4,6],[2,5,0,8,1],[9,4,8,0,5],[3,6,1,5,0]])



G=cluster.clustering_D(D)

print(G) #成功！至少与书上相符合了。






