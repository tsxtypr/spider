import requests
from xml import etree
base_url="http://www.baidu.com/more/"

response=requests.get(url=base_url)

# print(response.text)
#第一种：解决乱码
# response.encoding="utf-8"
# print(response.text)

#状态头中
print(response.status_code)
#响应头中
print(response.headers)


with open('index.html','w',encoding='utf-8') as f:
    #第二种
    # 解决乱码  将二进制文件转换成utf-8
    f.write(response.content.decode("utf-8"))

# text_xpath=etree.HTML(response)
# title=text_xpath.xpath('//div[@id="content"]/div[@class="con"]/')