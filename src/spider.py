import scrapy
from datetime import date
from scrapy.http import Response, Request


class SpiderSpider(scrapy.Spider):
    name = 'Spider'
    allowed_domains = ['https://notowania.pb.pl']
    start_urls = ['https://notowania.pb.pl/instrument/PBWALEUR/euro',
                  'https://notowania.pb.pl/instrument/PBWALUSD/dolar',
                  'https://notowania.pb.pl/instrument/PBWALEURUSD/eurusd']


    def parse(self, response):
        section = response.css('#pageMainContainer975')
        yield {
            'title': section.css('span.profilHead::text').get(),
            'value': section.css('div.profilLast::text').get(),
            'data': date.today()
        }
