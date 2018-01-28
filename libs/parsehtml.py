import requests
from lxml import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

class base():
    def __init__(self,url):
        self.get_page(url)

    def get_page(self,url):
        html = urlopen(url)
        self.bsObj = BeautifulSoup(html, "html.parser")

if __name__ == '__main__':
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lovadeck.settings")
    url=

