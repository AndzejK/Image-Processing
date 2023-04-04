import cv2
img=cv2.imread('galaxy.jpg')
# getting the size of img
print(img.shape) #(512, 512, 3) - Height, Width, Dimensions 

# Make a new img X % smaller than the original one, here we just calculate
def calc_size(scale_percen,height,width):
    new_width=int(width*scale_percen/100)
    new_heigh=int(height*scale_percen/100)
    return (new_heigh,new_width)

# test calc_size() method
print(calc_size(10,img.shape[0],img.shape[1]))

def resize(img_path,scale_perc,resized_path):
    img=cv2.imread(img_path)
    new_size=calc_size(scale_perc,img.shape[0],img.shape[1])
    resized_img=cv2.resize(img,new_size)
    cv2.imwrite(resized_path,resized_img)

resize('galaxy.jpg',50,'50x-smaller-galaxy.jpg')