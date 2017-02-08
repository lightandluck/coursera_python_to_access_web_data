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
    index = linkpos - 1

    new_url = tags[index]['href']
    reps -= 1
    return crawllinks(new_url, linkpos, reps) if (reps > 0) else tags[index].string

print(crawllinks(URL, LINKPOS, REPS))
