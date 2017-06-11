# ITJuZi spider
a python spider that to crawl the www.itjuzi.com

# 环境
python 3.6 
MongoDB 3.4
# 包
pymonogo 3.4.0
lxml 3.7.3
requests 2.13.0
bs4 0.0.1

此项目的功能是爬取IT橘子网的数据，并将数据存储到mongodb中

## 说明
# 爬取IT橘子的投资速递数据
# 'https://www.itjuzi.com/investevents?page='
inverstevents.py
# 爬取IT橘子的产品数据
# 'https://www.itjuzi.com/product?page='
products.py
# 爬取IT橘子的创投人物
# 'https://www.itjuzi.com/person?page='
persons.py
# 爬虫入口，运行之前可能需要修改
run.py

## 意外   
IT橘子对访问的数据页有限制，product和investevents、persons的数据page超过20后就获取不到数据了
需要爬取超过page20更多数据需要开通雷达会员或使用付费API服务 。
更多信息待日后尝试
