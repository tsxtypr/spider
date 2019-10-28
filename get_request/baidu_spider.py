import requests

base_url="https://www.baidu.com/"

# 封装请求头
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}

response=requests.get(url=base_url,headers=headers)

# print(response.text)

with open('baidu.html','w',encoding="utf-8") as f:
    f.write(response.content.decode("utf-8"))