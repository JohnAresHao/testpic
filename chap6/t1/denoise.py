import cv2
import numpy as np
# 6-2　图像降噪的简单实现：
def main():
    img = cv2.imread("..\c9.jpg")
    img3 = cv2.medianBlur(img, 7)
    cv2.imshow("img3", img3)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()