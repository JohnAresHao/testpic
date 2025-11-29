from PIL import Image
from PIL import ImageEnhance
import cv2


# 8-6 图像美白算法设计示例
def main():
    img = cv2.imread('..\c3.jpg')
    height, width, n = img.shape
    img2 = img.copy()  # 全白图层
    for i in range(height):
        for j in range(width):
            img2[i, j][0] = 255
            img2[i, j][1] = 255
            img2[i, j][2] = 255
    dst = cv2.addWeighted(img, 0.6, img2, 0.4, 0)  # 图像叠加
    cv2.imwrite('res_white21.jpg', dst)
    img3 = Image.open('res_white21.jpg')
    # 对比度增强
    enh_con = ImageEnhance.Contrast(img3)
    contrast = 1.2
    img_contrasted = enh_con.enhance(contrast)
    # 亮度增强
    enh_bri = ImageEnhance.Brightness(img_contrasted)
    brightness = 1.1
    img_brightened = enh_bri.enhance(brightness)
    img_brightened.show()
    img_brightened.save("res_white22.jpg")

if __name__ == '__main__':
    main()
