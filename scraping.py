import requests
from bs4 import BeautifulSoup

for i in range(1):
    source = requests.get('http://gacosbd.edu.in//').text

