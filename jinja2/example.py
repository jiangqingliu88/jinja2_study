from jinja2 import Template

tmpl = Template('hello {{ name}}')
result = tmpl.render(name = '111')
print(result)

