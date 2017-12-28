-*- coding:utf-8 -*-
import scrapy

calss ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlou-github'

    def start_request(self):
        url_tmpl = 'https://github.com/shiyanlou?tab=repositories'
        urls = (url_tmpl.format(i) for i in range(1,5))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for name in response.css('div.d-inline-block mb-1'):
            yield {'name': name.css('div.d-inline-block mb-1/h3/a::attr(href)').re_first('/shiyanlou/ (.+) ')}
        for updatetime in response.css('div.f6 text-gray mt-2'):
            yield {'update_time': updatetime.css('div.f6 text-gray mt-2/
