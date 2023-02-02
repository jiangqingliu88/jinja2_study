1、内置模块
2、当前目录
3、程序的主目录
4、python path 目录 设置了 path环境
5、表春链接库目录
6、第三方库目录
7、.path文件的内容
8、sys.path.append()临时添加的目录
其实这两个错误的原因归根结底是一样的：在涉及到相对导入时，package所对应的文件夹必须正确的被python解释器视作package，而不是普通文件夹。否则由于不被视作package，无法利用package之间的嵌套关系实现python中包的相对导入。
　　1、文件夹中必须有__init__.py文件，该文件可以为空，但必须存在该文件。

　　2、不能作为顶层模块来执行该文件夹中的py文件（即不能作为主函数的入口）。
这是因为我们是在TestIm文件夹下把main.py文件作为主函数的入口执行的，因此尽管TestIm文件夹中有__init__.py文件，但是该文件夹不能被python解释器视作package，即Tom package不存在上层packge，自然会报错，相对导入时超出了最高层级的package。



csdn
python 自己写package 导入 attempted relative import beyond top-level package