from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
''''
takes the entire html content and pass it in with bs4
'''

class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
