import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">

        <article class="product_pod">

                <div class="image_container">

                        <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
                </div>

                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>

                <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>

                <div class="product_price">

            <p class="price_color">£51.77</p>

    <p class="instock availability">
        <i class="icon-ok"></i>

            In stock
    </p>

        <form>
            <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
        </form>
                </div>
        </article>
    </li>
  </body>
</html>
'''

class ParsedItemLocators:

    '''
    Locators for an item in html page
    This allows us to see what our code will be looking at as well as change it
    quickly if we notice it is now different.
    '''

    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'



class ParsedItem:

    '''
    a class to take an HTML page or part of it and find properties in it.
    '''

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')


    def find_item_name(self):
        locator =   ParsedItemLocators.NAME_LOCATOR # CSS locator, location of what we want
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name


    def find_item_link(self):
        locator =  ParsedItemLocators.LINK_LOCATOR# CSS locator, location of what we want
        item_link = self.soup.select_one(locator).attrs['href']  # this is a relative link
        return item_link


    '''
    def find_item_price(self):
        # locator = 'article.product_pod p.price_color'
        # item_link = self.soup.select_one(locator)
        prod_price = soup.find('p', {'class': 'price_color'}).string
        return prod_price[1:]  # this extracts a strong not a number
    '''


    def find_item_price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return matcher.group(0)  # £51.77
        return float(matcher.group(1))  # 51.77


    def find_item_rating(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        star_rating_tag = soup.select_one(locator)
        # print(star_rating_tag)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        return rating_classes[0]

# ecapsulation
item = ParsedItem(ITEM_HTML)
print(item.find_item_link())
