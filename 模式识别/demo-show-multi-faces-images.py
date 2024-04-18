#显示人脸图片 2023.3.10 o.y.x
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math


#--------------------------------------------- 
def read_faces_dataset(path=r".\dataset\faces\TestDatabase"):
    filenames=["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg",]
    fig, ax = plt.subplots(nrows=3,ncols=4,sharex='all',sharey='all')
    axes = ax.flatten()
    for i,fname in enumerate(filenames): 
        img = mpimg.imread(path+"\\"+fname)
        #if img.ndim == 3: img2 = img[:,:,0]
        axes[i].imshow(img,cmap='Greys')
        axes[i].text(0, 0,"filename="+fname, va='center',color = "r", ha='center')
        
    axes[0].set_xticks([])
    axes[0].set_yticks([])
    plt.tight_layout()
    plt.show() 
    return  
#----------------------------------
read_faces_dataset()
