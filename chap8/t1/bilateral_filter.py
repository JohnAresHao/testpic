import cv2
# 8-3　双边过滤器示例
def main():
    img = cv2.imread('..\c1.jpg')
    bblur = cv2.bilateralFilter(img, 9, 75, 75)#d是领域的直径，后面两个参数是空间高斯函数标准差和灰度值相似性高斯函数标准差
    cv2.imshow('img', img)
    cv2.imshow('bblur', bblur)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()