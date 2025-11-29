import cv2

# 5-6　视频抖动效果设计
def img_shake(img):
    height, width, n = img.shape
    h1 = int(height * 0.1)
    h2 = int(height * 0.9)
    w1 = int(width * 0.1)
    w2 = int(width * 0.9)
    img2 = img[h1:h2, w1:w2]
    dst = cv2.resize(img2, (width, height))

    #cv2.imshow("dst", dst)
    cv2.waitKey(0)
    return dst

def main():
    vc = cv2.VideoCapture('..\sample.mp4')  # 读入视频文件
    c = 1
    count = 5
    fps = vc.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter("vid_shake.mp4", fourcc, fps, (272, 480))

    while vc.isOpened():  # 循环读取视频帧
        rval, frame = vc.read()
        try:
            if (c % 5 == 0 or 0<count<5):
                dst = img_shake(frame)
                video_writer.write(dst)
                count = count - 1
            else:
                count = 5
                #cv2.imshow("dst", frame)
                video_writer.write(frame)
                cv2.waitKey(0)
            c = c + 1
            cv2.waitKey(1)
        except: #最后一帧为None，添加异常捕获
            print(frame)
            exit(0)
    vc.release()
    print(fps, c)

if __name__ == '__main__':
    main()
