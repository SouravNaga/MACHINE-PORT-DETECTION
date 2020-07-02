import cv2
import numpy as np
img_rgb=cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template=cv2.imread('pp.png',0)
w,h=template.shape[::-1]
res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
print(res)
thresold=0.8
loc=np.where(res>=thresold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(255,0,0),2)
cv2.imshow('detect',img_rgb)
