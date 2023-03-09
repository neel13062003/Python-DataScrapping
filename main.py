import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range (2,10):
    url = "https://www.flipkart.com/search?q=mobile+under+15000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    """To getting status code"""
    r= requests.get(url)
    # print(r)
    """200 means we can get their html to scrapt data"""

    #soup  = BeautifulSoup(r.text,"html.parser")
    #print(soup)

    """while True:"""
    # np =  soup.find("a", class_ = "_1LKTO3").get("href")
    # cnp = "https://www.flipkart.com" + np
    # print(cnp)

    #soup means whole page content
    soup = BeautifulSoup(r.text,"html.parser")
    #box - perticular content
    box =  soup.find("div",class_ = "_1YokD2 _3Mn1Gg")

    #1
    names = box.find_all("div",class_ = "_4rR01T")
    #print(names)

    for i in names:
        name = i.next
        Product_name.append(name)

    #print(Product_name)

    #2
    prices = box.find_all("div",class_ = "_30jeq3 _1_WHN1")
    #print(prices)

    for i in prices:
        name =  i.next
        Prices.append(name)

    #print(Prices)


    #3
    dis = box.find_all("ul",class_ = "_1xgFaf")
    #print(names)

    for i in dis:
        name = i.next
        Description.append(name)

    #print(Description)


    #4
    reviews = box.find_all("div",class_ = "_3LWZlK")
    #print(names)

    for i in reviews:
        name = i.next
        Reviews.append(name)

    #print(Reviews)


    #24
    #print(len(Reviews))

min_len = min(len(Product_name), len(Prices), len(Description), len(Reviews))
Product_name = Product_name[:min_len]
Prices = Prices[:min_len]
Description = Description[:min_len]
Reviews = Reviews[:min_len]

#now target is to add in dataframe and then add into csev(excel format)
df= pd.DataFrame({"Product_name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})

#print(df)

df.to_csv("Flipkart_mobile_prices_under_15000.csv")

#ondesire location
#df.to_csv("C:/SEM_6/Flipkart_mobile_prices_under_15000.csv")


















# In Flipkart case links are like end ...1,...2 so here not works
# url = cnp
# r= requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")

