from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

# 6-1　机器学习的鸢尾花分类问题
iris = load_iris()
#读取数据和标签, x是输入特征矩阵，y是输出响应向量
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.4, random_state=1)
#训练模型
gnb = GaussianNB()
gnb.fit(x_train, y_train)
#做出预测
y_pred = gnb.predict(x_test)
#对比实际输出与预测
print("Gaussian Native Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
