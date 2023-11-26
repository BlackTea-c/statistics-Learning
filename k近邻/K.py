#K近邻算法

#构造kd树。
import numpy as np



#数据集
x=np.array([[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]])
y=np.array([1,1,2,3,3,4])
k=1

#度量函数
def Euclidean_distance(x,y):   #欧式距离
    distance=0
    for i in range(len(x)):
        distance+=(x[i]-y[i])**2
    return  distance**(1/2)

def Manhattan_distance(x,y):  #曼哈顿距离
    distance=0
    for i in range(len(x)):
        distance+=abs(x[i]-y[i])

def max_distance(x,y):  #Loo距离
    return max(abs(x-y))




#构建结点对象
class KdNode(object):
    def __init__(self, dom_elt, dim=0, left=None, right=None):
        self.dom_elt = dom_elt  # k维向量节点(k维空间中的一个样本点) 具体值
        self.dim = dim  # 整数（进行分割维度的序号）
        self.left = left  # 该结点分割超平面左子空间构成的kd-tree
        self.right = right  # 该结点分割超平面右子空间构成的kd-tree


class KdTree(object):
    def __init__(self, data):
        k = len(data[0])  # 数据维度

        # 按第dim维划分数据集exset创建KdNode
        def _CreateNode(dim, data_set):
            if not data_set:  # 数据集为空
                return None

            # 按要进行分割的那一维数据排序
            data_set.sort(key=lambda x: x[dim])  #key=排序依据  reverse=升序降序False升序
            split_pos = len(data_set) // 2
            median = data_set[split_pos]  # 中位数分割点
            split_next = (dim + 1) % k  # cycle coordinates

            # 递归的创建kd树
            return KdNode(
                median,
                dim,
                _CreateNode(split_next, data_set[:split_pos]),  # 创建左子树
                _CreateNode(split_next, data_set[split_pos + 1:]))  # 创建右子树
        #函数嵌套

        self.root = _CreateNode(0, data)  # 从第0维分量开始构建kd树,返回根节点






# kdTree的前序遍历
def preorder(root):
    print(root.dom_elt)
    if root.left:  # 节点不为空
        preorder(root.left)
    if root.right:
        preorder(root.right)

data = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
kd = KdTree(data)
print(kd.root.right.left.left)



















