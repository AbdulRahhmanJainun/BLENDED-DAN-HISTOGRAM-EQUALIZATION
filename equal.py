import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def equalization(image1,op1,image2,op2):
    hist,bins = np.histogram(image.fllaten(),bins=256,range=[0,256])
    cdf = hist.cumsum()
    cdf_normalized =(cdf/cdf.max()) *255
    imgEqual = np.interp(image.flatten(),bins[:-1],cdf_normalized)
    return imgEqual.reshape(image.shape).astype(np.uint8)

img1 = img.imread("C:\\gambar\\istockphoto-1317323736-612x612.jpg")
hist,bins = np.histogram(image.fllaten(),bins=256,range=[0,256]=)

   

    
