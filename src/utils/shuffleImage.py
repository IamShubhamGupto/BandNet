# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:37:05 2019

@author: Shubham
"""

from sklearn.utils import shuffle
from numpy import array
#from sklearn.model_selection import KFold
#import os
lines = [line.rstrip('\n') for line in open("D:\\Datasets\\sendata3\\index\\trainval.txt")]

lines = shuffle(lines,random_state=19)
train = lines[0:1146]
val = lines[1146:1446]
outF1 = open("D:\\Datasets\\sendata3\\index\\train.txt", "w")
for traini in train:
    outF1.write(traini)
    outF1.write("\n")
outF1.close()

#outF2 = open("F:\\Datasets\\sendata\\index\\trainval.txt", "w")
#for ri in r2:
#    outF2.write(ri)
#    outF2.write("\n")
#outF2.close()

outF3 = open("D:\\Datasets\\sendata3\\index\\val.txt", "w")
for vali in val:
    outF3.write(vali)
    outF3.write("\n")
outF3.close()
#print(lines)