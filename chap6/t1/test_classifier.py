import numpy as np
import cv2
#6-4　机器学习训练代码
face_cascade = cv2.CascadeClassifier('../cascade.xml')
img = cv2.imread('../c14.jpg') #单人脸可识别
#img = cv2.imread('../c13.jpg') #多人脸识别不全
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()