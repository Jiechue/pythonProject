import requests

query = input("请输入要查找的信息")

url = "https://www.baidu.com/s?wd={query}"

#伪装标头，让服务器以为是浏览器访问
head = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.54"
}

resp = requests.get(url, headers=head)

print(resp)
print(resp.text)
resp.close()