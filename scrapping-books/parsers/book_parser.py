import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scrapping.book_parser')

class BookParser:

    '''
    a class to take an HTML page or part of it and find properties in it.
    '''
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent # parent is already a soup object

    def __repr__(self):
        return f'<Book {self.name}, {self.price} ({self.rating} stars)>'

    @property
    def name(self):
        logger.debug('Finding book name....')
        locator =   BookLocators.NAME_LOCATOR # CSS locator, location of what we want
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug('Found book name, `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding book link....')
        locator =  BookLocators.LINK_LOCATOR# CSS locator, location of what we want
        item_link = self.parent.select_one(locator).attrs['href']  # this is a relative link
        logger.debug('Found book link, `{item_link}`.')
        return item_link


    '''
    def find_item_price(self):
        # locator = 'article.product_pod p.price_color'
        # item_link = self.soup.select_one(locator)
        prod_price = soup.find('p', {'class': 'price_color'}).string
        return prod_price[1:]  # this extracts a strong not a number
    '''

    @property
    def price(self):
        logger.debug('Finding book price....')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        #return matcher.group(0)  # £51.77
        float_price = float(matcher.group(1))  # 51.77
        logger.debug('Found book price, `{float_price}`.')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating....')
        locator = BookLocators.PRICE_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        # print(star_rating_tag)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        #return rating_classes[0]

        rating_number = BookParser.RATINGS.get(rating_classes[0]) #none if not found
        logger.debug('Found book rating, `{rating_number}`.')
        return rating_number
