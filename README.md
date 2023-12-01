# 李航 《统计学习方法》 第二版 代码复现以及相关公式推导
#代码注释会写得很详细.

参考repo lihang-code



Bug修正

# 2023/11/30 提升方法 eg8.1 lihang-code运行出来最后score=0.4 而书上是1.0 原因是lihang-code里把G3(x)弄错了(应该为positive)，关键在于 if weight_error_positive <= weight_error_nagetive:  #这里应该改成<=  代码第60行。