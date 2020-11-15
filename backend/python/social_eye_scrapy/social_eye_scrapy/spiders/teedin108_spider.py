import scrapy
import re
import string


class QuotesSpider(scrapy.Spider):
    name = "teedin108"

    def start_requests(self):
        url = 'https://www.teedin108.com/'
        province = getattr(self, 'province', None)
        amphur = getattr(self, 'amphur', None)
        if amphur is not None:
            url = url + '/search/province/' + province
        if province is not None:
            url = url + '/house/amphur/' + province
        yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    # def parseinside(self, response):
    #     # for info in response.css('div.working-area div.row div.padding-right-10 div.row article'):
    #     for info in response.css('div.working-area div.row div.padding-right-10 div.row article'):
    #         yield {
    #             'info': re.sub('\s{2,}', '', "".join(info.css('div.description::text').getall())),
    #             'name': re.sub('\s{2,}', '', info.css('div.poster-detail::text').getall()[1]),
    #             'line': re.sub('\s{2,}', '', info.css('div.poster-detail::text').getall()[2]),
    #             'telephone': info.css('div.poster-detail a::text').getall()[0],
    #             'email': info.css('div.poster-detail a::text').getall()[1]
    #         }

    def parse(self, response):
        for container in response.css('div.container div.row div.col-sm-9 div.row div.col-xs-12 div.row'):
            # for row_a in container.css('div.row'):
            #     for colsm9 in row_a.css('div.col-sm-9'):
            #         for row_b in colsm9.css('div.row'):
            #             for colxs12 in row_b.css('div.col-xs-12'):
            #                 for row_c in colxs12.css('div.row'):
            yield {
                'name': container.css('div.col-xs-12 a::text').get(),
                'price': container.css('div.priceinlist::text')[1].get(),
                'link': container.css('div.col-xs-12 a::attr(href)').get(),
                'posted': container.css('div.postdate::text')[1].get()
            }
            # next_page = row_c.css(
            #     'div.col-xs-12 a::attr(href)').get()
            # print("following " + next_page)
            # if next_page is not None:
            #     yield response.follow(next_page, callback=self.parseinside)

    # def parseinside(self, response):
    #     for info in response.css('div.working-area div.row div.padding-right-10 div.row article'):
    #         yield {
    #             'info': info.css('div.poster-detail::text').getall()
    #         }

    # container = response.css('div.container')
    # row1 = container.css('div.row')
    # colsm9 = row1.css('div.col-sm-9')
    # row2 = colsm9.css('div.row')
    # colxs12 = row2.css('div.col-xs-12')
    # row3 = colxs12.css('div.row')
    # name = row3.css('div.col-xs-12 a::text').get()
    # price = row3.css('div.priceinlist::text').get()
    # link =  row3.css('div.col-xs-12 a::attr(href)').get()
    # print(dict(name=name, price = price,link = link))
