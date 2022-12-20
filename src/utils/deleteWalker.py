# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:11:45 2019

@author: Shubham
"""

import glob
import os
lst1  = glob.glob("D:\\Datasets\\sendata2\\image\\*.png")
# lst1 = [item for item in lst1 

lst2  = glob.glob("D:\\Datasets\\sendata3\\image\\*.png")
#outF = open("F:\\Datasets\\bangalore\\index\\val.txt", "w")
print(len(lst1))
print(len(lst2))
print(lst1[0])
print(lst2[0])
c= 0

for path2 in lst2:
    path1 = path2.replace("sendata3\\image", "sendata2\\image")
    if path1 not in lst1:
        os.remove(path2)
        # c+=1
        # print("will delete", path2) 
# print(c)
#delete_list = ["F:\\Datasets\\bangalore\\mask\\","F:\\Datasets\\bangalore\\image\\"]
# for line2 in lst2:
# #    for word in delete_list:
#     line1 = line2.replace("sendata3\\raw_mask", "sendata2\\image")
#     print(line1)
#     if line1 not in lst1:
#         print("will delete",line2)
#     #    os.remove(line2) 
