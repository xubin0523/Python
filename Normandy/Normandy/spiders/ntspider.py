
import re
from scrapy.spider import Spider
from scrapy import Selector
from scrapy.http import Request
from Normandy.items import NormandyItem



class MySpideri(Spider):
    name = "Normandy"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://music.baidu.com"]
    def parse(self, response):
        hxs = Selector(response)
        links = hxs.xpath("//a/@href").extract()
        crawledLinks = []
        linkPattern = re.compile("^(?:ftp|http|https):\/\/(?:[\w\.\-\+] \
            *@)?(?:[a-z0-9\-\.]+)")
        for link in links:
            if linkPattern.match(link) and not link in crawledLinks:
                crawledLinks.append(link)
                yield Request(link, self.parse)

        titles = hxs.xpath('/html/head/title/text()').extract()
        for title in titles:
            item = NormandyItem()
            item["title"] = title
            yield item
