import math
import cv2

# 8-7 图像美白试验示例, 通过beta参数
def main():
    img = cv2.imread('..\c3.jpg')
    height, width, n = img.shape
    img2 = img.copy()
    beta = 3
    alpha = 40

    for i in range(height):
        for j in range(width):
            img2[i, j][0] = alpha * math.log(img[i, j][0] * (beta - 1) + 1) / math.log(beta)
            img2[i, j][1] = alpha * math.log(img[i, j][1] * (beta - 1) + 1) / math.log(beta)
            img2[i, j][2] = alpha * math.log(img[i, j][2] * (beta - 1) + 1) / math.log(beta)
    dst = cv2.addWeighted(img, 0.6, img2, 0.4, 0)  # 图像叠加
    cv2.imshow("res", dst)
    cv2.imwrite('res_white31.jpg', dst)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
