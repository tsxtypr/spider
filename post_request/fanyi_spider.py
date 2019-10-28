# import requests
#
# base_url="https://fanyi.baidu.com/sug"
#
# kw="python"
# data={
#     "kw":kw
# }
#
# headers={
#     "content-length":str(len(kw)),
#     "content-type":"application/x-www-form-urlencoded;",
#     "origin":"https://fanyi.baidu.com",
#     "referer":"https://fanyi.baidu.com/",
#     "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
#     "x-requested-with":"XMLHttpRequest"
# }
#
# response=requests.post(url=base_url,headers=headers,data=data)
# #post请求返回的数据都是json数据
# print(response.json()["data"])
# result=""
# for data in response.json()["data"]:
#     result+=data["v"]+"\n"
# print(result)


#面向对象，对请求的数据进行封装
import requests

class Search_words:
    def __init__(self,words):
        self.words=words
        self.base_url="https://fanyi.baidu.com/sug"
        self.data={
    "kw":self.words
}
        self.headers={
    "content-length":str(len(self.words)),
    "content-type":"application/x-www-form-urlencoded;",
    "origin":"https://fanyi.baidu.com",
    "referer":"https://fanyi.baidu.com/",
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    "x-requested-with":"XMLHttpRequest"
}
    def get_data(self):
        response=requests.post(url=self.base_url,headers=self.headers,data=self.data)
        result=""
        for data in response.json()["data"]:
            result+=data["v"]+"\n"
        return result
    def __str__(self):
        return self.get_data()

if __name__ == '__main__':
    data=Search_words("python")
    print(data)