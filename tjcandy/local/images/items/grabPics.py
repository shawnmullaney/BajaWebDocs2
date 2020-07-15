#!/usr/bin/python
import re
import requests
from bs4 import BeautifulSoup

site = 'http://www.tjcandy.com/catalog/allitems?offset=0&limit=1500&col=description1&dir=ASC&terms=&queryCol='
site2 = "http://www.tjcandy.com/catalog/brands?view=brands&limit=1500"
response = requests.get(site2)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    print("Starting with " + str(len(urls)) + "urls")
    print("Working On " + str(url))
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
