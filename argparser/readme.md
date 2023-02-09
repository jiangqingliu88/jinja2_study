# postional arhgnment
代码中integer为positional arguments，num为optional arguments。

二者的差别在于参数有没有前缀“--”。
# - he --
'-n’可称为是flag，起作用可为在cmd中方便输入命令，而不会保存为argparse中的参数。但是没有--的情况下，会默认--的参数名字去保存参数值。
里有一个约定俗成的惯例：单个字母只是用一个 - ，多个字母使用两个 - (--)。python也支持一个 - 后面跟多个字母，不过看起来有关怪异。上面的定义 -s 显然是 --sn 的简写。
可见，当有多个字符串时，参数的识别是通过“–”，而不是字符串的长度。
# 可选参数
#!/usr/bin/env python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', 
    help="shows output")
args = parser.parse_args()
if args.output:
    print("This is some output")

# -c参数的dest='cpp'
dest参数就可以排上用场。或者参数本身的含义不够明确，比如 -r -k -i -t 等等，直接在代码中使用可读性不好，这时用dest来给他们指定一个可读性更好的名称。
>>> import argparse

>>> parser = argparse.ArgumentParser()

>>> parser.add_argument('-a', '--apple')
# 参数解析器metavar
它为帮助消息中的可选参数提供了不同的名称。在add_argument（）中为metavar关键字参数提供一个值。
add_argument函数的metavar参数，用来控制部分命令行参数的显示，注意：它只是影响部分参数的显示信息，不影响代码内部获取命令行参数的对象。
对于有nargs参数的命令行参数，可以用metavar来设置每一个具体的参数的名称：

>>> parser = argparse.ArgumentParser(prog='PROG')

>>> parser.add_argument('-x', nargs=2)

>>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))

>>> parser.print_help()

usage: PROG [-h] [-x X X] [--foo bar baz]

optional arguments:

-h, --help show this help message and exit

-x X X

--foo bar baz
为错误的期望值命名
https://blog.csdn.net/xixihahalelehehe/article/details/121199110?ops_request_misc=&request_id=&biz_id=102&utm_term=metavar&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-121199110.142^v73^wechat_v2,201^v4^add_ask,239^v1^insert_chatgpt&spm=1018.2226.3001.4187