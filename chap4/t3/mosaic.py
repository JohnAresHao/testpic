import skimage
import matplotlib.pyplot as plt
import numpy as np
import random
#4-8　图片马赛克
def main():
    img = skimage.io.imread("..\c4.jpg")
    img = skimage.img_as_float(img)
    img_out = img.copy()
    row, col, channel = img.shape
    half_patch = 10 #马赛克大小
    # 对马赛克滑块移动时图像内部像素进行处理
    for i in range(half_patch, row-1-half_patch, half_patch):
        for j in range(half_patch, col-1- half_patch, half_patch):
            k1 = random.random() - 0.5 # [0,1) float
            k2 = random.random() - 0.5
            m = np.floor(k1*(half_patch*2+1))
            n = np.floor(k2*(half_patch*2+1))
            h = int((i+m) % row)
            w= int((j+n) % col)
            img_out[i-half_patch:i+half_patch,j-half_patch:j+half_patch, :] = \
            img[h,w,:]

    plt.figure(1)
    plt.imshow(img)
    plt.axis("on")
    plt.figure(2)
    plt.imshow(img_out)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    main()