#朴素贝叶斯

import numpy as np

# 创建特征1（0到5的整数）
feature_1 = np.array([0, 1, 2, 3, 4, 5, 2, 3, 1, 4,
                      0, 5, 3, 2, 1, 4, 5, 0, 2, 1,
                      3, 4, 5, 1, 0, 4, 3, 2, 5, 1,
                      0, 2, 3, 4, 5, 0, 1, 2, 3, 4,
                      5, 3, 1, 4, 2, 5, 0, 1, 4, 3])

# 创建特征2（S，M，L三选一）
feature_2 = np.array(['S', 'M', 'L', 'S', 'M', 'L', 'M', 'L', 'S', 'M',
                      'L', 'S', 'S', 'M', 'L', 'M', 'L', 'S', 'M', 'L',
                      'S', 'M', 'L', 'S', 'M', 'L', 'S', 'M', 'L', 'S',
                      'M', 'L', 'S', 'M', 'L', 'S', 'M', 'L', 'S', 'M',
                      'L', 'S', 'M', 'L', 'S', 'M', 'L', 'S', 'M', 'L'])

# 合并特征
data_x = np.column_stack((feature_1, feature_2))
# 创建对应的标签
data_y = np.array([1, -1, -1, -1, -1, -1, 1, -1, 1, -1,
                   1, -1, -1, -1, 1, -1, 1, -1, 1, -1,
                   1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
                   1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
                   1, -1, 1, -1, 1, -1, 1, -1, 1, -1])


#计算目标  max (P(Y=1|X),P(Y=-1|X)



#做一下训练集验证集划分

train_data=data_x[:40]
test_data=data_x[40:50]
train_labels=data_y[:40]
test_label=data_y[40:50]


#计算先验概率以及条件概率



def get_one(data):
    list=[]
    for i in data:
        if i not in list:
            list.append(i)
    return list
label=get_one(train_labels)
f1=get_one(feature_1)
f2=get_one(feature_2)
print(label)
print(f1)
print(f2)






#计算P(yi)
def P_y(label,data):
    pos=np.zeros(len(label))
    for l in data:
        if(l==label[label.index(l)]):
            pos[label.index(l)]+=1
    return pos

#计算条件概率
def P_x_y(feature,label,data_feature):  #feature x在某维度上的所有取值
    pos=np.zeros(len(data_feature))
    for i in range(data_feature):
        pass


#暂时略过，今天脑子有点瓦特了。











