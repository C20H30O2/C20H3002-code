# 使用cmd安装pyspark后仍然无法导包，之后多次尝试在pycharm中用镜像网站下载才成功
from pyspark import SparkConf,SparkContext# 导包
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")# 创建sparkconf类对象,这里运用了链式调用的写法（链式调用的基本原则是不管调用什么方法，返回值都是同一个对象）
sc=SparkContext(conf=conf)# 基于sparkconf类对象创建sparkcontext对象
print(sc.version)# 打印spark的运行版本
rdd1=sc.parallelize([1,2,3,4,5])
rdd2=sc.parallelize((1,2,3,4,5))
rdd3=sc.parallelize("abcdefg")
rdd4=sc.parallelize({1,2,3,4,5})
rdd5=sc.parallelize({"key1":"value1","key2":"value2"})
print(rdd1.collect())# 查看rdd里的内容需要用collect（）方法
print(rdd2.collect())# 查看rdd里的内容需要用collect（）方法
print(rdd3.collect())# 查看rdd里的内容需要用collect（）方法
print(rdd4.collect())# 查看rdd里的内容需要用collect（）方法
print(rdd5.collect())# 查看rdd里的内容需要用collect（）方法



sc.stop()# 停止sparkcontext对象的运行（停止spark程序）
