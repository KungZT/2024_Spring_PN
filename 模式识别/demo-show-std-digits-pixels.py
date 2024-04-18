#显示图片的值
import numpy
import matplotlib.pyplot as plt
import math
import cv2
#--------------------------------------
#读入标准样本的图像数据
def read_std_digit_images(src_dir):
    filenames_list =["0.png","1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png"]
    images_list=[None]*len(filenames_list)
    for idx,filename in enumerate(filenames_list):
        pathfilename =src_dir+"\\"+filename 
        print(pathfilename)
        img_data = cv2.imread(pathfilename,cv2.IMREAD_GRAYSCALE) #读取一幅标准图片的数据
        if False:
            cv2.imshow('image%d'%idx,img_data)
            cv2.waitKey(0) 
        images_list[idx] = img_data
        print(img_data.shape)
    return images_list        
    
#----------------------------------
#读入数据集
std_digits_imgs=read_std_digit_images(src_dir=r".\dataset\std_digits")

for img in std_digits_imgs:
    print("图片维度:",img.shape)
    #遍历第0幅图的每行，输出像素值
    rowstr=''
    for line,row in enumerate(img):#每行line=0,..,27
        for e in row:
            rowstr +="%02x "%e
        print(rowstr)
    
    plt.imshow(img,cmap='Greys')
    plt.show()
