# -*- coding: utf8 -*-

import requests
import bs4

heraldo = requests.get('https://www.elheraldo.co/')
soup = bs4.BeautifulSoup(heraldo.text, 'html.parser')

print(soup.title)

links_with_text = [link['href'] for link in soup.find_all("a", href=True) if link.text]

print( links_with_text )

for x in links_with_text:
    print(x)


url = 'https://elcomercio.pe'
response1 = requests.get(url)
soup1 = bs4.BeautifulSoup(response1.text, 'html.parser')

news = soup1.select('.page-link')

for item in news:
    print('---------------------------------------------')
    print(item.contents[0])