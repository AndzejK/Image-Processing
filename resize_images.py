import cv2 
from pathlib import Path

path_to_org_img=Path("org_img")
path_to_converted_img=Path("conver_img/")

def calc_size(scale_percen,height,width):
    print(height,width)
    new_width=int(width*scale_percen/100)
    new_heigh=int(height*scale_percen/100)
    print(new_heigh,new_width)
    return (new_heigh,new_width)

def resize(img_path,scale_perc,resized_path):
    img=cv2.imread(img_path)
    new_size=calc_size(scale_perc,img.shape[0],img.shape[1])
    resized_img=cv2.resize(img,new_size)
    cv2.imwrite(resized_path,resized_img)


for file_path in path_to_org_img.glob('*'): #the "*"" wildcard matches all file names
    name=file_path.stem[:6]
    
    resize(str(file_path),50,f'conver_img/'+name+'-50x-smaller.jpg')
    #cv2.imread(str(file_path),0)
    #cv2.imwrite(f"{path_to_converted_img}{name}-times-{scale_perc}-smaller.jpg",org_image)
