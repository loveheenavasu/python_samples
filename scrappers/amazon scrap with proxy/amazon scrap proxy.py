import requests
from bs4 import BeautifulSoup
from random import choice
import json
def get_proxy():
    proxies= []
    url="https://free-proxy-list.net/"
    response=requests.get(url)
    htmlcontent=response.content
    soup=BeautifulSoup(htmlcontent,'html.parser')
    for a in soup.find('tbody').find_all('tr'):
        proxies_list=a.find_all('td')[0].text
        port=a.find_all('td')[1].text
        proxies.append(proxies_list+':'+port)
    return proxies

def random_proxy(proxies):
     return {"https://" : choice(proxies)}

proxies=get_proxy()
def get_working():
    working=[]
    for i in range(20):
        proxy=random_proxy(proxies)
        # print(f"using {proxy}...")
        try:
            r=requests.get('https://www.google.com',proxies=proxy,timeout=2)
            if r.status_code == 200:
                working.append(proxy)   
        except:
            pass
   
    return working

get_proxy()
    
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

url='https://www.amazon.in/s?k=mobile&sprefix=mo%2Caps%2C372&ref=nb_sb_ss_softlines-tsdoa-joint-contextual-iss_2_2'
proxy=choice(get_working())
r=requests.get(url,headers=headers,proxies=proxy)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,'html.parser')
dataArr=[]
for result in soup.findAll('div',attrs={'data-component-type':'s-search-result'}):
    name=result.find('h2',attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).a.text
    try:
        price=result.find('span','a-price')
        prices=price.find('span','a-offscreen').text
    
    except AttributeError:
        pass
    image=result.find('img',attrs={'class':'s-image'}).get('src')
    link=result.find('h2',attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).a.get('href')
    product_url='https://www.amazon.in'+link
    url2=product_url
    response=requests.get(url2,headers=headers,proxies=proxy)
    htmlcontent2=response.content
    soup2=BeautifulSoup(htmlcontent2,'html.parser')
    try:
        for a in soup2.find_all('div',attrs={'id':'availabilityInsideBuyBox_feature_div'}):
            check=a.find('span',attrs={'class':'a-size-medium a-color-success'}).text
        
    except AttributeError:
        pass

    
   
    dataArr.append({
        'name':name,
        'price':prices,
        'ProductLink':product_url,
        'image':image,
        'stock':check
    })
with open("amazon.json", "w") as jsonfile:
    json.dump(dataArr, jsonfile, indent=3)
