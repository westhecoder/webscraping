import requests
from bs4 import BeautifulSoup

page = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find_all('h3'))
