import cv2
import numpy as np

img = cv2.imread('car.jpg',0)
rows,cols = img.shape
cv2.imshow('Orginal Image (Press any key to continue)',img)
cv2.waitKey(0)
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Pixel Shifted Image( Press any key to continue)',dst)
cv2.waitKey(0)


M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Rotated Image (Press any key to continue)',dst)
cv2.waitKey(0)
cv2.DestroyAllWindows()
