import requests,time,random
import hashlib

base_url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

word="python"
def get_md5(value):
    md5=hashlib.md5()
    md5.update(value.encode("utf-8"))
    return md5.hexdigest()

#解决更换搜索词查询不到数据的问题
ts=str(time.time()*1000)
salt=ts+str(random.randint(1,10))
sign=str(get_md5("fanyideskweb"+word+salt+"n%A-rKaT5fb[Gy?;N5@Tj"))

data={
    'i':word,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':salt,
    'sign':sign,
    'ts':ts,
    'bv':'682084bf0823beb3fe92fb9559a5e3f0',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}

headers={
    'Content-Length': str(len(word)),
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1118531613@111.197.148.217; _ntes_nnid=c1819f6b2cea918022060eb2eb423301,1570871035552; OUTFOX_SEARCH_USER_ID_NCOO=1475724906.500016; JSESSIONID=aaawYSgzJ3iE6-PjTrr4w; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcbcDpBVjhFLdShlur4w; ___rl__test__cookies=1572251724286',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


response=requests.post(url=base_url,headers=headers,data=data)
#post返回的数据都是json格式的
print(response.json())