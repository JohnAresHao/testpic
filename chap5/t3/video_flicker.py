import cv2
import numpy as np

# 5-8　视频闪白效果设计
def gamma_trans(img, gamma):
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。

def main():
    vid = cv2.VideoCapture('..\sample.mp4')  # 读入视频文件
    c = 1
    count = 5
    fps = vid.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_writer = cv2.VideoWriter("vid_flicker.mp4", fourcc, fps, (272, 480))

    while vid.isOpened():  # 循环读取视频帧
        rval, frame = vid.read()
        try:
            if (c % 5 == 0 or 0 < count < 5):
                #Gamma参数暂定成了0.3
                dst = gamma_trans(frame, 0.3)
                video_writer.write(dst)
                count = count - 1
            else:
                count = 5
                # cv2.imshow("dst", frame)
                video_writer.write(frame)
                cv2.waitKey(0)
            c = c + 1
            cv2.waitKey(1)
        except:  # 最后一帧为None，添加异常捕获
            print(frame)
            exit(0)
    vid.release()
    print(fps, c)

if __name__ == '__main__':
    main()
