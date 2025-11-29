import cv2
# 8-1　均值过滤器示例
def main():
    img = cv2.imread("..\c1.jpg")
    blur = cv2.blur(img, (7,7)) #一般核越大，图片处理完的效果越模糊
    cv2.imshow("img", img)
    cv2.imshow("blur", blur)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()