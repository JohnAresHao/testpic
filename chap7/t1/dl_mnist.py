#import keras
import tensorflow as tf
from tensorflow import keras
#读取keras官方mnist
def preprocess(labels, images):
    '''
    最简单的预处理函数:
        转numpy为Tensor、分类问题需要处理label为one_hot编码、处理训练数据
    '''
    # 把numpy数据转为Tensor
    labels = tf.cast(labels, dtype=tf.int32)
    # labels 转为one_hot编码
    labels = tf.one_hot(labels, depth=10)
    # 顺手归一化
    images = tf.cast(images, dtype=tf.float32) / 255
    return labels, images


abs_path_to_dataset = 'D:/Documents/PyFiles/testpic/chap7/mnist.npz'
(x, y), (x_test, y_test) = keras.datasets.mnist.load_data(path=abs_path_to_dataset)  # 绝对路径
print(type(x), x.shape)  # <class 'numpy.ndarray'> (60000, 28, 28)
print(type(y), y.shape)  # <class 'numpy.ndarray'> (60000,)
db_train = tf.data.Dataset.from_tensor_slices((x, y))
print(db_train)  # <DatasetV1Adapter shapes: ((28, 28), ()), types: (tf.uint8, tf.uint8)>
print(type(db_train))  # <class 'tensorflow.python.data.ops.dataset_ops.DatasetV1Adapter'>
db_train.shuffle(1000)
db_train.map(preprocess)
db_train.batch(64)
db_train.repeat(2)
print(type(db_train))  # <class 'tensorflow.python.data.ops.dataset_ops.DatasetV1Adapter'>
