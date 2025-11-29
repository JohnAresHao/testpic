import numpy as np
import cv2
# 3-5 彩色图像转灰度图像
def main():
    img =  cv2.imread('..\c1.jpg')
    img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #从彩色图像转化成灰度图像
    cv2.imshow('img2.bmp', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()