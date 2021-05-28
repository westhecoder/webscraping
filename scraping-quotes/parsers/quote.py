from locators.quote_locators import QuoteLocators

class QuoteParser:
    '''
    Given one of the specific quote divs, find the data
    about the quote(content, author, tags)

    get some tag and find quote data from within that tag
    '''

    def __init__(self, parent):
        self.parent = parent #BeautifulSoup tag, the div

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

        #under those divs we are searching the following 
    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        #return self.parent.select(locator)
        return [e.string for e in self.parent.select(locator)]
