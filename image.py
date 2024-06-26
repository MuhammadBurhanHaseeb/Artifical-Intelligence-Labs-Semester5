import cv2
import numpy as np
image = cv2.imread("butt.png")
print(image.shape)


B = image[:,:,0]
G = image[:,:,1]
R = image[:,:,2]

cv2.imshow("blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
cv2.waitKey(0)

z = np.zeros((image.shape[0],image.shape[1]))
image[:,:,1] = z
image[:,:,2] = z
cv2.imshow("Blue", image)
cv2.waitKey(0)

ROI = image[0:100, 0:50 , :]
cv2.imshow("ROI", ROI)
cv2.waitKey(0)

image[100:200, 50:100 , :] = ROI
