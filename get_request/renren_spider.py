import requests

#使用登陆后的url
base_url="http://www.renren.com/972683127"

headers={
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
"Cookie":"xxxx"
}

response=requests.get(url=base_url,headers=headers)
print(response.text)