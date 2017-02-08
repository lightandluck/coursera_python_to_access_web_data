# Python 3
"""This will crawllinks"""
import urllib.request
from bs4 import BeautifulSoup

LINKPOS = 18
REPS = 7
URL = 'http://python-data.dr-chuck.net/known_by_Kinnon.html'

def crawllinks(url, linkpos, reps):
    """Will crawl"""
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    tags = soup('a')

    new_url = tags[linkpos - 1]['href']
    reps -= 1
    if reps > 0:
        return crawllinks(new_url, linkpos, reps)
    else:
        return tags[linkpos - 1].string

print(crawllinks(URL, LINKPOS, REPS))
