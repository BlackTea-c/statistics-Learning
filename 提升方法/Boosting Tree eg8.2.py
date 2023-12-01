




import numpy as np



X_train=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y_train=np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05])
class AdaBoost:
    def __init__(self, tol=0.1, max_iter=10):
        # 训练中止条件 平方损失误差要求
        self.tol = tol
        # 最大迭代次数
        self.max_iter = max_iter
        # 初始化样本权重w
        self.G = []  # 弱分类器,(s,c1,c2)

    def build_stump(self,X,y): #决策树桩
        #m, n = np.shape(self.X)  #记录X 样本个数m 样本的特征维数n
        """最开始输入的是（xi,yi） i=1-N
        然后计算出m(s),找出min的; 切分点s的learning_rate为1,从1.5开始
        得到最优的s之后得到T1,所以此时f1=T1,计算残差r2i,T2就拟合r2i得到下一个s
        如此往复"""
        best_m_s=10000 #初始化m_s，无穷大
        best_s=0 #初始化s
        best_c1=0
        best_c2=0
        for s in [i+0.5 for i in range(1,10)]:
            #计算s划分出的两个区域R1，R2对应的c1,c2(c1,c2为使得平方误差最小的值,则ci=1/Ni * sum(yi))
            c1_,c2_=0,0
            N1,N2=0,0
            for i in range(len(y)):
                if X[i][0]<s:  #这里X[i][0]  i表示第i个样本，0表示样本的第一个分量，多维度情况请自行修改
                    c1_+=y[i]
                    N1+=1
                else:
                    c2_+=y[i]
                    N2+=1

            c1,c2=c1_/N1,c2_/N2
            ms_R1,ms_R2=0,0
            for i in range(len(y)):
                if X[i][0]<s:
                    ms_R1+=(y[i]-c1)**2
                else:
                    ms_R2+=(y[i]-c2)**2
            ms_next=ms_R1+ms_R2
            if ms_next<=best_m_s:
                best_m_s=ms_next
                best_s=s
                best_c1=c1
                best_c2=c2

        return best_s,best_c1,best_c2


    def T_(self,x,s,c1,c2): #决策树函数
        if x<s:
            return c1
        else:
            return c2

    def f_(self,x,G): #计算当前fm(x),给与x，得出y
        value=0
        for stump in G:
            s,c1,c2=stump
            value+=self.T_(x,s,c1,c2)
        return value

    def residual(self,G,X,y): #计算当前fm(x)的残差
        res=[]
        res_square_sum=0 #平方损失误差
        for i in range(len(y)):
            res_square_sum+=(y[i]-self.f_(X[i][0],G))**2
            res.append(y[i]-self.f_(X[i][0],G))
        return res,res_square_sum



    def fit(self,X,y):

        res_square=100
        res=y
        for epoch in range(self.max_iter):
            if res_square>=self.tol:
               #print(X,res)
               #print(self.build_stump(X,res))
               self.G.append(self.build_stump(X,res))
               res,res_square=self.residual(self.G,X,y)
               print("epoch:",epoch,"train_loss:",res_square)
            else:
                break


    def predict(self,x):
        pass
    def score(self,X,y):
        pass



Ada=AdaBoost(max_iter=100,tol=0.05)
Ada.fit(X_train,y_train)

#完成哈哈哈哈 简单~


