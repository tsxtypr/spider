import threading
import time
import requests
import json

class Douban:
    def __init__(self,url):
        self.url=url
        self.headers={
            'user-agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        }
        self.get_link()

    def get_link(self):
        page = requests.get(url=url, headers=self.headers)
        page_data = json.loads(page.text)
        datas = page_data['Data']['Posts']
        links = []
        for each in datas:
            link = 'http://careers.tencent.com/jobdesc.html?postId=' + each['PostId']
            links.append(link)
        print(links)

if __name__ == '__main__':
    for i in range(1,3):
        timestamp = time.time()
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=' + str(
            timestamp * 1000) + '&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=' + str(
            i) + '&pageSize=10&language=zh-cn&area=cn'
        Douban(url)