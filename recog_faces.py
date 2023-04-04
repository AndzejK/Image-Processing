import cv2
#loading an image
img=cv2.imread('human_faces-2.jpg')
#loading xml file for recognising faces
face_cascade=cv2.CascadeClassifier('faces.xml')
#find diff sizes of the face
faces=face_cascade.detectMultiScale(img,1.1,4) # command set-up
# we get the list with a bunch of list "faces"/number/cordinates
print(faces) 

#place this cordinates on the img
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),4)
cv2.imwrite('Detected_human_faces-2.jpeg',img)
