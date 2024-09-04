from page.all_books_page import AllBookPage
import requests
import logging
import asyncio
import aiohttp
import async_timeout
import time


logging.basicConfig(format  =   '%(asctime)s %(levelname)-8s '
                        '%(filename)s:%(lineno)d] %(message)s',
                     datefmt= '$d-%m-%y %H:%M:%S',
                     level=logging.DEBUG,
                     filename ='app.log'
                     )

logger = logging.getLogger('scraping')

loop = asyncio.get_event_loop()

logging.info('Loading books...')
page_content = requests.get('https://books.toscrape.com').content

page = AllBookPage(page_content)

books = page.books

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Pagte took{time.time() - page_start}')
            return await response.text()
        

async def get_multi_page(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop= loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        group_tasks = asyncio.gather(*tasks)
        return await group_tasks


urls = [f'https://books.toscrape.com/catalogue/page-{page_numb}.html'
                         for page_numb in range(1,page.page_count)]

start = time.time()
pages = loop.run_until_complete(get_multi_page(loop, *urls))
print(f'Total pages requests took {time.time() - start}')

for page_content in pages:
    logger.debug('Creating AllBooks page from page content.')
    page = AllBookPage(page_content)
    books.extend(page.books)


    
