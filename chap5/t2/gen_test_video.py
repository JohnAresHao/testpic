import cv2
# 5-4 测试视频抖动效果
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('save0.avi', fourcc, fps, (429,415))
c = 0
frame = cv2.imread("..\chessboard.jpg")
while c < 200: #200帧图像，6s多
    videoWriter.write(frame)
    c = c + 1
videoWriter.release()