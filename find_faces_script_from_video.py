import cv2
import os

cascade='faces.xml'
input_dir='org_img'
output_dir='conver_img/detected_faces'
colour_of_rect=(255,255,255)
width_of_rect=4
scale=1.1
near_neighb=4

#find faces
def has_face(img_path):
    img=cv2.imread(img_path,1)
    #loading xml file for recognising faces
    face_cascade=cv2.CascadeClassifier(cascade)
    #find diff sizes of the face
    faces=face_cascade.detectMultiScale(img,scale,near_neighb) # command set-up
    # we get the list with a bunch of list "faces"/number/cordinates
    print(faces) 
    #place this cordinates on the img
    if len(faces)!=0:   
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),colour_of_rect,width_of_rect)
    return img
    
images=os.listdir(input_dir)
for img_path in images:
    face_img=has_face(f'{input_dir}/{img_path}')
    if face_img is not None:
        cv2.imwrite(f'{output_dir}/{img_path}',face_img)

