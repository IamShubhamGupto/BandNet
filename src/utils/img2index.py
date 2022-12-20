# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:25:40 2019

@author: Shubham
"""

import glob
import cv2
import numpy as np
#import matplotlib.pyplot as plt
import scipy.misc
#import matplotlib.cm as cm
color2index = {
        (0,0,255) : 1,
        (0,0,0) : 0,
}
def im2index(im):
    """
    turn a 3 channel RGB image to 1 channel index image
    """
    assert len(im.shape) == 3
    height, width, ch = im.shape
    assert ch == 3
    m_lable = np.zeros((height, width), dtype=np.uint8)
    for w in range(width):
        for h in range(height):
            b, g, r = im[h, w,:]
            try:
                m_lable[h, w] = color2index[(r, g, b)]
            except:
                m_lable[h, w] = 0
    return m_lable

def main():
    lst  = glob.glob("D:\\Datasets\\sendata3\\raw_mask\\*.png")
    for item in lst:
#        item = "F:\\Datasets\\bangalore\\mask_RGB\\blr_13_01.png"
        name = item.replace("D:\\Datasets\\sendata3\\raw_mask\\","")
        print(name)
    #        name = name.replace(".png","")
        img = cv2.imread(item)
        index  = im2index(img)
#        print(index)
    #        cv2.imwrite("F:\\Datasets\\bangalore\\mask_RGB\\%"%name,index)
#        plt.imsave("F:\\Datasets\\bangalore\\mask_test2\\" + name, np.array(index/np.max(index)).reshape(549,549))
#        pngWriter.Writer("F:\\Datasets\\bangalore\\mask_test3\\" + name,
#                        np.array(index/np.max(index)).reshape(549,549), (-1, 549*2))
        scipy.misc.toimage(np.array(index/np.max(index)).reshape(549,549), cmin=0.0, cmax=255.0).save("D:\\Datasets\\sendata3\\mask\\" + name)
if __name__=='__main__':
    main()    