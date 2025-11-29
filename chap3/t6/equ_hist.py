import numpy as np
import numpy as numpy
import cv2
from matplotlib import pyplot as plt

# 3-17 灰度图像直方图均衡化
def main():
    img = cv2.imread("..\g1.png", 0)
    eq = cv2.equalizeHist(img) #图像均衡化
    cv2.imshow("Histogram Equalization", np.hstack([img, eq]))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()