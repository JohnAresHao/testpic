import cv2
# 4-9　漫画风格
#1.将彩色图像转换成灰度图像
#2.边缘检测提取灰度图像的边缘
#3.对于检测的边缘进行增强并二值化产生粗线条的特征图像
#4.将处理完的图像与原图进行叠加，得到最终效果
def main():
    img_rgb = cv2.imread("..\c4.jpg")
    img_color = img_rgb
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7) #中值滤波，主要是降低图片的准确度
    img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2) #自适应阈值二值化
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    img_cartoon = cv2.bitwise_and(img_color, img_edge)
    cv2.imshow("img_cartoon", img_cartoon)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()