import glob
import os

import cv2

# 5-2　视频截取和保存为图片，再将图片合称为视频
def video2imgs(video_name):
    vid = cv2.VideoCapture(video_name)  # 读入视频文件
    c = 0

    if vid.isOpened():  # 判断是否正常打开
        rval, frame = vid.read()
    else:
        rval = False
    print("rval=" + str(rval))

    timeF = 30  # 视频帧计数间隔，每隔30帧取一张图
    while rval:  # 循环读取视频帧
        rval, frame = vid.read()
        if (c % timeF == 0):  # 每隔timeF帧进行存储操作
            cv2.imwrite('imgs/' + str(c) + '.jpg', frame)  # 存储为图像
            cv2.imshow('test', frame)
        c = c + 1
        cv2.waitKey(1)
    vid.release()


def imgs2video(imgs_dir, save_name):
    fps = 30
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter(save_name, fourcc, fps, (408, 720))
    imgs = glob.glob(os.path.join(imgs_dir, '*.jpg'))
    for i in range(len(imgs)):
        #img_name = os.path.join(imgs_dir, '{d}:03.jpg'.format(i))
        frame = cv2.imread(imgs[i])
        video_writer.write(frame)
    video_writer.release()

def main():
    video2imgs("testp1.avi")
    imgs2video(".\imgs\\", "test_img_mix.avi")

if __name__ == '__main__':
    main()