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