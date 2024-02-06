from sklearn.datasets import load_iris
iris = load_iris()
print(dir(iris))
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0:2])
print(iris.target[0:2])
