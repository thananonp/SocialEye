import json
import re

import scrapy


class TeedinInsideSpider(scrapy.Spider):
    name = "teedin108inside"

    def start_requests(self):
        province = getattr(self, 'province', None)
        amphur = getattr(self, 'amphur', None)
        if province is not None:
            print("province = " + province)
        if amphur is not None:
            print("amphur = " + amphur)
        urls = []
        path = './result/teedin108/province_' + province + '.json'
        f = open(path, encoding='utf8')
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
                'link': url,
                'name': info.css('div.poster-detail a::text').getall()[0],
                'line': re.sub('\s{2,}', '', info.css('div.poster-detail::text').getall()[1]),
                'mail': re.sub('\s{2,}', '', info.css('div.poster-detail a::text').getall()[2]),
                'telephone': info.css('div.poster-detail a::text').getall()[1],
                'info': re.sub('\s{2,}', '', "".join(info.css('div.description::text').getall()))
            }
