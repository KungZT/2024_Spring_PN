#显示图片的值
import numpy
import matplotlib.pyplot as plt
import math
#--------------------------------------
def read_local_MNIST_dataset(filename=r".\dataset\mnist\mnist.npz"):
    f = numpy.load(filename)
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']
    f.close()
    return (x_train, y_train), (x_test, y_test)


#----------------------------------
#读入数据集
(X,Y),(A,B) = read_local_MNIST_dataset()

#取第idx幅图

img_idx = 0 #1 29
img_matrix =X[img_idx] 

print("图片维度:",img_matrix.shape)

#遍历第0幅图的每行，输出像素值
for row in img_matrix:
    #print(row.shape);print(row)
    rowstr=''
    for e in row:
        if e>0:
            rowstr +="%02x "%e
        else:
            rowstr +="   "
            
    print(rowstr)
    
plt.imshow(img_matrix,cmap='Greys')
plt.show()
