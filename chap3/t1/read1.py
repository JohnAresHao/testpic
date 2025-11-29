import cv2
# 3-1 读取一张图片并显示和存储
def main():
    # 输出已安装OpenCV的版本
    print(cv2.__version__) #V4.6.0
    # 读取一张灰度图像, cv2.imread() 函数默认以BGR顺序加载彩色图像
    img = cv2.imread('..\gray1.jpg')
    # 指定标题窗口展示图像
    cv2.imshow('gray', img)
    # 输出图像到文件
    cv2.imwrite('.\save.png', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
