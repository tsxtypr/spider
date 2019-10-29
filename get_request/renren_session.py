import requests

#登录之前的url
base_url="http://www.renren.com/PLogin.do"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    "Cookie":"anonymid=k2b8ozqbnw51u7; wp=0; wp_fold=0; depovince=JL; jebecookies=f7f692e1-f8d8-4f8d-9b74-edff4e039ad0|||||; _r01_=1; JSESSIONID=abcnAyEQRYsmn7ywWxv4w; ick_login=a67c37e5-24a8-4b70-b242-f6fc1d6639ac",
    "Host":"www.renren.com",
    "Referer":"http://www.renren.com/972683127/newsfeed/photo",
}

#用户名、密码
data={
"email":"xxxx",
"password":"123456"
}

proxies={
    "http":"http://114.239.1.245:808",
    "http":"http://117.69.200.250:9999",
    "http":"http://27.43.184.161:9999",
}

se=requests.session()
se.post(url=base_url,headers=headers,data=data)
#获取登录后的url
response=se.get("http://www.renren.com/972683127",headers=headers)
if "刘柯柯" in response.text:
    print("登录成功，已进入到首页")
    print(response.text)
else:
    print("登录失败")