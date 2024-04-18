import numpy
import matplotlib.pyplot as plt
import math
from collections import Counter

# 示例列表
my_list = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 3, 2, 1]

# 使用Counter统计数字出现的次数
counts = Counter(my_list)

# 打印结果
print(counts)


def read_local_MNIST_dataset(filename=r".\dataset\mnist.npz"):
    f = numpy.load(filename)
    x_train, y_train = f['x_train'][5000:11000], f['y_train'][5000:11000]    
    x_test, y_test = f['x_test'], f['y_test']
    f.close()
    return (x_train, y_train), (x_test, y_test)

#--------------------------------------------- 
def ShowImages(dataset,begin_pos,count):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 显示负号
    
    col = 10    
    row = math.ceil(count/col)
    fig, ax = plt.subplots(nrows=row,ncols=col,sharex='all',sharey='all')
    
    ax = ax.flatten()
    for i in range(count):
        idx = begin_pos+i
        img = dataset[idx]
        ax[i].imshow(img,cmap='Greys')
        ax[i].text(0, 0,"idx="+str(idx), va='center',color = "r", ha='center')
    #end-for
        
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show() 

#----------------------------------
(X,Y),(A,B) = read_local_MNIST_dataset()

# print("len(X)=%d,len(A)=%d"%(len(X),len(A)))
print("X[0]=",X[1], " Y[0]=",Y[0])
# ShowImages(X,0,20)
# counts = Counter(Y)
# print(counts)