from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import lxml.html
import lxml.html.soupparser

page_sh = ["http://shtrih-m.com.ua/production/elcomm-scales/chekopechat/vesy-s-pechatyu-etiketki-print-f1-2mb.html",
        "http://shtrih-m.com.ua/production/elcomm-scales/chekopechat/vesy-s-pechatyu-etiketki-print-m-2mb.html"]
page_slav = ["http://rsc.zp.ua/shtrih-print-m4-5"]
page_promua = ["http://prom.ua/search?category=50908&search_term=%D1%82%D0%B5%D1%80%D0%BC%D0%BE%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%BE%D1%81%D0%B0+%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D0%B0&page=1"]
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
        price = bsObj.findAll("span",attrs={"class":"cost"})
        print(title.get_text())
        for el in price:
            print(el.get_text())
    except AttributeError as e:
        return None
    return price

def getTitleAll(url,t1,t2,t3):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
        price = bsObj.findAll(t1,attrs={t2:t3})
        print(title.get_text())
        for el in price:
            print(el.get_text())
    except AttributeError as e:
        return None
    return price

def getPageAllPromua(url,t1,t2,t3,name):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html, 'html.parser')
        title = bsObj.html.head.title.contents
        firma = bsObj.findAll(t1,attrs={t2:name})
        price = bsObj.findAll(t1, attrs={t2: t3})

        for el in range(len(firma)):
            print(firma[el].get_text(),price[el].get_text())
        print(len(firma))
        print(title)

    except AttributeError as e:
        return None
    return price

#for pr in page_slav:
#    getTitleAll(pr,"div","class","price")
for pr in page_promua:
    getPageAllPromua(pr,"div","class","x-gallery-tile__price","x-gallery-tile__name_type_company")
#for pr in page_sh:
#    getTitle(pr)




 #html = urlopen("http://shtrih-m.com.ua/production/elcomm-scales/chekopechat/vesy-s-pechatyu-etiketki-print-f1-2mb.html")
 #bsObj = BeautifulSoup(html)
 #nameList = bsObj.findAll("span", {"class": "cost"})
 #for name in nameList:
 #    print(name.get_text())
