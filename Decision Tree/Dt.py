#Decision Tree

#entropy越大 不确定性越高。
import numpy as np
import pandas as pd
import math
data_f=pd.read_excel('E:/Project_YOLO/Stattitiscs_learning_method/Decision Tree/data.xlsx')


#信息增益: 特征A对训练数据集D的信息增益G（D,A）=H(D)-H(D|A)

#信息熵

print(data_f)

def entropy(X,data_):  #random variable
    data=data_[X]
    l=[]
    for i in data:
        if i not in l:
            l.append(i)
    b=np.zeros(len(l))
    for i in data:
       if(i==l[l.index(i)]):
           b[l.index(i)]+=1
    c=b/len(data)
    d=[]
    for i in c:
        if i==0:
            d.append(0)
        else:
            d.append(math.log(i,2))  #以2为底
    d=np.array(d)

    return -np.sum(c*d)


def condi_entropy(condition,X,data):
    l=[]
    for i in data[condition]:
        if i not in l:
            l.append(i)
    b = np.zeros(len(l))
    for i in data[condition]:
        if (i == l[l.index(i)]):
            b[l.index(i)] += 1
    c = b / len(data[condition])  #得到H（Di）

    d=[]
    for fe in l:
        d.append(entropy(X,data[data[condition]==fe]))

    d=np.array(d)
    return  sum(c*d)




g1=entropy('是否发放贷款',data_f)-condi_entropy('年龄','是否发放贷款',data_f)
print(g1)
g2=entropy('是否发放贷款',data_f)-condi_entropy('有工作','是否发放贷款',data_f)
print(g2)
#....编辑成功！！

features=data_f.columns[1:-1]
labels=[]
for label in features:
    labels.append(label)
#ID3算法   (C4.5算法则采用信息增益比来选择特征)
def feature_get(dataset, labels):  # 传入数据集与标签
    g_d_a = []
    for label in labels:
        g_d_a.append(entropy('是否发放贷款', dataset) - condi_entropy(label, '是否发放贷款', dataset))
    index = g_d_a.index(max(g_d_a))
    optimum_label = labels[index]
    return optimum_label, index, g_d_a[index]


def splitdata(dataSet, bestfeature):  # 按照optimum_label划分数据集
    bestfeature_value = []
    splitset = {}
    for value in dataSet[bestfeature]:
        if value not in bestfeature_value:
            bestfeature_value.append(value)
    for condition in bestfeature_value:
        splitset[condition] = (dataSet[dataSet[bestfeature] == condition])  # 得到{Di}

    return splitset

class Node:
    def __init__(self,feature,subtree):
        self.feature=feature  #feature = 类 or 类下的取值？
        self.subtree=subtree




class DS_Tree:
    def __init__(self,data):
        self.root=None
        k=len(data.columns)



    def createtree(self,dataSet, labels, thresh=0):  # 默认阈值为0
                                                           # sublabels是往下延展是用到的特征集合，每次使用一个特征就要删取该特征

       #首先判断是否所有实例都属于一类：
       ifallinclass=[item for item in dataSet['是否发放贷款']]
       if len(set(ifallinclass))==1:
           return  Node(ifallinclass[0],subtree=None)
           #实例就只有一类则直接返回该类

       #如果特征没了，则用最大的类值作为节点

       if len(labels)==0:

           return Node(max(ifallinclass, key=ifallinclass.count),subtree=None)
       bestfeature, i, score =feature_get(dataSet,labels)

       if(score>thresh):
           dict=splitdata(dataSet,bestfeature)
           labels.remove(bestfeature)
           subnode=[]
           for condition,dataset in dict.items():
               subnode.append(self.createtree(dataset, labels))


           return Node(bestfeature,subnode)




       else:
           return  Node(max(ifallinclass, key=ifallinclass.count),subtree=None)


def preorder(root):
    print(root.feature)
    if root.subtree!=None:
        for node in root.subtree:
            preorder(node)


TREE=DS_Tree(data_f)
TREE.root=TREE.createtree(dataSet=data_f,labels=labels)


preorder(TREE.root)


#终于算是编出来了 泪目= =||






