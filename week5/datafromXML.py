# Python 3
""" Extract data from xml """
import urllib.request
import xml.etree.ElementTree as ET

def get_count():
    """ Get the count """
    url = ' http://python-data.dr-chuck.net/comments_357523.xml '

    data = urllib.request.urlopen(url).read()
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    sum_of_counts = 0
    for count in counts:
        sum_of_counts += int(count.text)
    return sum_of_counts

print(get_count())


