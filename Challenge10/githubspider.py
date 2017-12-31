# -*- coding: utf-8 -*-
import scrapy

class GithubSpider(scrapy.Spider):
    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        url_tmp1 = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmp1.format(i) for i in range(1,5))

    def parse(self,response):
        for repository in response.css('li.public'):
            yield {
                    'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                    'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
                    }
