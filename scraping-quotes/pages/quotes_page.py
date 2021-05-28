from bs4 import BeautifulSoup

from  locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser
'''
contains code to use locators to find particular things in a page

code related to getting data out of the quotes page
'''
class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser') #lets us search within this page

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE #finds a locator
        quote_tags = self.soup.select(locator) #selects every div with a quote class
        return [QuoteParser(e) for e in quote_tags] #quote parse for each element in quote tags
