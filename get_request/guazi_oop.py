import requests
from lxml import etree
import json

class Guazi:

    def __init__(self,base_url):
        self.base_url=base_url

    def get_content(self,url,headers):
        response=requests.get(url,headers=headers)
        return response.text

    #用于取xpath解析出来列表的元素
    def get_text(self,text):
        if text:
            return text[0]
        return ''

    #爬取所有车型的超链接
    def get_base_url(self,headers):
        html = self.get_content(url=self.base_url, headers=headers)
        # print(html)
        html_element=etree.HTML(html)
        href_list=html_element.xpath('//div[@class="dd-all clearfix js-brand js-option-hid-info"]/ul/li/p/a/@href')
        # print(href_list)
        for href in href_list:
            self.get_detail_content(href)
            return

    #获取详情页的text
    def get_detail_content(self,href):
        hrefs=href.split('#')
        href1=hrefs[1]
        href2=hrefs[2]
        for i in range(1,10):
            url="https://www.guazi.com{}{}#{}".format(href1,'/o'+str(i),href2)
            # print(url)
            headers={
                'Cookie':'uuid=4d2f2fbb-9410-41e7-e0bd-c7d68a0d5035; antipas=3r989zm896515f2606q138094P; cityDomain=bj; clueSourceCode=10103000312%2300; user_city_id=12; ganji_uuid=8338270205960639466855; sessionid=98021027-4853-4844-e96d-a190af032b79; lg=1; track_id=7539896610365440; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%25e4%25ba%258c%25e6%2589%258b%25e8%25bd%25a6%22%7D; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%25e4%25ba%258c%25e6%2589%258b%25e8%25bd%25a6%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%227539896610365440%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%224d2f2fbb-9410-41e7-e0bd-c7d68a0d5035%22%2C%22sessionid%22%3A%2298021027-4853-4844-e96d-a190af032b79%22%2C%22ca_city%22%3A%22bj%22%7D; preTime=%7B%22last%22%3A1572953576%2C%22this%22%3A1572952590%2C%22pre%22%3A1572952590%7D',
                'Host':'www.guazi.com',
                'Referer':'https://www.guazi.com/bj/buy/',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            }
            html=self.get_content(url,headers=headers)
            # print(html)
            self.get_detail_infos(html)

    #解析详情页
    def get_detail_infos(self,html):
        html_element=etree.HTML(html)
        li_list=html_element.xpath('//ul[@class="carlist clearfix js-top"]/li')
        info_list=[]
        for li in li_list:
            item={}
            title=self.get_text(li.xpath('.//h2[@class="t"]/text()'))
            # print(title)
            price1=self.get_text(li.xpath('.//div[@class="t-price"]/p/text()'))
            price2=self.get_text(li.xpath('.//div[@class="t-price"]/p/span/text()'))
            price=price1+price2
            year=self.get_text(li.xpath('.//div[@class="t-i"]/text()'))
            kilometre=li.xpath('.//div[@class="t-i"]/text()')[1]
            # print(kilometre)
            img_url=self.get_text(li.xpath('.//img/@src'))
            detail_url=self.get_text(li.xpath('.//a/@href'))
            item['title']=title
            item['price']=price
            item['year']=year
            item['kilometre']=kilometre
            item['img_url']=img_url
            item['detail_url']=detail_url
            # print(item)
            info_list.append(item)
            self.save_data(info_list)

    def save_data(self,data):
        with open('guazi.txt','a+',encoding='utf-8') as f:
            json.dump(data,f)

    def main(self):
        headers={
            'Cookie':'uuid=4d2f2fbb-9410-41e7-e0bd-c7d68a0d5035; antipas=3r989zm896515f2606q138094P; cityDomain=bj; clueSourceCode=10103000312%2300; user_city_id=12; ganji_uuid=8338270205960639466855; sessionid=98021027-4853-4844-e96d-a190af032b79; lg=1; track_id=7539896610365440; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%25e4%25ba%258c%25e6%2589%258b%25e8%25bd%25a6%22%7D; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22%25e7%2593%259c%25e5%25ad%2590%25e4%25ba%258c%25e6%2589%258b%25e8%25bd%25a6%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%227539896610365440%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%224d2f2fbb-9410-41e7-e0bd-c7d68a0d5035%22%2C%22sessionid%22%3A%2298021027-4853-4844-e96d-a190af032b79%22%2C%22ca_city%22%3A%22bj%22%7D; preTime=%7B%22last%22%3A1572952856%2C%22this%22%3A1572952590%2C%22pre%22%3A1572952590%7D',
            'Host':'www.guazi.com',
            'Referer':'https://www.guazi.com/bj/?ca_n=tbmkbturl&scode=10103000312&ca_s=pz_baidu&tk_p_mti=ad.pz_baidu.tbmkbturl.1.7539896610365440',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        }
        self.get_base_url(headers)

if __name__ == '__main__':
    base_url = "https://www.guazi.com/bj/mazda/bread"
    g=Guazi(base_url)
    g.main()