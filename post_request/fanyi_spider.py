import requests

base_url="https://fanyi.baidu.com/sug"

kw="python"
data={
    "kw":kw
}

headers={
    "content-length":str(len(kw)),
    "content-type":"application/x-www-form-urlencoded;",
    "origin":"https://fanyi.baidu.com",
    "referer":"https://fanyi.baidu.com/",
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    "x-requested-with":"XMLHttpRequest"
}

response=requests.post(url=base_url,headers=headers,data=data)
#post请求返回的数据都是json数据
print(response.json()["data"])
result=""
for data in response.json()["data"]:
    result+=data["v"]+"\n"
print(result)