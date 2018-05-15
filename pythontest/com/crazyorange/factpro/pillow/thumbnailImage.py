"""
压缩整个文件的图片 并保存到新的文件中
"""
###1.读取文件中的图片
###2.对图片进行压缩
###3.重新命名图片
###4.保存图片到新的文件
import math
import os
from PIL import Image

oldpath=input('请指定要压缩的文件夹').replace(" ","")
newPath=input('请指定要保存的文件').replace(" ","")
print("")
if not os.path.isdir(oldpath):
    print('请指定一个文件夹 : '+os.path.isdir(oldpath))
    exit()
else:
    ###获取文件夹下的所有文件
    files=os.listdir(oldpath)
    for file in files:
        ###不是文件夹才打开
        if not os.path.isdir(file):
            path=os.path.join(oldpath,file)
            print('open path abs: '+path)
            oldImage=Image.open(path)
            if max(oldImage.size[0],oldImage.size[1])>100:
                oldImage.thumbnail((100,100))
                if not os.path.exists(newPath):
                    os.makedirs(newPath)
                else:
                    oldImage.save(newPath.join(path))

