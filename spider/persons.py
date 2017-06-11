import requests
from bs4 import BeautifulSoup
from spider.common import headers,get_proxy,itjuzi
import time
'''
该爬虫用于爬取it橘子的创投人物
'''
# persons表
persons = itjuzi['persons']

def get_and_insertdb_persons(soup):
    if soup.title is None:
        return None
    ul = soup.select_one('ul[class="list-main-personset person-list-result"]')
    if ul.select('li'):
        lilist = ul.select('li')
    else:
        pass
    for perli in lilist:
        liright = perli.select_one('i[class="right"]')
        name = liright.select_one('a[class="name"]').get_text()
        link = liright.select_one('a[class="name"]').get('href')
        des = liright.select_one('a[class="des"]').get_text()
        intro = perli.select_one('p[class="intro"]').get_text()
        data = {'name':name,'link':link,'des':des,'intro':intro}
        persons.insert_one(data)
    print('successful')

def run_spider(url):
    response = requests.get(url,headers=headers,proxies=get_proxy()).content
    soup = BeautifulSoup(response,'lxml')
    result = get_and_insertdb_persons(soup)
    if result is None:
        pass

# url = 'https://www.itjuzi.com/person?page=1'
# run_spider(url)

def start():
    baseurl = 'https://www.itjuzi.com/person?page='
    # run_spider(baseurl)
    urls = [baseurl+str(i) for i in range(20,30)]
    for url in urls:
        run_spider(url)
        time.sleep(2)

start()