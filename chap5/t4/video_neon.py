import cv2

# 5-11　视频霓虹效果设计
def neon(img, cnt):
    height, width, n = img.shape
    mask = img
    if cnt == 1:
        mask = cv2.imread("..\mask1.jpg")
    elif cnt == 2:
        mask = cv2.imread("..\mask2.jpg")
    elif cnt == 3:
        mask = cv2.imread("..\mask3.jpg")
    elif cnt == 4:
        mask = cv2.imread("..\mask4.jpg")

    mask = cv2.resize(mask, (width, height), interpolation=cv2.INTER_CUBIC)
    dst = cv2.addWeighted(img, 0.7, mask, 0.3, 0)  # 图像叠加
    return dst

def main():
    vid = cv2.VideoCapture('..\sample.mp4')
    c = 1
    fps = vid.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter("vid_neon.mp4", fourcc, fps, (272, 480))
    while vid.isOpened():  # 循环读取视频帧
        rval, frame = vid.read()
        try:
            cnt = c % 5
            dst = neon(frame, cnt)
            video_writer.write(dst)
            c = c + 1
            cv2.waitKey(1)
        except: #最后一帧为None，添加异常捕获
            print(frame)
            exit(0)
    vid.release()
    print(fps, c)

if __name__ == '__main__':
    main()