# http://automationpractice.com/
# Goal: scrap the product names and prices on the WOMEN category

import csv
import requests
from bs4 import BeautifulSoup

# name of website
baseURL = "http://automationpractice.com/"
# to bypass the security of the webpage
headers = {
    'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}
# request the page of the website that we want to work on
r = requests.get("http://automationpractice.com/index.php?id_category=3&controller=category", headers = headers).text
# read it with lxml
soup = BeautifulSoup(r,'lxml')

# create empty list
Items_names = []
Items_prices = []
price = []

# find the product's names
# note: find the tag-name and class-name where the product name is located
for i in soup.find_all('a', class_='product-name'):
    # convert it to text
    string = i.text
    # clear the extra spaces before and after the text
    Items_names.append( string.strip() )
    # remove the duplicates from list
    Item_name = Items_names[1:]
for k in Item_name:
    print(k)

# find the product's prices
for i in soup.find_all('span', class_='price product-price'):
    string = i.text
    Items_prices.append( string.strip() )
    # remove duplicates from items_prices list and store it in a new list
    [price.append(x) for x in Items_prices if x not in price]

for j in price:
    print(j)

# save it into a csv file: price and Item_name

# name of file
file_name = "women's_items.csv"
# write to csv file
with open(file_name,'w') as file:
    writer = csv.writer(file)
    # create three columns
    writer.writerow(['No', 'Item_name', 'price'])
    # write the item_name and price to csv
    for i in range(len(Item_name)):
        writer.writerow([i, Item_name[i], price[i]])










