import scrapy
from scrapy import Selector

class QuotesSpider(scrapy.Spider):
    name = "teedin108"

    def start_requests(self):
        urls = [
            'https://www.teedin108.com/house/amphur/43/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    def parse(self, response):
        for container in response.css('div.container'):
                for row_a in container.css('div.row'):
                    for colsm9 in row_a.css('div.col-sm-9'):
                        for row_b in colsm9.css('div.row'):
                            for colxs12 in row_b.css('div.col-xs-12'):
                                for row_c in colxs12.css('div.row'):
                                    yield{
                                      'name': row_c.css('div.col-xs-12 a::text').get(),
                                      'price': row_c.css('div.priceinlist::text')[1].get(),
                                      'link': row_c.css('div.col-xs-12 a::attr(href)').get()
                                    }
                                    next_page = row_c.css('div.col-xs-12 a::attr(href)').get()
                                    print("following " + next_page)
                                    if next_page is not None:
                                        yield response.follow(next_page, callback=self.parseinside)

        
        
    def parseinside(self, response):
        for info in response.css('div.working-area div.row div.padding-right-10 div.row article'):
            yield {
                'info': info.css('div.poster-detail::text').getall()
            }

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
