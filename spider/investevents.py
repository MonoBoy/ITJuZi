import requests
from bs4 import BeautifulSoup
import time
from spider.common import get_proxy,itjuzi
'''
it橘子投资速递信息
    时间，公司名称，公司logo，业务类型，地址，投资阶段，投资金额，投资方，详情地址
'''

investevents = itjuzi['investevents'] # 表

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}


def get_investevents_and_insertdb(soup):
    # if soup.title is None:
    #     pass
    lilist = soup.select_one('ul[class="list-main-eventset"]').select('li')
    for li in lilist:
        celldate = li.select_one('i[class="cell date"]').span.get_text()
        cellpic = li.select_one('i[class="cell pic"]').a.select_one('img')
        # some image is None
        if cellpic:
            cellpic = cellpic.get('src')
        else:
            cellpic = "this picture is missing"
        companytitle = li.select_one('p[class="title"]').a.span.get_text().strip()
        companytype = li.select_one('p:nth-of-type(2)').select_one('span[class="tags t-small c-gray-aset"]').get_text().strip()
        address = li.select_one('p:nth-of-type(2)').select_one('span[class="loca c-gray-aset t-small"]').get_text().strip()
        # 融资阶段
        cellround = li.select_one('i[class="cell round"]').a.span.get_text().strip()
        cellmoney = li.select_one('i[class="cell money"]').get_text().strip()
        # 投资方
        investorset = li.select_one('i[class="cell name"]').select_one('div[class="investorset"]').get_text().replace('\n','')
        detailurl = li.select_one('i[class="cell detail"]').a.get('href')
        data = {'celldate':celldate, 'cellpic':cellpic, 'companytitle':companytitle, 'companytype':companytype, 'address':address, 'cellround':cellround, 'cellmoney':cellmoney, 'investorset':investorset, 'detailurl':detailurl}
        investevents.insert_one(data)
    print("successful")

def run_collection(url):
    '''start to run the spider'''
    response = requests.get(url, headers=headers, proxies=get_proxy())
    soup = BeautifulSoup(response.content,'lxml')
    get_investevents_and_insertdb(soup)


def find(limit=2):
    table = investevents.find().limit(limit)
    return table

def start():
    baseurl = 'https://www.itjuzi.com/investevents?page='
    #'https://www.itjuzi.com/investevents?page=2'
    urls = [baseurl+str(i) for i in range(20,40)]
    for url in urls:
        run_collection(url)
        time.sleep(2)


start()