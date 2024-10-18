import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Abdul Rahman Jainun
def blend(image1, op1, image2, op2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)
    imgBlend = (img1 * op1) + (img2 * op2)
    imgBlend = np.clip(imgBlend, 0, 255)
    return imgBlend.astype(np.uint8)

img1 = img.imread(r"C:\\gambar\\images.jpg")
img2 = img.imread(r"C:\\gambar\\istockphoto-1317323736-612x612.jpg")
img1_resized = np.array(Image.fromarray(img1).resize((img2.shape[1], img2.shape[0])))

imgBlend = blend(img1_resized, 0.3, img2, 0.7)
plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(img1_resized)
plt.title('Gambar 1 (Resize)')
plt.subplot(3,2,3)
plt.imshow(img2)
plt.title('Gambar 2')
plt.subplot(3,2,5)
plt.imshow(imgBlend)
plt.title('Hasil Blend')
plt.show()
