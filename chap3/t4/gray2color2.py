import numpy as np
import cv2
# 3-10 伪彩色图像
def main():
    img = cv2.imread('..\gray1.jpg')
    img_color = cv2.applyColorMap(img, cv2.COLORMAP_JET) #色度图上色
    cv2.imshow("img_color.jpg", img_color)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()