#近邻聚类算法 2.3.1 P18 o.y.x 2023.11.2
import numpy as np

def dist(Xi,Zj): #定义样本Xi到类Zj的距离
    Z_mat = np.array(Zj) #py列表转为 np矩阵    
    Z_mean = np.mean(Z_mat, axis=0)    # 0 列均值 1:行均值 求类Zj的均值向量
    #print("Zj=",Zj," mean=",Z_mean)
    diff_vect = Xi - Z_mean
    dx2 = np.dot(diff_vect.T,diff_vect)
    d=np.sqrt(dx2)
    #print("d=",d)
    return d[0][0]
    
d=[[0,0],[1,0],[2,3],[3,6],[4,6],[6,3],[7,3],[6,4]]    
#X = [np.array([[0,0]]).T,np.array([[1,0]]).T,np.array([[2,3]]).T,np.array([[3,6]]).T,
#           np.array([[4,6]]).T,np.array([[6,3]]).T,np.array([[7,3]]).T,np.array([[6,4]]).T,]
X=[np.array([e]).T for e in d]
i =  0 #选择初始为0的元素作为初始分类
T=3.0 #阈值T
print("T=%.3f\n-----------\n"%T)
Z=[] #
Z.append([X[i],]) #取样本Xi作为第一个聚类中心
Z_indexs=[[0]] #以样本集序号的表示的聚类集
c=1 #置当前类数目为1
DEBUG = True #是否进行调试输出
for k,Xk in enumerate(X,0): #下标从1开始
    if k==0:continue  #跳过 X0
    # 先计算当前样本Xk到Z中各个类的距离
    d_list =[dist(Xk,Z[j]) for j in range(len(Z))]
    if DEBUG: #调试输出语句
        dist_str = ["%.2f"%e for e in d_list]
        cnt_list=[len(z) for z in Z]
        print("No.%d X%d--to-->{Z,c=%d,counts=%s}: dist_list = "%(k,k,c,str(cnt_list)),dist_str)
    #end-if
        
    if min(d_list) > T: #最小值都是>T则满足 P18末行条件
        Z.append([Xk]) #新增样本单独成类[]
        Z_indexs.append([k]) 
        c +=1 #类别数+1  c==len(Z)
    else: #Z中存在某些类与本样本距离小于T
        pos = np.argmin(d_list) #求最小值的索引（位置）
        Z[pos].append(Xk) #原有类中添加一个新成员
        Z_indexs[pos].append(k) 
        
#end-for
print("-----------\nclass details:")
for idx,z in enumerate(Z,1):
    print("c%d="%idx,z)
print("Z=",Z_indexs)
print("-----------\nclass summary:")
for i,e in enumerate(Z_indexs,1): 
    print("c%d:"%i,["X%d"%j for j in e])

    
    
            
    


     
