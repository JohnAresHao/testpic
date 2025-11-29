import cv2

#5-15　视频人物漫画效果
def cartoon_style(img_rgb):
    img_color = img_rgb
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY) #转换为灰度图
    img_blur = cv2.medianBlur(img_gray, 7) #中值滤波
    # 检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2) #二值化
    # 转换回彩色图像
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    img_cartoon = cv2.bitwise_and(img_color, img_edge) #叠加
    return img_cartoon

def main():
    vc = cv2.VideoCapture('..\sample.mp4')
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
    print("rval=" + str(rval))

    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        try:
            frame = cartoon_style(frame)
            cv2.imshow("cartoon", frame)
            cv2.waitKey(1)
        except: #最后一帧为None，添加异常捕获
            print(frame)
            exit(0)
    vc.release()

if __name__ == '__main__':
    main()