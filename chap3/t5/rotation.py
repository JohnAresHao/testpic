import numpy as np
import cv2
# 3-13　图像旋转
def main():
    img = cv2.imread("..\c2.jpg")
    height, width, temp = img.shape
    M =cv2.getRotationMatrix2D((width/2, height/2), 45, 1) #中心逆时针旋转45°
    img_ro = cv2.warpAffine(img, M, img.shape[:2])
    cv2.imshow('imgage', img) #显示原图
    cv2.imshow('img_ro', img_ro)
    cv2.imwrite('img_ro.jpg', img_ro)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()