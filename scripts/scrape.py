import requests
import os
from bs4 import BeautifulSoup

BASE = 'http://shakespeare.mit.edu/Poetry/'
SONNETS = BASE + 'sonnets.html'

def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    links = []

    for h in soup.select('dt a'):
        href = h['href']
        links.append(BASE + href)

    return links

def get_titles():
    res = requests.get(SONNETS)
    soup = BeautifulSoup(res.text, 'lxml')
    links = {}

    for h in soup.select('dt a'):
        href = BASE + h['href']
        txt = get_sonnet(href)
        links[h.text.split('.')[0]] = txt

    return links


def get_sonnet(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    for h in soup.select('blockquote'):
        return h.text

def get_sonnets():
    links = get_links(SONNETS)
    sonnets = []
    for link in links:
        sonnets.append(get_sonnet(link))

    return sonnets

def get_sonnets_from_files():
    sonnets = []
    base = os.path.abspath('sonnets')
    for path in os.listdir(base):
        full_path = os.path.abspath(base + '/' + path)
        with open(full_path, 'r') as f:
            sonnets.append(f.read())

    return sonnets
