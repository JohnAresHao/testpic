import numpy as np
import numpy as numpy
import cv2
from matplotlib import pyplot as plt

# 3-18 灰度图像直方图局部均衡化
def main():
    img = cv2.imread("..\g1.png", 0)
    clahe = cv2.createCLAHE(5, (8, 8)) #对比度的大小为5，每次处理块大小为8×8
    dst = clahe.apply(img)
    cv2.imshow("Local Histogram Equalization", np.hstack([img, dst]))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()