# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:36:42 2019

@author: Shubham
"""

import glob
lst  = glob.glob("D:\\Datasets\\sendata3\\image\\*.png")
outF = open("D:\\Datasets\\sendata3\\index\\trainval.txt", "w+")

delete_list = [".png",".jpg",
               "D:\\Datasets\\sendata3\\image\\"]
for line in lst:
  # write line to output file
  for word in delete_list:
        line = line.replace(word, "")
  outF.write(line)
  outF.write("\n")
outF.close()