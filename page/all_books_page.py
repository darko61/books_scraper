import re
from bs4 import BeautifulSoup
from locators.all_book_page import AllBooksPageLocator
from parsers.book_parser import BookParser

class AllBookPage:
    
    def __init__(self,page_content) -> None:
        self.soup = BeautifulSoup(page_content, 'html.parser')
    
    @property
    def books(self):
        return [BookParser(e)for e in self.soup.select(AllBooksPageLocator.BOOKS)]
    
    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocator.PAGE).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages
