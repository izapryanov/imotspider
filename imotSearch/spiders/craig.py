from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["google.com"]
    start_urls = ["https://www.google.com/search?client=ubuntu&channel=fs&q=%D0%B8%D0%BC%D0%BE%D1%82%D0%B8+%D1%81%D0%BE%D1%84%D0%B8%D1%8F+%D0%BA%D1%8A%D1%89%D0%B0+%D0%B4%D1%80%D0%B0%D0%B3%D0%B0%D0%BB%D0%B5%D0%B2%D1%86%D0%B8+&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=52QxWO3QO7DY8AfN46LgAw"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//p")
        for titles in titles:
            title = titles.select("a/text()").extract()
            link = titles.select("a/@href").extract()
            print title, link

