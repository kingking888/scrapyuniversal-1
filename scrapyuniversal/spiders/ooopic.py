from scrapy import Request, Spider
from scrapyuniversal.items import OoopicItem
from scrapyuniversal.utils import get_config


# 我图网爬虫
class OoopicSpider(Spider):
    name = 'ooopic'

    def __init__(self, *name, **kwargs):
        super().__init__(self.name, **kwargs)
        config = get_config(self.name)
        self.allowed_domains = config.get('allowed_domains')
        self.start_urls = config.get('start_urls')
        self.config = config

    def parse(self, response):
        # 水平爬取
        pages = response.css('.page > a::attr(href)').extract()
        for page in pages:
            if "javascript:void(0)" not in page:
                yield Request(page, callback=self.parse)
        # 垂直爬取
        pics = response.css('#flow > div > a::attr(href)').extract()
        for pic in pics:
            yield Request(response.urljoin(pic), callback=self.parse_pic)

    def parse_pic(self, response):
        # 数据爬取
        pic_src = response.css('#pic_play::attr(src)').extract_first()
        ooopic_item = OoopicItem()
        ooopic_item['table'] = self.config.get('table')
        ooopic_item['page_url'] = response.url
        ooopic_item['pic_src'] = response.urljoin(pic_src)
        yield ooopic_item
