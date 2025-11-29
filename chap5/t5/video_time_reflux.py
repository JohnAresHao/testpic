import cv2

#5-12　视频时光倒流效果
def main():
    vc = cv2.VideoCapture('..\sample.mp4')  # 读入视频文件
    c = 1
    fps = vc.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter("time_reflux.mp4", fourcc, fps, (272, 480))

    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
    print("rval=" + str(rval))

    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if c>=21 and c<=50:# ，21~50，取中间30帧
            cv2.imwrite('imgs/' + str(50-c) + '.jpg', frame)  # 存储为图像
            print("t1="+str(c))
            cv2.imshow('t1', frame)
        c = c + 1
        cv2.waitKey(1)
    vc.release()

    for i in range(0, 30):
        img = cv2.imread('imgs/%d.jpg' % i)
        #cv2.imshow("t2", img)
        video_writer.write(img)
    video_writer.release()

if __name__ == '__main__':
    main()
