



import  numpy as np
#Regression Tree
#区域划分问题  还是要递归的放法


data=[[1,4.5],[2,4.75],[3,4.91],[4,5.34],[5,5.8],[6,7.05],[7,7.90],[8,8.23],[9,8.70],[10,9.0]]  #INDEX -1 为Y值
 #Y为连续变量



def Split_find(dataSet):


    min_outside={}
    index=0
    for split_pos in range(len(dataSet[0])-1): #选取切分量

       min_inside={}

       for split in range(len(dataSet)):   #SPLIT=[X1,X2,X3....,Y]
           right_region=[item for item in dataSet if item[split_pos]>dataSet[split][split_pos]]
           left_region =[item for item in dataSet if item[split_pos]<=dataSet[split][split_pos]]
           right_region_y=[item[-1] for item in right_region]
           left_region_y=[item[-1] for item in left_region]
           c_right=np.mean(right_region_y)
           c_left=np.mean(left_region_y)
           sum1=0
           sum2=0
           for y in right_region_y:
               sum1+=(y-c_right)**2
           for y in left_region_y:
               sum2+=(y-c_left)**2
           min_inside[split]=sum1+sum2


       min_outside[(min(min_inside,key=min_inside.get),index)]=min(min_inside.values())
       index+=1

    point,j=min(min_outside,key=min_outside.get)
    return  point,j,min(min_outside.values())


print(Split_find(data))









class Node:
    def __init__(self,split_point,right_region,left_region):

        self.split_point=split_point
        self.right_region=right_region
        self.left_region=left_region

class regression_tree:
    def __init__(self,root):
        self.root=root


    def create_tree(self,dataset): #停机条件为 检测新增划分能否降低误差


        split_point,split_dim,loss_f=Split_find(dataSet=data)















