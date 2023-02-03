import importlib
import importlib.util
a=importlib.util.find_spec(name=None, package='b')
#绝对导入
print(a)
params = importlib.import_module('b.c.c') 
 
#相对导入，注意路径前面有一个“.”，（这时__name__就可以派上用场）
params_ = importlib.import_module('.c.c',package='b') 

# 对象中取出需要的对象
params.args #取出变量
params.C  #取出class C
params.C.c  #取出class C 中的c 方法
a=importlib.util.find_spec(name=None, package='b')
a=importlib.util.find_spec(name=None, package='b')