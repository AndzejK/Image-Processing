# Image -> on the screen represented in pixels format (1 - Matrix)
# and pixel is filled out with a colour (2 - Matrix)
# in order to represent colour we use 3 dif colors RGB (3 - Matrix)
# Combining all 3 Matrixs we get an <- Image

import cv2 
colour=cv2.imread("galaxy.jpg",0) # 1 is flag load in colours, 0 - load in grey
cv2.imwrite("galaxy-grey.jpg",colour)
print(colour)