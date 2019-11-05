import threading
import time
import requests
import json
from queue import Queue

class Douban(threading.Thread):
    def __init__(self,name,q):
        super().__init__()
        self.url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=' + str(
            timestamp * 1000) + '&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn'
        self.headers={
            'user-agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        }
        self.name=name
        self.q=q

    def run(self):
        self.get_link()

    def get_link(self):
        while True:
            if not self.q.empty():
                page=self.q.get()
                print(f'{self.name}执行了第{page}页')
                url=self.url % page
                page = requests.get(url=url, headers=self.headers)
                page_data = json.loads(page.text)
                datas = page_data['Data']['Posts']
                links = []
                for each in datas:
                    link = 'http://careers.tencent.com/jobdesc.html?postId=' + each['PostId']
                    links.append(link)
                # print(links)
                self.save_file(links)
            else:
                break

    def save_file(self,data):
        with open('douban_ajax.txt','a+',encoding='utf-8') as f:
            f.writelines(data)

if __name__ == '__main__':
    start=time.time()
    timestamp = time.time()
    #先定义一个消息队列
    q=Queue()
    #将所有页码放入到消息队列中
    for i in range(30):
        q.put(i)
    #定义一个列表，用于开几个线程
    name_list=['aa','bb','cc','dd']
    #在建一个列表，用于阻塞主线程
    xc_list=[]
    for name in name_list:
        #分别执行进程
        t=Douban(name,q)
        t.start()
        xc_list.append(t)
    #将所有的线程阻塞主线程
    for j in xc_list:
        j.join()
    print(time.time()-start)