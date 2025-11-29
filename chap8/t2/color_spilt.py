import cv2
import numpy as np
# 8-5　颜色分割
def main():
    img = cv2.imread('..\c4.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 红色的H范围是160～179，S和V的范围为50～255
    lower_red = np.array([160, 50, 50])
    upper_red = np.array([179, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('res', res)
    cv2.imwrite('res.jpg', res)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
