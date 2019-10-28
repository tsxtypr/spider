import requests
import os

base_url="http://tieba.baidu.com/f?"

#封装请求头
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}

kw="李钟硕"
dirname='./tieba/'+kw

#自动创建贴吧相对应的文件夹
if not os.path.exists(dirname):
    os.mkdir(dirname)

for i in range(10):
    #封装请求参数
    params={
        "kw":kw,
        "ie":"utf-8",
        "pn": str(50*i)
    }
    response=requests.get(url=base_url,params=params,headers=headers)

    with open(dirname+'/%s.html'%i,'w',encoding="utf-8") as f:
        f.write(response.content.decode("utf-8"))