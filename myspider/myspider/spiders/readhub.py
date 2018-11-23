# -*- coding: utf-8 -*-
'''
    scrapy crawl readhub
'''
import scrapy


class ReadhubSpider(scrapy.Spider):
    name = 'readhub'
    allowed_domains = ['readhub.cn/topics']
    start_urls = ['http://readhub.cn/topics/']

    def parse(self, response):
        res_select = response.xpath('//*[@id="itemList"]/div/h2/span/text()')
        # / div[1] / h2 / span / text()
        head_content = res_select.extract()
        # print("这是标题"+str(head_content))

        body_content = response.xpath('//*[@id="itemList"]/div/div[1]/div/text()').extract()
        print(type(body_content))
        for i in range(len(body_content)):
            print(body_content[i])
        pass
