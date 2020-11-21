import json
import re
from datetime import datetime
import feedparser

url = "https://www.ddproperty.com/rss/sale/N"
filename = './result/ddProperty/condo.json'


def write_json(data, filename=filename):
    print("Added Item " + str(added_element))
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


NewsFeed = feedparser.parse(url)
added_element = 0
entry = NewsFeed.entries[1]
# print(NewsFeed.entries[0])
print(entry.keys())
data = {'ddProperty': []}
with open(filename, mode='r', encoding='utf-8') as f:
    data_old = json.load(f)
    temp = data['ddProperty']
    # for item in data_old['ddProperty']:
    #     data['ddProperty'].append(item)

for item in NewsFeed.entries:
    title = item.title
    link = item.link
    description = item.description
    category = item.category
    pubDate = item.published
    pubDateParsed = item.published_parsed
    priceRE = re.search("฿\s([0-9]+,)*([0-9]*)", description)
    sizeInMeterRE = re.search("([0-9,]*.[0-9]* sqm)", description)
    if priceRE is not None:
        price = str(priceRE.group())
    else:
        price = "Undefined"
    if sizeInMeterRE is not None:
        sizeInMeter = str(sizeInMeterRE.group())
    else:
        sizeInMeter = "Undefined"
    # print("Title " + title)
    # print("Category " + category)
    # print("pubDate " + pubDate)
    # print("price " + price)
    # print("sizeInMeter " + sizeInMeter)
    # print("link " + link)
    if link not in data_old['ddProperty']:
        temp.append({
            'title': title,
            'category': category,
            'pubDate': pubDate,
            'price': price,
            'size': sizeInMeter,
            'link': link
        })
        ++added_element

write_json(data)
