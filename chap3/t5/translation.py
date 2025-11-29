import numpy as np
import cv2
# 3-12　图像平移
def main():
    img = cv2.imread("..\c2.jpg")
    height, width, temp = img.shape
    M = np.array([[1, 0, 50], [0, 1, 50]], np.float32)
    img_trans = cv2.warpAffine(img, M, img.shape[:2]) #图像平移
    cv2.imshow('imgage', img) #显示原图
    cv2.imshow('img_trans', img_trans)
    cv2.imwrite('img_trans.jpg', img_trans)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()