import cv2
# 8-2　高斯过滤器示例
def main():
    img = cv2.imread('..\c1.jpg')
    gblur = cv2.GaussianBlur(img, (7,7), 0)
    cv2.imshow('img', img)
    cv2.imshow('gblur', gblur)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()