import cv2
from scipy.cluster.vq import vq, kmeans
from matplotlib import pyplot as plt
import numpy as np

test_image = 'test.jpg'
img = cv2.imread(test_image)
hsv_image = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

plt.imshow(hsv_image)
plt.show()

hue, sat, val = hsv_image[:,:,0], hsv_image[:,:,1], hsv_image[:,:,2]

print sat
print len(sat)

print img.size

plt.figure(figsize=(10,8))
plt.subplot(311)
plt.subplots_adjust(hspace=.5)
plt.title("Hue")
plt.hist(np.ndarray.flatten(hue), bins=180)
plt.subplot(312)
plt.title("Saturation")
plt.hist(np.ndarray.flatten(sat), bins=128)
plt.subplot(313)
plt.title("Luminosity Value")
plt.hist(np.ndarray.flatten(val), bins=128)
plt.show()
