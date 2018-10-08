import cv2
from matplotlib import pyplot as plt,colors

img = cv2.imread('car.jpg')
matplot_imag=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Origninal Image",img)
print("Image Displayed")
#cv2.waitKey(0);
edges = cv2.Canny(img,100,200)

cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0);

cv2.DestroyAllWindows()
'''plt.figure(figsize=(10, 10))

plt.subplot(211)

plt.imshow(matplot_imag)
plt.title('Original Image')
plt.grid(False)

plt.subplot(212)
plt.imshow(edges)
plt.title('Edge Detected Image')
plt.grid(False)

plt.show()
'''
