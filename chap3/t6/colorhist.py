import numpy as numpy
import cv2
from matplotlib import pyplot as plt

# 3-16 彩色图像直方图
def main():
    img = cv2.imread('..\c3.jpg')
    chans = cv2.split(img)
    colors = ('b', 'g', 'r')

    plt.figure() #新建一个图像
    plt.title("Flattened Color Histogram") #图像的标题
    plt.xlabel("Bins") #X轴标签
    plt.ylabel("# of Pixels") #Y轴标签
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color) #画图
        plt.xlim([0, 256]) #设置X轴坐标的范围
    plt.show() #显示图像

if __name__ == '__main__':
    main()