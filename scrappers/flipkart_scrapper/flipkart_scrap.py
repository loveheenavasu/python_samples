from bs4 import BeautifulSoup
import requests
import json
url='https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'
response=requests.get(url)
htmlcontent=response.content
soup=BeautifulSoup(htmlcontent,'html.parser')
dataArr=[]
for d in soup.findAll('div',attrs={'class':'_2kHMtA'}):
      title=d.find('div',attrs={'class':'_4rR01T'}).text
      price=d.find('div',attrs={'class':'_30jeq3 _1_WHN1'}).text
      image=d.find('img',attrs={'class':'_396cs4 _3exPp9'})   
      dataArr.append({
        'title':title,
        'price':price,
        'image':image.get('src')
    })
with open("flipkart.json", "w") as jsonfile:
    json.dump(dataArr, jsonfile, indent=3)

with open("flipkart.json", "r") as f1:
    file1 = json.loads(f1.read())
    
with open("flipkartsample.json", "r") as f2:
    file2 = json.loads(f2.read())


def comparing_json():
    flag = 0
    sample_keys = []
    for i in file2:
        sample_keys.append(list(i.keys()))
        real_keys = []
    for j in file1:
        real_keys.append(list(j.keys()))
    for i in sample_keys:
        for j in real_keys:
            if set(i) == set(i).intersection(set(j)):
                flag = 1
            else:
                break
        break
    if flag !=0 :
        return 'Correct json'
    else:
        return 'Incorrect json'

print(comparing_json())