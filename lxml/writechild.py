from lxml import etree

root=etree.Element('root')
print(root.tag)
child=etree.SubElement(root,'child') # 添加一个子节点
child1=etree.SubElement(root,'child1') # 添加一个子节点
child.set('id','test_Id')
child1.set('id1','test_Id1')
child2=etree.SubElement(child,'child2')
child3=etree.SubElement(child1,'child3')
child2.set('id2','test_Id2')
child3.set('id3','test_Id3')
print(etree.tostring(root))   