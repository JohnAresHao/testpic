import cv2

# 5-10　图像霓虹效果测试
def main():
    img = cv2.imread('..\c51.jpg')
    height ,width, n = img.shape
    h1 = int(height * 0.9)
    w1 = int(width * 0.1)
    cv2.circle(img, (w1, h1), 20, (114,128,250), -1)
    cv2.circle(img, (w1+40, h1-40), 20, (106,106,255), -1)
    cv2.circle(img, (w1+80, h1), 20, (114,128,250), -1)
    cv2.circle(img, (w1, h1-60), 20, (114,128,240), -1)
    cv2.imshow("demo", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()