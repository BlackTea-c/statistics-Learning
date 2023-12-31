# 感知机（Perceptron）教程

## 感知机简介
感知机是最简单的人工神经网络形式之一，用于解决二元分类问题。

## 感知机的工作原理

### 大致思想
- 感知机接收多个输入（x1, x2, ..., xn），每个输入都有一个对应的权重（w1, w2, ..., wn）。
- 输入和权重相乘并求和，加上偏置项（bias）。
- 将得到的结果传递给激活函数（通常为阶跃函数），输出最终的分类结果。

### 数学原理
感知机的数学表达式如下所示：
- 输入和权重的线性组合: \( \sum_{i=1}^{n} w_i \cdot x_i + b \)
- 阶跃函数： \( f(x) = \begin{cases} 1, & \text{if } \sum_{i=1}^{n} w_i \cdot x_i + b > 0 \\ 0, & \text{otherwise} \end{cases} \)

### 权重更新算法
感知机的学习规则使用简单的权重更新算法，通过随机梯度下降（Stochastic Gradient Descent）来更新权重和偏置项以最小化误差。
在每一轮训练中，对于每个输入样本（xi）和对应的真实标签（yi），权重更新规则如下：
- \( w_i = w_i + \alpha \cdot (y_i - \hat{y_i}) \cdot x_i \)，其中 \(\alpha\) 是学习率（learning rate），\(\hat{y_i}\) 是预测值，\(y_i\) 是真实值。
- \( b = b + \alpha \cdot (y_i - \hat{y_i}) \)

### 对偶形式
感知机还有一种对偶形式，使用输入数据和标签的内积（dot product）计算权重更新。
对于权重更新，可以使用以下公式进行更新：
- \( w_i = w_i + \alpha \cdot (y_i - \hat{y_i}) \cdot x_i \)
- \( b = b + \alpha \cdot (y_i - \hat{y_i}) \cdot 1 \)，其中 \(x_i\) 和 \(1\) 是输入数据和偏置项，通过内积计算。



## 总结
感知机是最简单的神经网络形式之一，通过调整权重和偏置项，它可以学习并完成简单的二元分类任务。

## 文件解释
eg1.py 原始问题
eg_dual_form.py 对偶形式（起始就是计算下Gram矩阵）
