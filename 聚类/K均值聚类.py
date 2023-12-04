

import random as rd
import numpy as np



data=np.array([[0,2],[0,0],[1,0],[5,0],[5,2]])
class K_clustering():
    def __init__(self,k):
        self.k=k
        self.category=[]


    def initial_category(self,data): #随机选取k个样本点作为类的中心
        sample=rd.sample(range(len(data)),self.k)
        for i in sample:
            self.category.append([i])


    def centre_G(self,G): #计算类的中心
        m=np.zeros(len(data[0]))
        for i in G:
             m+=data[i]
        m=m/len(G)
        return m
    def distance(self,X,Y):#计算两点距离,此处X，Y就不是索引了，是具体的
        return np.sum((X-Y)**2)**1/2

    def clustering(self,data):
        #self.initial_category(data) #随机选择
        self.category=[[0],[1]] #书上的选择

        stop=False


        G_drop=[]
        for i in self.category:
            G_drop.append(i[0])
        #将一开始的K个添加入，不计入后面的分类
        while(stop==False):
            m=[self.centre_G(G) for G in self.category] #得到各个类别的中心点


            for i in range(len(data)):
               store=[]
               for m_i in range(len(m)):
                  if i not in G_drop:
                        #print(i,m_i)
                        store.append(self.distance(data[i],m[m_i]))
               if store!=[]:
                  min_=store.index(min(store))
                  self.category[min_].append(i)
                  G_drop.append(i)

            if len(G_drop)==len(data):
                stop=True



cluster=K_clustering(k=2)
cluster.clustering(data)
print(cluster.category)