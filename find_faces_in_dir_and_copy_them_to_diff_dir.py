# A script that finds faces and copies these files to another dir
import cv2
from pathlib import Path
import time
#loading an image
path_to_org_img=Path("org_img")
path_to_save_edited_img=Path('conver_img/')
#loading xml file for recognising faces
face_cascade=cv2.CascadeClassifier('faces.xml')


for file_path in path_to_org_img.glob('*'): #the "*"" wildcard matches all file names
    print(file_path)
    img=cv2.imread(f'{file_path}')
    name=file_path.stem[:6]
    faces=face_cascade.detectMultiScale(img,1.1,4) # command set-up
    cv2.imwrite(f"{path_to_save_edited_img}detected_faces/{name}-detected.jpg",img)
    print( cv2.imwrite(f"{path_to_save_edited_img}detected_faces/{name}-detected.jpg",img))
    