import cv2
import os
import numpy

columns=4
rows=2

horizontal_margin=40
vertical_margin=20

images=os.listdir('org_img')
# we have a list of the paths 
img_objects=[cv2.imread(f'org_img/{filename}') for filename in images]
print(len(images))

# Get a shape/size of one image 
size=cv2.imread('org_img/devops_QiYgZu6Ub8uXZkl7FizH_7.jpg').shape # 768, 768, 3 - Height,Width, Depth
# Define the size of the output image
output_size = (768, 768)
um=cv2.UMat(images)
resized_image = cv2.resize(um, output_size)
# we gonna *create* an empty whiet img, bg
gb_white_img=numpy.zeros((size[0]*rows+horizontal_margin*(rows+1),size[1]*columns+vertical_margin*(columns+1),size[2]),numpy.uint8)
#covert img from black to white
gb_white_img.fill(255)
# calculate the positioning of the pic
positions=[(x,y) for x in range(columns) for y in range(rows)]
print(positions)
for (pos_x,pos_y), resized_image in zip(positions,img_objects):
    x=pos_x*(size[1]+vertical_margin)+vertical_margin
    y=pos_y*(size[0]+horizontal_margin)+horizontal_margin
    gb_white_img[y:y+size[1],x:x+size[1]] = resized_image
cv2.imwrite("grid_w_res.jpeg",gb_white_img)