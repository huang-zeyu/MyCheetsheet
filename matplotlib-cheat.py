import numpy as np
from matplotlib import pyplot as plt

#==========绘制折线图==============
# 函数值，可以是list or arr
K1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18]
K2 = [10, 12, 14, 16, 18, 1, 2, 4, 6, 8]

# 范围是arg1到arg2，一共取arg3个数，endpoint指是否包含arg2自己。
X = np.linspace(0, len(K1)-1, len(K1), endpoint=True)

# subplot直接每个plot前调用，指示位置
plt.subplot(1,2,1)
plt.plot(X,K1,color='red', label="error rate")
plt.legend()
# x轴上显示的坐标，和绘图的x坐标不相关
plt.xticks([i for i in range(len(K1))])


#==========绘制散点图==============
plt.subplot(1,2,2)

# s 点的大小，c 点的颜色
plt.scatter(X,K2,s=10,c='red')
plt.show()