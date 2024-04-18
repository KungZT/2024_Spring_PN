#显示手写体图片
import numpy
import matplotlib.pyplot as plt
import math

def read_local_MNIST_dataset(filename=r".\dataset\mnist.npz"):
    f = numpy.load(filename)
    x_train, y_train = f['x_train'][5000:11000], f['y_train'][5000:10000]
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
T = []
M = []
for i in range(6000):
    T[i] = X[i+5000]
    M[i] = Y[i+5000]
    #A[i] = A[i+5000]
    #B[i] = B[i+5000]
print("len(X)=%d,len(A)=%d"%(len(T),len(M)))
# print("X[0]=",X[1], " Y[0]=",Y[0])
# ShowImages(X,0,20)

