import cv2
from matplotlib import pyplot as plt,colors
from numpy import random
img = cv2.imread('home.jpeg')
cv2.imshow("image",img)
matplot_imag=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("HSV Image", hsv)
#cv2.imshow("GreyScaleImage", img_gray)

plt.figure(figsize=(10, 8))

plt.subplot(121)

plt.imshow(matplot_imag)
plt.title('Original Image')
plt.grid(False)

plt.subplot(122)
plt.imshow(colors.rgb_to_hsv(matplot_imag))
plt.title('HSV Image')
plt.grid(False)

plt.show()
