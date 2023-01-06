import requests
import re
import csv

f = open("data.csv", mode="w")
csvWriter = csv.writer(f)
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>'
                 , re.S)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

for star in range(0,250,25):
    url = "https://movie.douban.com/top250?start={star}"

    resp = requests.get(url=url, headers=headers)

    result = obj.finditer(resp.text)

    for i in result:
        print(i.group("name"))
        print(i.group("year").strip())
        print(i.group("score"))
        print(i.group("num"))
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvWriter.writerow(dic.values())

f.close()
print("over!")