#最大最小距离进行聚类
import numpy as np
theta = 1/3  #比例因子θ
#----------------------
def dist_point_to_set(Xi,Zj): #定义样本Xi到类Zj(集合)的距离
    Z_vect = np.array(Zj) #py列表转为 np矩阵    
    Z_mean = np.mean(Z_vect, axis=0)    # 0 列均值 1:行均值 求类Zj的均值向量 
    diff_vect = Xi - Z_mean
    dd = np.dot(diff_vect.T,diff_vect)
    d=np.sqrt(dd)
    return d[0][0] #转为标量
#end-def
#----------------------
def dist_point_to_point(Xi,Xk): #定义样本Xi到样本Xk的距离
    diff_vect = Xi - Xk
    dd = np.dot(diff_vect.T,diff_vect)
    d=np.sqrt(dd)
    return d[0][0] #转为标量
#end-def
#----------------------
samles=[[0,0],[1,0],[2,3],[3,6],[4,6],[6,3],[7,3],[6,4]]   
X=[np.array([e]).T for e in samles]

i =  0 #选择初始为0的元素作为初始分类
Z=[] #
Z.append([X[i],]) #取样本Xi作为第一个聚类中心 Z1
#计算样本中与Z0最大距离的点
dist_points_to_Z0=[dist_point_to_set(xi,Z[0]) for xi in X]
pos = np.argmax(dist_points_to_Z0) #求最大值的索引（位置）
max_dist = dist_points_to_Z0[pos]
print("max dist=%.3f,point=X%d"%(max_dist,pos))
Z.append([X[pos],]) #Z2
Z_ids=[[0],[pos]] #以样本集序号的表示的聚类集
c=len(Z_ids) #置当前类数目为1

T=theta*max_dist #根据θ计算T 
left_points =list(range(len(X)))
del left_points[0]
del left_points[pos]

print(left_points)
while True:
    min_dists=[0]*len(left_points) #存储最小距离的列表
    for i,e in enumerate(left_points):
        k = left_points[i]
        Xk=X[k]
        dist_xk_to_Z_list=[dist_point_to_set(Xk,Zi) for Zi in Z]
        min_pos = np.argmin(dist_xk_to_Z_list)
        min_dists[i] = dist_xk_to_Z_list[min_pos] #寻找最小距离值
    #end-for
    max_pos = np.argmax(min_dists) #选择距离最大的点
    max_dist = min_dists[max_pos]
    if max_dist > T:
        idx = left_points[max_pos]
        Z.append([X[idx],])
        Z_ids.append([idx])
        
print("-----------\nclass details:")
for idx,z in enumerate(Z,1):
    print("c%d="%idx,z)
print("Z=",Z_ids)
print("-----------\nclass summary:")
for i,e in enumerate(Z_ids,1): 
    print("c%d:"%i,["X%d"%j for j in e])

    
    
            
    


     
