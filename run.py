from spider import investevents,persons,products
# run these spiders to crawl some data from www.itjuzi.com
if __name__ == '__main__':
    investevents.start()
    print('investevents was over')
    persons.start()
    print('persons was over')
    products.start()
    print('products was over')