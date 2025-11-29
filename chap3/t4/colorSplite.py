import numpy as np
import cv2
# 3-6 彩色图像的通道分离和混合
def main():
    img = cv2.imread('..\c1.jpg')
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(img2.shape)
    r, g, b = cv2.split(img2) #img分离成三个单通道的图像
    cv2.imshow("red", r)
    cv2.imshow("green", g)
    cv2.imshow("blue", b)
    img3 = cv2.merge([b, g, r])
    cv2.imshow("merge", img3)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()