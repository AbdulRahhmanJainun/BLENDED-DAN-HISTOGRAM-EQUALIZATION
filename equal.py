import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

# Abdul Rahman jainun

def equalization(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()  
    cdf_normalized = (cdf / cdf.max()) * 255 
    imgEqual = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    return imgEqual.reshape(image.shape).astype(np.uint8)


image = img.imread(r"C:\\gambar\\istockphoto-1317323736-612x612.jpg")
hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

imgEqual = equalization(image)
hist_e, bins_e = np.histogram(imgEqual.flatten(), bins=256, range=[0, 256])

plt.figure(figsize=(10,10))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Gambar Asli')
plt.subplot(2, 2, 2)
plt.plot(hist)
plt.title('Histogram Gambar Asli')
plt.subplot(2, 2, 3)
plt.imshow(imgEqual, cmap='gray')
plt.title('Gambar Setelah Ekualisasi')
plt.subplot(2, 2, 4)
plt.plot(hist_e)
plt.title('Histogram Gambar Setelah Ekualisasi')

plt.show()
