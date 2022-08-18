

from bs4 import BeautifulSoup
import requests,openpyxl
exel=openpyxl.Workbook()
sheet=exel.active
sheet.title='Ebay'
print(exel.sheetnames)
sheet.append(['Product Url,Name,price,Image'])
for x in range(1,5):
        url='https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=mobiles&_sacat=0'
        response=requests.get(url+str(x))
        htmlcontent=response.content
        soup=BeautifulSoup(htmlcontent,'html.parser')
        for ebay in soup.findAll('li',attrs={'class':'s-item'}):
                link=ebay.find('a',attrs={'class':'s-item__link'})
                name=ebay.find('h3',attrs={'class':'s-item__title'}).text
                price=ebay.find('span',attrs={'class':'s-item__price'}).text
                image=ebay.find('img',attrs={'class':'s-item__image-img'})
                sheet.append([link.get('href'),name,price,image.get('src')])
                print(name)
exel.save('ebay.xlsx')
      
      
    
     
    
    
