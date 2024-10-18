import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def equalization(image1,op1,image2,op2):
    hist,bins = np.histogram(image)
    img2 = image2.astype(np.float32)
    imgBlend = (img1*op1)+(img2*op2)
    imgBlend = np.clip(imgBlend,0,255)
    return imgBlend.astype(np.uint8)
