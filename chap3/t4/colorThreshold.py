import numpy as np
import cv2
# 3-7 彩色图像二值化
def main():
    img =  cv2.imread('..\c1.jpg', 0) #imread读取图像的时候直接设置参数为0，彩色图像自动被读成灰度图像
    # 图像二值化, 高于127的像素全部置为255，低于的全部置为0
    thresh, dst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()