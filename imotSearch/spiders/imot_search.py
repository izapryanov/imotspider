from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from imotSearch.items import ImotSearchItem
import sys
import logging


class MySpider(BaseSpider):
    name = "imot_search"
    allowed_domains = ["www.google.com"]
    start_urls = ["https://www.google.com/search?client=ubuntu&channel=fs&q=%D0%B8%D0%BC%D0%BE%D1%82%D0%B8+%D1%81%D0%BE%D1%84%D0%B8%D1%8F+%D0%BA%D1%8A%D1%89%D0%B0+%D0%B4%D1%80%D0%B0%D0%B3%D0%B0%D0%BB%D0%B5%D0%B2%D1%86%D0%B8+&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=52QxWO3QO7DY8AfN46LgAw"]
    logging.basicConfig(filename='imot.log',level=logging.DEBUG)
    def parse(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//h3")
        items = []
        for element in titles:
            item = ImotSearchItem()
            titles = element.select("a/text()").extract()
            logging.debug("Titles: " + ",".join(titles))
            t = ''.join(titles)
            title = t
            item["title"] = title
            item["link"] = element.select("a/@href").extract()
            items.append(item)
        return items
