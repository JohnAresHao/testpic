import cv2
import math

# 4-3 哈哈镜的放大和缩小
def maxFrame(frame):
    height, width, n = frame.shape
    center_x = height / 2
    center_y = width / 2
    radius = 400
    real_radius = int(radius / 2.0)
    new_data = frame.copy()
    #图像遍历
    for i in range(height):
        for j in range(width):
            tx = i - center_x
            ty = j - center_y
            distance = math.sqrt(tx * tx + ty * ty)
            if distance < radius * radius:
                newX = int(tx / 2.0 * distance / real_radius + center_x)
                newY = int(ty / 2.0 * distance / real_radius + center_y)
                if newX < height and newY < width:
                    new_data[i, j][0] = frame[newX, newY][0]
                    new_data[i, j][1] = frame[newX, newY][1]
                    new_data[i, j][2] = frame[newX, newY][2]
            else:
                new_data[i, j][0] = frame[i, j][0]
                new_data[i, j][1] = frame[i, j][1]
                new_data[i, j][2] = frame[i, j][2]

    return new_data

def minFrame(frame):
    height, width, n = frame.shape
    center_x = height / 2
    center_y = width / 2
    radius = 400
    real_radius = int(radius / 2.0)
    new_data = frame.copy()
    #图像遍历
    for i in range(height):
        for j in range(width):
            tx = i - center_x
            ty = j - center_y
            theta = math.atan2(ty, tx) #返回给定的X及Y坐标值的反正切值，结果是在-pi和pi之间。
            distance = math.sqrt(tx * tx + ty * ty)
            newR = math.sqrt(distance) * 12
            newX = int(math.cos(theta) * newR + center_x)
            newY = int(math.sin(theta) * newR + center_y)
            if newX < 0 or newX > height:
                newX = 0
            if newY < 0 or newY > width:
                newY = 0
            if newX < height and newY < width:
                new_data[i, j][0] = frame[newX, newY][0]
                new_data[i, j][1] = frame[newX, newY][1]
                new_data[i, j][2] = frame[newX, newY][2]
            else:
                new_data[i, j][0] = frame[i, j][0]
                new_data[i, j][1] = frame[i, j][1]
                new_data[i, j][2] = frame[i, j][2]

    return new_data


def main():
    img = cv2.imread("..\c8.jpg")
    cv2.imshow("original", img)
    img2 = maxFrame(img) #哈哈镜放大效果
    cv2.imshow("enlarge", img2)
    img3 = minFrame(img) #哈哈镜缩小效果
    cv2.imshow("lessen", img3)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()