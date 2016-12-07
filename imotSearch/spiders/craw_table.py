from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from imotSearch.items import ImotSearchItem
import sys
import logging


class MySpider(BaseSpider):
    name = "crawl_table"
    allowed_domains = ["www.sofia.holmes.bg"]
    start_urls = ["http://sofia.holmes.bg/pcgi/home.cgi?act=5&f1=0&f2=1&f3=10&f4=%E3%F0%E0%E4%20%D1%EE%F4%E8%FF&f5=%C4%F0%E0%E3%E0%EB%E5%E2%F6%E8"]
    logging.basicConfig(filename='crawlTable.log',level=logging.DEBUG)

    def parse(self, response):
        reload(sys)

        hxs = HtmlXPathSelector(response)
        items = hxs.xpath('//table[@width="956"]')
        logging.debug("Items: " + str(len(items)))
        result = []
        for element in items:
            item = ImotSearchItem()
            title = element.xpath('.//text()').extract()
            logging.debug("Title: " + "".join(title))
            item["title"] = title
            result.append(item)
        return result
