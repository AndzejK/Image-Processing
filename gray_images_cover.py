import cv2 
from pathlib import Path

path_to_org_img=Path("org_img")
path_to_converted_img=Path("conver_img")

for file_path in path_to_org_img.glob('*'): #the "*"" wildcard matches all file names
    name=file_path.stem[:6]
    org_image=cv2.imread(str(file_path),0)
    cv2.imwrite(f"conver_img/{name}-gray.jpg",org_image)
