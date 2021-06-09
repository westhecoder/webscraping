import requests

from pages.all_books_page import AllBooksPage

page_content = requests.get('https://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books

'''
for book in books:
    print(book)
'''

for page_num in range(1, 50):
    url = f'https://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books)
