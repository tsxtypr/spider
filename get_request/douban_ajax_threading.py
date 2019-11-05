import threading
import time
import requests
import json

class Douban(threading.Thread):
    def __init__(self,url):
        super().__init__()
        self.url=url
        self.headers={
            'user-agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        }

    def run(self):
        self.get_link()

    def get_link(self):
        page = requests.get(url=url, headers=self.headers)
        page_data = json.loads(page.text)
        datas = page_data['Data']['Posts']
        links = []
        for each in datas:
            link = 'http://careers.tencent.com/jobdesc.html?postId=' + each['PostId']
            links.append(link)
        # print(links)
        self.save_file(links)

    def save_file(self,data):
        with open('douban_ajax.txt','a+',encoding='utf-8') as f:
            f.writelines(data)
if __name__ == '__main__':
    for i in range(1,20):
        timestamp = time.time()
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=' + str(
            timestamp * 1000) + '&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=' + str(
            i) + '&pageSize=10&language=zh-cn&area=cn'
        douban=Douban(url)
        t=threading.Thread(target=douban.get_link)
        t.run()