import cv2

#5-13　视频反复效果设计
def main():
    vc = cv2.VideoCapture('..\sample.mp4')  # 读入视频文件
    c = 1
    fps = vc.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter("repeat.mp4", fourcc, fps, (272, 480))
    vid1 = cv2.VideoWriter("vid1.mp4", fourcc, fps, (272, 480)) #正序
    vid2 = cv2.VideoWriter("vid2.mp4", fourcc, fps, (272, 480)) #倒序

    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
    print("rval=" + str(rval))

    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if c>=21 and c<=50:# ，21~50，取中间30帧
            vid1.write(frame)
            cv2.imwrite('imgs/' + str(50-c) + '.jpg', frame)  # 存储为图像
            #print("t1="+str(c))
            #cv2.imshow('t1', frame)
        c = c + 1
        #cv2.waitKey(1)
    vc.release()
    vid1.release() #必须要释放，否则无法接着再次打开

    for i in range(0, 30):
        img = cv2.imread('imgs/%d.jpg' % i)
        #cv2.imshow("t2", img)
        vid2.write(img)
    vid2.release() #必须要释放，否则无法接着再次打开

    # video merge repeat like: video1->video2->video1
    vc1 = cv2.VideoCapture('vid1.mp4')
    if vc1.isOpened():  # 判断vid1是否正常打开
        rval, frame = vc1.read()
    else:
        rval = False
    print("rval1=" + str(rval))
    while rval:  # 循环读取视频帧
        rval, frame = vc1.read()
        video_writer.write(frame)
    vc1.release()

    vc2 = cv2.VideoCapture('vid2.mp4') #用时声明
    if vc2.isOpened():  # 判断vid2是否正常打开
        rval, frame = vc2.read()
    else:
        rval = False
    print("rval2=" + str(rval))
    while rval:  # 循环读取视频帧
        rval, frame = vc2.read()
        video_writer.write(frame)
    vc2.release()

    vc1 = cv2.VideoCapture('vid1.mp4')
    if vc1.isOpened():  # 判断vid1是否正常打开
        rval, frame = vc1.read()
    else:
        rval = False
    print("rval1=" + str(rval))
    while rval:  # 循环读取视频帧
        rval, frame = vc1.read()
        video_writer.write(frame)
    vc1.release()


if __name__ == '__main__':
    main()
