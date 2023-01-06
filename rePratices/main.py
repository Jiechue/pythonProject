import re
# findall search all
lst = re.findall("m", "model,mo,ma,aa,ba")
print(lst)
# search,search first,global search
lst = re.search(r'\d', "before 5 a.m,give me 3 millions dollar").group()
print(lst)
# finditer return iterator
lst = re.finditer("m", "model,mo,ma,aa,ba")
print(lst)
for i in lst:
    print(i.group())

# match,search start from scratch such as ^\d
lst = re.match(r"\d+", "10086,我的电话是:11111").group()
print(lst)

# preload
com = re.compile(r"\d+")
print(com.findall("10086,110,119,aa1"))

s = """
<div class='a1'><span id='1'>one</span></div>
<div class='a2'><span id='2'>two</span></div>
<div class='a3'><span id='3'>three</span></div>
<div class='a4'><span id='4'>four</span></div>
<div class='a5'><span id='5'>five</span></div>
"""

# re.S: 匹配换行 #(?P<group name>)
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<aaa>.*?)</span></div>", re.S)

result = obj.finditer(s)
for it in result:
    print(it.group("aaa"))