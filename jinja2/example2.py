from jinja2 import Template, FileSystemLoader, Environment
j2_loader = FileSystemLoader('./')
env = Environment(loader=j2_loader)
j2_tmpl = env.get_template('./jinja2_for.j2')
# 传入一个列表，对列表里面的人打招呼
names = ['Zhang San', 'Li Si', 'Wang Wu']
result = j2_tmpl.render(names=names)
print(result)
