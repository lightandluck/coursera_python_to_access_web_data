# getJson
import json
import urllib.request

def get_json():
    url = 'http://python-data.dr-chuck.net/comments_357527.json'
    data = urllib.request.urlopen(url).read()

    parsed_items = json.loads(data)

    comments = parsed_items['comments']
    counts = 0
    for item in comments:
        counts += int(item['count'])
    return counts

print(get_json())
