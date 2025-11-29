import numpy as np
import numpy as numpy
import cv2
from matplotlib import pyplot as plt

# 3-19 灰图像反向投影
def main():
    sample = cv2.imread("..\c50.jpg")
    target = cv2.imread("..\c51.jpg")
    roi_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV) #图像转HSV空间
    target_hsv =  cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
    cv2.imshow("sample", sample)
    cv2.imshow("target", target)

    roiHist = cv2.calcHist([roi_hsv], [0, 1], None, [32, 30], [0, 180, 0, 256]) #计算直方图
    cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX) #直方图归一化
    dst = cv2.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1) #直方图反向投影计算
    cv2.imshow("back_project_demo",dst)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()