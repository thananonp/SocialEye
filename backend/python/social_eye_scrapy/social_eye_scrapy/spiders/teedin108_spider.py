import datetime
import re
import time

import scrapy

from .convertDateToUnix import convertDateToUnix


class TeedinSpider(scrapy.Spider):
    name = "teedin108"

    def start_requests(self):
        url = 'https://www.teedin108.com/'
        province = getattr(self, 'province', None)
        amphur = getattr(self, 'amphur', None)
        if province is not None:
            print("province = " + province)
            url = url + 'search/province/' + province
            print(url)
        if amphur is not None:
            print("amphur = " + amphur)
            url = url + 'house/amphur/' + amphur
            print(url)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        now = int(time.mktime((datetime.datetime.now()).timetuple()))

        for container in response.css('div.container div.row div.col-sm-9 div.row div.postlist div.row'):
            cleaned_date = re.sub('[ \t]{2,}', '', container.css('div.postdate::text')[1].get())
            posted = convertDateToUnix(cleaned_date)
            if posted > 1605524360:
                print("yes")
                yield {
                    'name': re.sub('[ \t]{2,}', '', container.css('div.col-xs-12 a::text').get()),
                    'price': re.sub('[ \t]{2,}', '', container.css('div.priceinlist::text')[1].get()),
                    'link': container.css('div.col-xs-12 a::attr(href)').get(),
                    'posted': re.sub('[ \t]{2,}', '', container.css('div.postdate::text')[1].get()),
                    'queryAt': now
                }
