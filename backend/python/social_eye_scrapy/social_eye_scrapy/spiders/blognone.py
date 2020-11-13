import scrapy
import re
import string


class QuotesSpider(scrapy.Spider):
    name = "blognone"

    def start_requests(self):
        urls = [
            'https://www.blognone.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parseinside(self, response):
        for info in response.css('div#wrapper div#content div#main-content div.region-content div#block-system-main div.content div div.content div.node-content div.field div.field-items div.even'):
            yield {
                'text': info.css('p::text').getall()
            }

    def parse(self, response):
        for container in response.css('div#wrapper div#content div#main-content div.content-container div.region-content div#block-system-main div.content div'):
            yield {
                'title': container.css('h2 a::text').getall(),
                'link': container.css('h2 a::attr(href)').getall()
            }
            # next_page = container.css('h2 a::attr(href)').get()
            # print("following " + next_page)
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield response.follow(next_page, callback=self.parseinside)
