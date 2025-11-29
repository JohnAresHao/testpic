import numpy as np
import cv2
# 3-14　图像镜像变换
def main():
    img = cv2.imread("..\c2.jpg")
    height, width, temp = img.shape
    xImg = cv2.flip(img, 1, dst=None) #水平翻转
    yImg = cv2.flip(img, 0, dst=None) #垂直翻转
    cv2.imshow('imgage', img) #显示原图
    cv2.imshow('xImg', xImg)
    cv2.imshow('yImg', yImg)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()