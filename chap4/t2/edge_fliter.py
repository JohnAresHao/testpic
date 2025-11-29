import cv2

# 4-5　轮廓算法
def edge_fliter(img):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #图像变成灰度图像
    img2 = cv2.medianBlur(img2, 3) #中值滤波, 1357
    img2 = cv2.Laplacian(img2, cv2.CV_8U, 5) #拉普拉斯变换
    cv2.imshow("Lap", img2)
    ret, thresh1 = cv2.threshold(img2, 32, 255, cv2.THRESH_BINARY_INV) #二值化
    cv2.imshow("edge_fliter", thresh1)

def main():
    img = cv2.imread("..\c8.jpg")
    edge_fliter(img)
    cv2.imshow("img", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()

