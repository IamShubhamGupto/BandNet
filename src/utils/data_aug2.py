# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:15:58 2019

@author: Shubham
"""

from scipy import ndimage
import cv2
import glob
from PIL import Image, ImageEnhance 
#im = Image.open("sample5.png")
#enhancer = ImageEnhance.Brightness(im)
#enhanced_im = enhancer.enhance(1.8)
#enhanced_im.save("enhanced.sample5.png")
#rotation angle in degree
lst  = glob.glob('F:\\Datasets\\RFJ\\raw_mask_rfj\\*.png')
for pic_path in lst:
#    img = Image.open(pic_path)
    img = cv2.imread(pic_path)
    img_name = pic_path.replace("F:\\Datasets\\RFJ\\raw_mask_rfj\\","")
#    for i in range(1,8):
#        rotated = ndimage.rotate(img,90*i)
    rotated = ndimage.rotate(img, 270)
    cv2.imwrite("F:\\Datasets\\RFJ\\mask\\"+img_name.replace(".png","_r.png"),rotated)
