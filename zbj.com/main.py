from lxml import etree
import requests
url = "https://guangzhou.zbj.com/search/service/?kw=saas&r=2&l=0"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
resp = requests.get(url)
# print(resp.text)
html = etree.HTML( resp.text)
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div')
for div in divs:
    price = div.xpath('.//*[@class="price"]/span/text()')[0].strip("￥")
    name = div.xpath('.//*[@class="name-pic-box"]/a/text()')[0]
    print(name)
    print(price)
