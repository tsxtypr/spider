import requests

url="https://search.sina.com.cn/?"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}

params={
    "q":"区块链",
    "c":"news",
    "from":"channel",
    "ie":"utf-8"
}

response=requests.get(url=url,headers=headers,params=params)

with open('sina_news.html','w',encoding="gbk") as f:
    f.write(response.content.decode("gbk"))