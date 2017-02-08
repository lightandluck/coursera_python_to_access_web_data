# import urllib
# from BeautifulSoup import *

# Python 2 code
# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()

# soup = BeautifulSoup(html)

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print 'TAG:',tag
#     print 'URL:',tag.get('href', None)
#     print 'Contents:',tag.contents[0]
#     print 'Attrs:',tag.attrs

# Python 3
import urllib.request
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_357526.html'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'lxml')
tags = soup('span')

sum = 0
print(f"Tags: {len(tags)}")
for tag in tags:
  sum += int(tag.string)
print(f"Sum: {sum}") 






