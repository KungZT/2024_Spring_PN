import numpy as np
#第1组数据-来自例子
X1=np.array([0,0,0]).T
X2=np.array([1,0,1]).T
X3=np.array([1,1,0]).T
X4=np.array([1,0,0]).T

X5=np.array([0,1,1]).T
X6=np.array([0,0,1]).T
X7=np.array([0,1,0]).T
X8=np.array([1,1,1]).T
#第2组数据-来自教程
X1=np.array([0,0,0]).T
X2=np.array([0,0,1]).T
X3=np.array([0,1,1]).T
X4=np.array([0,1,0]).T #教程纠错 原(1,0,0) =改=> (0,1,0)

X5=np.array([1,0,0]).T #教程纠错 原(0,1,1) =改=> (1,0,0)
X6=np.array([1,0,1]).T
X7=np.array([1,1,0]).T
X8=np.array([1,1,1]).T

C1_0=[X1,X2,X3,X4]
C2_0=[X5,X6,X7,X8]

X=[]
#增广规范化模式向量 见P58-59
for c1 in C1_0:
    c=np.insert(c1,3,[1],axis=0)
    X.append(c)
for c2 in C2_0:
    c=np.insert(c2,3,[1],axis=0)
    c = c*(-1)
    X.append(c)
    
print("X=",X)

W=[]
W.append(np.array([1,1,1,1]))

c=0.5
k=0 #从0开始这里的W[0]对应书上的W(1)
ok_cnt=0
while True:
    pos= k % len(X)
    JX=np.dot(W[k].T,X[pos])
    if JX>0:
        W.append(W[k])
        ok_cnt +=1
    else:
        new_W=W[k]+c*X[pos]
        W.append(new_W)
        ok_cnt =0
        
    k += 1
    if ok_cnt >= len(X):#连续分类的正确数目等于样本数(即所有样本都被正确分类)
        break
#end-while

#输出训练过程的W变化值
for i,w in enumerate(W):
    print("W[%d]="%i,w)
    
