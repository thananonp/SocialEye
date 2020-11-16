import re

import feedparser

NewsFeed = feedparser.parse("https://www.ddproperty.com/rss")
entry = NewsFeed.entries[1]
print(entry.keys())
for i in NewsFeed:
    title = entry.title
    link = entry.link
    description = entry.description
    price = str(re.search("฿\s([0-9]+,)*([0-9]*)", description).group())
    sizeInMeter = str(re.search("([0-9,]*.[0-9]* sqm)",description).group())

