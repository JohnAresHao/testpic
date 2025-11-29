import cv2
import os

# 5-3 多个视频合并
def video_merge():
    VideoWriter = cv2.VideoWriter("test_vid_mix.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 30, (408,720))
    vid_list = ['testp1.avi','testp2.avi']
    print("vid_file=" + str(vid_list))
    for vid_file in vid_list:
        capture = cv2.VideoCapture(vid_file)
        fps = capture.get(cv2.CAP_PROP_FPS)
        #print("fps=" + str(fps))
        if capture.isOpened():
            i = 0
            while i < fps * 17.5:#17.5???
                i += 1
                ret, prev = capture.read()
                if ret is True:
                    VideoWriter.write(prev)
                else:
                    break
    VideoWriter.release()
    cv2.destroyAllWindows()

def main():
    video_merge()

if __name__ == '__main__':
    main()