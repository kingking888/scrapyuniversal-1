from scrapy import Request, Spider
from scrapyuniversal.items import TrademarkItem
from scrapyuniversal.utils import get_config


# 标库网爬虫
class TmkooSpider(Spider):
    name = 'tmkoo'

    def __init__(self, *name, **kwargs):
        super().__init__(self.name, **kwargs)
        config = get_config(self.name)
        self.allowed_domains = config.get('allowed_domains')
        self.start_urls = config.get('start_urls')
        self.config = config

    def parse(self, response):
        # 获取类别
        categories = response.css('.fr > a::attr(href)').extract()
        for categorie in categories:
            yield Request(response.urljoin(categorie), callback=self.parse_trademark)

    def parse_trademark(self, response):
        trademarks = response.css('.tmPicMiddleD img::attr(alt)').extract()
        for trademark in trademarks:
            item = TrademarkItem()
            item['table'] = self.config.get('table')
            item['page_url'] = response.url
            item['category'] = response.css('.main > div:nth-child(2)::text').extract_first()
            item['trademark'] = trademark
            yield item
        # 翻页
        pages = response.css('.main > div:nth-child(4) > a::attr(href)').extract()
        for page in pages:
            yield Request(response.urljoin(page), callback=self.parse_trademark)
