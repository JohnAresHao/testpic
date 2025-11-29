import numpy as numpy
import cv2
from matplotlib import pyplot as plt

# 3-15 灰度图像直方图
def main():
    img = cv2.imread('..\c3.jpg', 0)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure() #新建一个图像
    plt.title("GrayScale Histogram") #图像的标题
    plt.xlabel("Bins") #X轴标签
    plt.ylabel("# of Pixels") #Y轴标签
    plt.plot(hist) #画图
    plt.xlim([0, 256]) #设置X轴坐标的范围
    plt.show() #显示图像
    #input()

if __name__ == '__main__':
    main()