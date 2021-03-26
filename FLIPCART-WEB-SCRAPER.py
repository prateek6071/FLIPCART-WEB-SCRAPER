from bs4 import BeautifulSoup
import pandas as pd
import requests


def extract(page):

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    url = 'https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='  + str(page)

    r=requests.get(url).text
    soup=BeautifulSoup(r,'lxml')
    divs=soup.find_all('div',class_='_1AtVbE col-12-12')
    for items in divs:
        product_name=items.find('div',class_='_4rR01T')
        price=items.find('div',class_='_30jeq3 _1_WHN1')
        description=items.find('div',class_='rgWa7D')
        mobilephone={
        'name':product_name,
        'price':price,
        'description':description

              }
        joblist.append(mobilephone)

    return


joblist=[]

for i in range(0,11,3):
    print(f'Getting page,{i}')
    c=extract(i)


df=pd.DataFrame(joblist)
print(df.head())
df.to_csv('flipcart_phones.csv')