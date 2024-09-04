import re
from locators.book_locators import BookLocators


class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self,parent):
        self.parent = parent
    
    def __repr__(self) -> str:
        return f'<Book {self.name}, price = {self.price}, {self.rating} stars.>'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator).attrs['title']
        return item_link
    
    @property
    def link(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link
    
    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_link = self.parent.select_one(locator).string # 65.22

        pattern = '£([0-9]+\.[0-9]+)'
        match = re.search(pattern, item_link)
        return float(match.group(1)) # 65.22
    
    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        item_link = self.parent.select_one(locator)
        classses = item_link.attrs['class'] # [star-rating, Three]
        rating_class = [r for r in classses if r != 'star-rating']
        rating = BookParser.RATINGS.get(rating_class[0])
        return rating