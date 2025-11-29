import matplotlib.pyplot as plt
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
# 读取图像数据
#img = tf.compat.v1.gfile.FastGFile('..\c15.jpg', 'rb').read()
img = tf.compat.v1.gfile.FastGFile('..\c15.jpg', 'rb').read()

with tf.compat.v1.Session() as sess:
    img_data = tf.compat.v1.image.decode_jpeg(img)
    # 将图像上下翻转
    flipped0 = tf.compat.v1.image.flip_up_down(img_data)
    # 将图像左右翻转
    flipped1 = tf.compat.v1.image.flip_left_right(img_data)
    # 通过交换第一维和第二维来转置图像
    flipped2 = tf.compat.v1.image.transpose_image(img_data)

    plt.subplot(221), plt.imshow(img_data.eval()), plt.title('original')
    plt.subplot(222), plt.imshow(flipped0.eval()), plt.title('flip_up_down')
    plt.subplot(223), plt.imshow(flipped1.eval()), plt.title('flip_left_right')
    plt.subplot(224), plt.imshow(flipped2.eval()), plt.title('transpose_image')

    plt.show()