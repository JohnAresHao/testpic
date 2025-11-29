import numpy as np
import cv2

# 8-9　手动祛痘算法设计示例
# 定义全局变量
global inpaintMask, img
global point1, point2
def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    img2 = img.copy()
    height1, width1, n = img.shape
    inpaintMask = np.zeros((height1, width1), dtype='uint8')
    if event == cv2.EVENT_LBUTTONDOWN: # 左键单击
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), -1)
        cv2.circle(inpaintMask, point1, 10, 255, -1)
        cv2.imshow('img2', img2)
    elif event == cv2.EVENT_LBUTTONUP: # 左键释放
        cv2.circle(img2, point1, 10, (0, 255, 0), -1)
        cv2.circle(inpaintMask, point1, 10, 255, -1)
        cv2.imshow("inpaintMask", inpaintMask)
        cv2.imshow('img2', img2)
        dst = cv2.inpaint(img, inpaintMask, 3, cv2.INPAINT_TELEA)
        cv2.imshow("inpaint image", dst)
        cv2.imwrite("inpaint.jpg", dst)

def main():
    global img
    img = cv2.imread('..\c5.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()