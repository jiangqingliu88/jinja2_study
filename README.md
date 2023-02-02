# jinja2_study
jinja2 study
file_source https://blog.csdn.net/q965844841qq/article/details/105532428
# 基本语法：

语句 {% ... %}
变量 {{ ... }}
注释 {# ... #}
# 基本用法
from jinja2 import Template

tmpl = Template('hello {{ name}}')
result = tmpl.render(name = '111')
print(result)
# 打印结果
hello 111
