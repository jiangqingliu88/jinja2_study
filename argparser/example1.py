from argparse import ArgumentParser
# python
from argparse import Namespace

# python

parser = ArgumentParser()
parser.add_argument('--foo', dest='jjj', type=str, required=True)
parser.add_argument('-env', choices=['test', 'prod'])
a = parser.parse_args(['--foo', 'werw', '-env', '234'])

print(a.env)
# 输出 234

#b = B()
b=parser.parse_args(['--foo', 'werw', '-env', '234'], namespace=b)
print(b.env)
# 输出 234
# python
a = Namespace(env='test', level=2)
print(a.evn)
# 输出 test
print(a.level)
# 输出 2
