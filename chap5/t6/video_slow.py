import cv2

#5-14　视频慢动作效果
def main():
    vc = cv2.VideoCapture('..\sample.mp4')
    c = 1
    fps_slow = 10
    fps = vc.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter("slow.mp4", fourcc, fps, (272,480))
    video1 = cv2.VideoWriter("video1.mp4", fourcc, fps, (272, 480))
    video2 = cv2.VideoWriter("video2.mp4", fourcc, fps_slow, (272, 480))
    video3 = cv2.VideoWriter("video3.mp4", fourcc, fps, (272, 480))

    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False
    print("rval=" + str(rval))

    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if c <= 20:
            video1.write(frame)
        elif c > 20 and c < 51:
            video2.write(frame)
        elif c >= 51:
            video3.write(frame)
        c = c + 1
    vc.release()
    video1.release()
    video2.release()
    video3.release()

    # video merge
    vc1 = cv2.VideoCapture('video1.mp4')
    if vc1.isOpened():
        rval, frame = vc1.read()
    else:
        rval = False
    print("rval1=" + str(rval))
    while rval:
        rval, frame = vc1.read()
        video_writer.write(frame)
    vc1.release()

    vc2 = cv2.VideoCapture('video2.mp4')
    if vc2.isOpened():
        rval, frame = vc2.read()
    else:
        rval = False
    print("rval2=" + str(rval))
    while rval:
        rval, frame = vc2.read()
        video_writer.write(frame)
    vc2.release()

    vc3 = cv2.VideoCapture('video3.mp4')
    if vc3.isOpened():  # 判断vid1是否正常打开
        rval, frame = vc3.read()
    else:
        rval = False
    print("rval3=" + str(rval))
    while rval:  # 循环读取视频帧
        rval, frame = vc3.read()
        video_writer.write(frame)
    vc3.release()

if __name__ == '__main__':
    main()