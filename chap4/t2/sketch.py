import cv2
import numpy as np

# 4-6 素描风格
def sketch_style(img):
    height, width, n = img.shape
    gray0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #转换为灰度图
    #cv2.imshow("gray0", gray0)
    #构建一个空的图像
    img2 = np.zeros((height, width), dtype='uint8')
    gray1 = cv2.addWeighted(gray0, -1, img2, 0, 255, 0) #图像叠加,得到反色图片
    cv2.imshow("img0", gray1)
    gray1 = cv2.GaussianBlur(gray1, (19, 19), 0) #高斯滤波
    dst = cv2.addWeighted(gray0, 1.2, gray1, 0.3, 0) #滤波后图像叠加
    cv2.imshow("sketch_img", dst)

def main():
    img = cv2.imread("..\c8.jpg")
    sketch_style(img)
    cv2.imshow("img", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
