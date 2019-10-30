import re
import requests
import json

class Yaowang:
    def __init__(self,base_url):
        self.base_url=base_url
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
        self.medicine=[]
        self.parse()
    def parse(self):
        for i in range(1,51):
            print("正在爬取第%s页"%i)
            if i==50:
                print("爬取结束")
            url=self.base_url%i
            response=requests.get(url=url,headers=self.headers)

            #获取到包裹着数据的标签
            ul_pattern=re.compile(r'<ul id="itemSearchList" class="itemSearchList">(.*?)</ul>',re.S)
            ul_content=ul_pattern.search(response.text)
            if ul_content:
                ul_content=ul_content.group()
            # print(ul_content)

            li_pattern=re.compile(r'<li.*?>(.*?)</li>',re.S)
            li_list=li_pattern.findall(ul_content)
            # print(li_list)
            # print(len(li_list))

            for li in li_list:
                item = {}
                #价格
                price_pattern=re.compile(r'<p class="price".*?<span>(.*?)</span>',re.S)
                price=price_pattern.search(li).group(1).strip()
                # print(price)

                #描述
                desc_pattern=re.compile(r'<a class="productName.*?</span>(.*?)</a>',re.S)
                desc=desc_pattern.search(li).group(1).strip()
                # print(desc)

                #评论数量
                commend_num_pattern=re.compile(r'<span class="comment comment_right".*?<em>(.*?)</em>',re.S)
                commend_num=commend_num_pattern.search(li)
                if commend_num:
                    commend_num=commend_num.group(1)
                else:
                    commend_num = "没有评论数"
                # print(commend_num)

                #详情页链接
                detail_link_pattern=re.compile(r'<p class="titleBox">.*?href="(.*?)" target="_blank"',re.S)
                detail_link="https:"+detail_link_pattern.search(li).group(1).strip()
                # print(detail_link)

                item["价格"]=price
                item["描述"]=desc
                item["评论数量"]=commend_num
                item["详情链接"]=detail_link

                self.medicine.append(item)
        # print(self.medicine)
        # print(len(self.medicine))
        self.save_data(self.medicine)

    def save_data(self,data):
        with open('yaowang.json','w',encoding="utf-8") as f:
            json.dump(data,f)


if __name__ == '__main__':
    base_url="https://www.111.com.cn/categories/953710-j%s.html"
    Yaowang(base_url)