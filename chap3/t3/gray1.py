import numpy as np
import cv2
# 3-4 灰度图像的遍历
def main():
    img = cv2.imread('..\gray1.jpg')
    height, width, n = img.shape #得到图片的宽、高和维度
    img2 = img.copy()
    # 从宽、高两个维度遍历图片
    for i in range(height):
        for j in range(width):
            img2[i, j] = 0 #将数组里面的元素重新赋值为0，全黑
    cv2.imshow('img2.jpg', img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()