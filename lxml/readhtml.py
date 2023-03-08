#提取html中的数据
from lxml import etree


text = '''
<html>
        <div class="clearfix">
        <div class="nav_com">
          <ul>
              <li class="active"><a href="/">推荐</a></li>
              <li class=""><a href="/nav/python">Python</a></li>
              <li class=""><a href="/nav/java">Java</a></li>
              <li class=""><a href="/nav/web">前端</a></li>
              <li class=""><a href="/nav/arch">架构</a></li>
              <li class=""><a href="/nav/db">数据库</a></li>
              <li class=""><a href="/nav/5g">5G</a></li>
              <li class=""><a href="/nav/game">游戏开发</a></li>
              <li class=""><a href="/nav/mobile">移动开发</a></li>
              <li class=""><a href="/nav/ops">运维</a></li>
          </ul>
        </div>
        </div>
</html>>
</html>>


'''
#将字符串解析为html文档
html = etree.HTML(text)
#print(html)
#将字符串序列化为html
result = etree.tostring(html).decode('utf-8')
print(result)

