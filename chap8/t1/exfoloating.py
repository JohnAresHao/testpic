from PIL import Image
from PIL import ImageEnhance
import cv2
# 8-4　图像磨皮算法设计示例
def main():
    img = cv2.imread('..\c3.jpg')
    # 图像滤波，双边过滤器
    blur = cv2.bilateralFilter(img, 9, 75, 75)
    alpha = 0.3
    beta = 1-alpha
    gamma = 0
    sharpness = 1.5
    contrast = 1.15
    # 图像融合
    img_add = cv2.addWeighted(img, alpha, blur,beta, gamma)
    cv2.imwrite('img_add.jpg', img_add)
    # 锐度增强
    img_add = Image.open('img_add.jpg')
    enh_sha = ImageEnhance.Sharpness(img_add)
    img_sharped = enh_sha.enhance(sharpness)
    # 对比度增强
    enh_con = ImageEnhance.Contrast(img_sharped)
    img_contrasted = enh_con.enhance(contrast)
    img_contrasted.show()
    img_contrasted.save("c3new.jpg")

    cv2.waitKey(0)

if __name__ == '__main__':
    main()