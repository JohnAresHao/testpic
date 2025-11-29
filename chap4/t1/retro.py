import cv2

# 4-4 怀旧风格
def retro_style(img):
    img_cp = img.copy()
    height, width, n = img.shape
    for i in range(height):
        for j in range(width):
            b = img[i, j][0]
            g = img[i, j][1]
            r = img[i, j][2]
            # 计算新的图像中的BGR值
            new_b = int(0.272 * r + 0.534 * g + 0.131 * b)
            new_g = int(0.349 * r + 0.686 * g + 0.168 * b)
            new_r = int(0.393 * r + 0.769 * g + 0.189 * b)
            #约束图像像素值，防止溢出
            #img_cp[i, j][0] = min(max(0, new_b), 255)
            img_cp[i, j][0] = max(0, min(new_b, 255))
            img_cp[i, j][1] = max(0, min(new_g, 255))
            img_cp[i, j][2] = max(0, min(new_r, 255))

    cv2.imshow("retro_img", img_cp)

def main():
    img = cv2.imread("..\c8.jpg")
    retro_style(img)  # 怀旧效果
    cv2.imshow("img", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()