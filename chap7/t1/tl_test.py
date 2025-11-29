import tensorflow as tf
#TensorFlow 2.x中用于禁用动态执行模式（Eager Execution）的函数，强制代码以静态计算图模式运行，类似于TensorFlow 1.x的行为。
tf.compat.v1.disable_eager_execution()
# 7-1　TensorFlow安装测试代码, tf2版本过高，测试案例则使用tf1
hello = tf.constant('Hello, TensorFlow!')
sess = tf.compat.v1.Session()
print(sess.run(hello))
a=tf.constant(10)
b=tf.constant(32)
print(sess.run(a+b))
