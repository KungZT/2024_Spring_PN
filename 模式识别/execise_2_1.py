import numpy as np
#Omiga = [np.array([[0,0,0]]).T,np.array([[0,1,1]]).T ,np.array([[1,0,1]]).T,np.array([[1,1,1]]).T]
Omiga = [np.mat([[0,0,0]]).T,np.mat([[0,1,1]]).T ,np.mat([[1,0,1]]).T,np.mat([[1,1,1]]).T]
Mean = np.mean(Omiga, axis=0)    # 0 列均值 1:行均值
print("M=",Mean)
N=len(Omiga)
Diff = np.array([(e-Mean)*(e-Mean).T for e in Omiga])
C=1/(N-1) * np.sum(Diff, axis=0)  #按书公式(2-17)
print("C=",C)
C_1 =  np.linalg.inv(C) # 求C的逆矩阵
print("inv(C)=",C_1)
for i,e_i in enumerate(Omiga,1):
    for j,e_j in enumerate(Omiga,1):
        if j>i:
            #按书公式(2-14)
            D_ij = np.sqrt((e_i - e_j).T *  C_1 * (e_i - e_j))#  *=元素按位相乘 换mat可以
            #D_ij =np.sqrt(np.dot(np.dot((e_i - e_j).T, C_1), (e_i - e_j))) # .dot()=矩阵相乘
            print("Dm[X%d,X%d]"%(i,j),"=",D_ij)
        #end-if
    #end-for_j
#end-for-i
            
