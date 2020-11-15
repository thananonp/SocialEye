import json
import scrapy
import re
# urls = []
# f = open('./result/teedin108_23.json', encoding='utf8')
# data = json.load(f)
# for i in data:
#     # print(i['link'])

#     urls.append(i['link'])
# f.close()
# print(urls)


class QuotesSpider(scrapy.Spider):
    name = "teedin108inside"

    def start_requests(self):
        urls = []
        f = open('./result/teedin108_23.json', encoding='utf8')
        data = json.load(f)
        for i in data:
            # print(i['link'])
            urls.append(i['link'])
        f.close()

        # tag = getattr(self, 'tag', None)
        # if tag is not None:
        #     url = url + tag

        # urls = ["https://www.teedin108.com/house/view/2286869/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseinside, cb_kwargs=dict(url=url))

    def parseinside(self, response, url):
        # for info in response.css('div.working-area div.row div.padding-right-10 div.row article'):
        for info in response.css('div.working-area div.row div.padding-right-10 div.row article'):
            yield {
                'url': url,
                'info': re.sub('\s{2,}', '', "".join(info.css('div.description::text').getall())),
                'name': re.sub('\s{2,}', '', info.css('div.poster-detail::text').getall()[1]),
                'line': re.sub('\s{2,}', '', info.css('div.poster-detail::text').getall()[2]),
                'telephone': info.css('div.poster-detail a::text').getall()[0],
                'email': info.css('div.poster-detail a::text').getall()[1]
            }
