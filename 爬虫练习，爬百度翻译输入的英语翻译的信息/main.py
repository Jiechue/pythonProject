import requests
url = "https://fanyi.baidu.com/sug"

s = input("请输入翻译的英语单词")
data = {
    "kw": s
}

resp = requests.post(url, data=data)
if resp:
    print(resp.json())