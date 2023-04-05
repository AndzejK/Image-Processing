import cv2
img=cv2.imread('galaxy.jpg')
img_w=cv2.imread('watermark/template.png')

### The Calculation, where to place the watermark ###

# Get the size of images
print(img.shape) #(471, 501, 3) - Height, Width, dim
print(img_w.shape) #50, 320, 3) - Height, Width, dim
# Coordinates from where we should start placing the watermark
x = img.shape[1]- img_w.shape[1] #421
y = img.shape[0]- img_w.shape[0] #181
#extracting/cropping from img - galaxy.jpg this part where watermark will go
watermark_place=img[y:,x:]
cv2.imwrite('watermark_place.jpeg',watermark_place) 
# On the copped img watermark was placed
blend=cv2.addWeighted(watermark_place,0.3,img_w,0.4,0)
cv2.imwrite('blend.jpeg',blend)
# replacing the original area of img, galaxy.jpg with a new pic - blend.jpeg
img[y:,x:]=blend
cv2.imwrite('galaxy-watermarked.jpg',img)

