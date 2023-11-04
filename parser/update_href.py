import requests
from bs4 import BeautifulSoup as bs
from parser.href_groups import all_groups


def all_groups_update():

    url_groups = 'http://raspisanie.nnst.ru/public/www/cg.htm'

    response = requests.get(url_groups)
    soup = bs(response.text, 'html.parser')
    groups = soup.find_all('a', class_='z0')

    for group in groups:
        all_groups[group.text] = group.get('href')
