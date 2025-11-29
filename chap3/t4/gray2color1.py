import numpy as np
import cv2
# 3-9 增加图像通道
def main():
    img = cv2.imread('..\gray1.jpg')
    gray = np.zeros((480, 480, 3), np.uint8) # 生成一个空彩色图像
    print(img.shape)
    height, width, n = img.shape
    # 图像像素级遍历
    for i in range(height):
        for j in range(width):
            gray[i, j][0] = img[i, j][0]
            gray[i, j][1] = 0
            gray[i, j][2] = 0
    cv2.imshow('gray.jpg', gray)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()