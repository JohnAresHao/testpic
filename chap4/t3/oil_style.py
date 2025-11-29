import cv2
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import random
#4-7　油画风格
def oil_style(img):
    height, width, n = img.shape
    output = np.zeros((height-2, width, n), dtype='uint8')
    for i in range(1, height-2):
        for j in range(width-2):
            # 相邻行像素随机打乱, 相邻3行，使得笔触粗糙
            if random.randint(1, 10) % 3 == 0:
                output[i, j] = img[i+1, j]
            elif random.randint(1, 10) % 2 == 0:
                output[i, j] = img[i+2, j]
            else:
                output[i, j] = img[i-1, j]
    #cv2.imshow("oil_img", output)
    cv2.imwrite("oil_img.jpg", output)

def add_color():
    image = Image.open(".\oil_img.jpg")
    enhance_color = ImageEnhance.Color(image)
    color = 2.0
    image_colored = enhance_color.enhance(color)
    image_colored.show()

def main():
    img = cv2.imread("..\c4.jpg")
    oil_style(img)
    add_color()
    #cv2.imshow("img", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()

