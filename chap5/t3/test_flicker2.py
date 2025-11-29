import cv2
import numpy as np
# 5-9　图像闪白效果测试2
def main():
    img = cv2.imread('..\c51.jpg')
    height, width, n = img.shape
    mask = cv2.imread('..\mask.jpg')
    mask = cv2.resize(mask, (width, height), interpolation=cv2.INTER_CUBIC)
    dst = cv2.addWeighted(img, 0.6, mask, 0.4, 0) #图像叠加,主图叠加系数为0.6
    cv2.imshow("demo", dst)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
