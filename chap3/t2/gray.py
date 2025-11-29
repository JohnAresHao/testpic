import numpy as np
import cv2
# 3-3 创建二维灰度图像
def main():
    img = np.array([
        [0, 255, 0],
        [255, 0, 255]
    ], dtype = np.uint8)
    # 用OpenCV存储
    cv2.imwrite('img_cv2.jpg', img)
    cv2.imshow('img_cv2.jpg', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()