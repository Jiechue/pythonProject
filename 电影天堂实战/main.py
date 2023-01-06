import requests
import re

domain = "https://www.dytt89.com"

resp = requests.get(url=domain, verify=False)
resp.encoding = "gb2312"
# print(resp.text)

obj1 = re.compile(r"2023必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)

child_href_list = []
result1 = obj1.finditer(resp.text)
for i in result1:
    ul = i.group('ul')
    # print(ul)
    result2 = obj2.finditer(ul)
    for l in result2:
        href = l.group('href')
        child_href = domain + href
        child_href_list.append(child_href)
        # print(child_href_list)

obj3 = re.compile(r'◎片　　名　(?P<movieName>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)"', re.S)
for href in child_href_list:
    child_resp = requests.get(url=href, verify=False)
    child_resp.encoding = "gb2312"
    result3 = obj3.search(child_resp.text)
    print(result3.group("movieName"))
    print(result3.group("download"))