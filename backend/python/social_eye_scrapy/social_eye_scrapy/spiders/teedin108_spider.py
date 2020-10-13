import scrapy


class QuotesSpider(scrapy.Spider):
    name = "teedin108"

    def start_requests(self):
        urls = [
            'https://www.teedin108.com/house/amphur/42/'
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
                                      'colxs12a': row_c.css('div.col-xs-12 a::text').getall()
                                    }
            # yield {
            #     'row_a': container.css('div.row'),
            #     'colsm9': row_a.css('div.col-sm-9'),
            #     'row_b': colsm9.css('div.row'),
            #     'colxs12': row_b.css('div.col-xs-12'),
            #     'row_c': colxs12.css('div.row'),
            #     'colxs12a' : row_c.css('div.col-xs-12 a::text').getall()
            # }

# container = response.css('div.container')
# row1 = container.css('div.row')
# colsm9 = row1.css('div.col-sm-9')
# row2 = colsm9.css('div.row')
# colxs12 = row2.css('div.col-xs-12')
# row3 = colxs12.css('div.row')
# colxs12a = row3.css('div.col-xs-12 a::text')[1].get()
# print(dict(text=colxs12a))
