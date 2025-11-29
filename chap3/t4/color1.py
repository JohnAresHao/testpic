import numpy as np
import cv2
# 3-8 彩色图像的遍历
def main():
    img =  cv2.imread("..\c1.jpg")
    height, width, n = img.shape #得到图片的宽高和维度
    img2 = img.copy() #复制一个跟img相同的新图片
    # 宽高两个维度遍历图片
    for i in range(height):
        for j in range(width):
            img2[i, j][0] = 0 #将第一个通道内的元素重新赋值
    cv2.imshow('img2.jpg', img2)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()