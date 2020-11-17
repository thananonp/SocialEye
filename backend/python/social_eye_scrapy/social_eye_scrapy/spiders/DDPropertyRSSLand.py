import json
import re
import feedparser

url = "https://www.ddproperty.com/rss/sale/L"
NewsFeed = feedparser.parse(url)
entry = NewsFeed.entries[1]
# print(NewsFeed.entries[0])
print(entry.keys())
data = {'ddProperty': []}

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

    data['ddProperty'].append({
        'title': title,
        'category': category,
        'pubDate': pubDate,
        'price': price,
        'size': sizeInMeter,
        'link': link
    })

with open('./result/ddPropertyLand.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)
