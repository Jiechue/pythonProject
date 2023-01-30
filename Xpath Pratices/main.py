from lxml import etree

xml = """
<book>
    <author>
        <nick>张三</nick>
        <nick>李四</nick>
        <nick>王五</nick>
        <div>
            <nick>Jack</nick>
        </div>
        <span>
            <nick>Tom</nick>
        </span>
    </author>
</book>
"""

tree = etree.XML(xml)
result = tree.xpath("/book/author/*/nick/text()")
result2 = tree.xpath("/book/author//nick/text()")

print(result)
print(result2)