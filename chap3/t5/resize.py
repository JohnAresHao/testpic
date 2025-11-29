import numpy as np
import cv2
# 3-11　图像缩放
def main():
    img = cv2.imread("..\c2.jpg")
    height, width, temp = img.shape
    downscale = cv2.resize(img, (100, 100), interpolation=cv2.INTER_LINEAR) #缩小
    upscale = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_LINEAR) #放大
    cv2.imshow("image", img) #显示原图
    cv2.imshow("downscale", downscale)
    cv2.imshow("upscale", upscale)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()