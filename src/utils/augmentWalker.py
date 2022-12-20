import glob
import os
import cv2
from scipy import ndimage
lst1  = glob.glob("D:\\Datasets\\sendata2\\image\\*r.png")
# lst1 = [item for item in lst1 

lst2  = glob.glob("D:\\Datasets\\sendata3\\raw_mask\\*.png")
#outF = open("F:\\Datasets\\bangalore\\index\\val.txt", "w")
print(len(lst1))
print(len(lst2))
# print(lst1[0])
# print(lst2[0])
c= 0


for path1 in lst1:
    print("processing ", path1)
    path2 = path1.replace("sendata2\image",r"sendata3\raw_mask")
    path2 = path2.replace("_r.png", "")
    print("editing ", path2)
    print()
    img = cv2.imread(path2+".png")
    rotated = ndimage.rotate(img, 270)
    cv2.imwrite(path2+"_r.png",rotated)
# for path2 in lst2:
#     rpath1 = path2.replace("sendata3\\image", "sendata2\\image")
#     path1 = rpath1.replace("_r", "")
#     if path1 not in lst1:
#         os.remove(path2)