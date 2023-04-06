import cv2
import numpy as np
bg=cv2.imread('org_img/humans-10.jpeg')
fg=cv2.imread('org_img/green-bg.jpg')

# Now I need to find the value of this green background
fg[40,40] # printing a px based on this coordinates  - [27 150  54]
width=fg.shape[1] # getting width
height=fg.shape[0] # getting height
r1 = np.arange(23, 42)
r2 = np.arange(100, 210)
r3 = np.arange(30, 80)
#keep the same size as bg
resized_bg=cv2.resize(bg,(width,height))

for i in range(width):
    for j in range(height):
        pixel=fg[j,i]# current pixel
        #finding that green pixel
        if (pixel[0] in r1) and (pixel[1] in r2) and (pixel[2] in r3):
            #then we access foreground, current pixel and we change it
            fg[j,i]=resized_bg[j,i]

cv2.imwrite('output_v7.jpg',fg)