#在数据总体上进行的PCA成为总体PCA，在有限样本上进行的PCA为样本PCA；实际运用基本都是样本PCA，因为均值，方差基本都是根据样本估计出来

import pandas as pd

data=pd.read_excel('data.xlsx')



class PCA():
    def __init__(self):
        pass

    def R(self):#计算样本相关矩阵
        pass

    def nata(self): #对样本相关矩阵进行特征值分解，得到相关矩阵的特征值并按大小排序
        pass
    def contri(self):#计算主成分的贡献率
        pass
    def fit(self):
        pass

#以后复习的时候再具体写