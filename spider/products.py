from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
from spider.common import itjuzi,get_proxy,headers
import time
'''
用于爬取it橘子的产品库数据
'''

# 存放产品信息的数据表
products = itjuzi['products']

def get_simple_message(soup):
    lilist = soup.select_one('ul[class="list-main-prodset"]').select('li')
    for perli in lilist:
        link = perli.select_one('a')
        href = link.get('href')
        appid = get_appid(href)
        name = link.select_one('p[class="title"]').get_text()
        type = link.select_one('p[class="des"]').get_text()
        data = {'name':name,'appid':appid,'link':href,'type':type}
        # 存储到mongodb中
        products.insert_one(data)
    print('successful')

def get_appid(url):
    response = requests.get(url,headers=headers,proxies=get_proxy()).content
    soup = BeautifulSoup(response,'lxml')
    appid = soup.select_one('div[class="mart10"]').select('div')[3].span.get_text()
    return appid

def run_spider(url):
    response = requests.get(url,headers=headers,proxies=get_proxy())
    soup = BeautifulSoup(response.content,'lxml')
    get_simple_message(soup)

def start():
    baseurl = 'https://www.itjuzi.com/product?page='
    urls = [baseurl+str(i) for i in range(1,10)]
    for url in urls:
        run_spider(url)
        time.sleep(2)


start()