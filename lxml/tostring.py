from lxml import etree
root = etree.XML('<root><a><b/></a></root>') 
print(etree.tostring(root))                        #default: method = 'xml'
print(etree.tostring(root, encoding='iso-8859-1')) #设置编码方式为 iso-8859-1
print(etree.tostring(root, pretty_print=True))     # 格式化
root = etree.XML('<html><head/><body><p>Hello<br/>Python知识学堂</p></body></html>')
etree.tostring(root, method='xml')                 # 默认值为：xml
etree.tostring(root, method='html')                #转成html
etree.tostring(root, method='text')                #转成文本即获取标签内的文本