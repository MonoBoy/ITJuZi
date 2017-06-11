import random
import pymongo
'''
common code
'''
client = pymongo.MongoClient('127.0.0.1',27017)
itjuzi = client['itjuzi'] # 数据库
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}
def get_proxy():
    proxy_list = [
        'http://117.177.250.151:8881',
        'http://111.85.219.250:3129',
        'http://122.70.183.138:8118'
    ]
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies