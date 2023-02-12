# Crawler from:
# https://www.scrapingbee.com/blog/crawling-python/

import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

mainUrl = 'https://en.wikipedia.org/'

class Crawler:

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url, f):
        html = self.download_url(url)
        
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)
            if mainUrl in url:
                f.write(url + '\n')

    def run(self):
        f = open("demofileTEST.txt", "a")
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url, f)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
        f.close()

def main():
#    Crawler(urls=['https://www.imdb.com/']).run()
    Crawler(urls=[mainUrl]).run()

if __name__ == '__main__':
    main()
