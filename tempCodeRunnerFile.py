import cv2
import numpy as np
image = cv2.imread("butt.png")
print(image.shape)


B = image[:,:,0]
G = image[:,:,1]
R = image[:,:,2]

cv2.imshow("blue", B)
cv2.waitKey(0)