import cv2
# 5-5　图像抖动效果测试
def img_shake(img):
    height, width, n = img.shape
    h1 = int(height * 0.1)
    h2 = int(height * 0.9)
    w1 = int(width * 0.1)
    w2 = int(width * 0.9)
    # 将图像按比例裁剪20%之后再放大至原图大小
    img2 = img[h1:h2, w1:w2]
    dst = cv2.resize(img2, (width, height))
    cv2.imshow("src", img)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)

def main():
    vid = cv2.VideoCapture("..\sample.mp4")
    c = 1
    while vid.isOpened():
        rval, frame = vid.read()
        if c == 2:
            img_shake(frame)
        c = c + 1
        cv2.waitKey(1)
    vid.release()

if __name__ == '__main__':
    main()
