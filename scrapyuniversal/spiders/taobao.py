from scrapy import Request, Spider
from scrapyuniversal.items import *
from scrapyuniversal.utils import get_config


# 淘宝网爬虫
class TaobaoSpider(Spider):
    name = 'taobao'

    def __init__(self, *name, **kwargs):
        super().__init__(self.name, **kwargs)
        config = get_config(self.name)
        self.allowed_domains = config.get('allowed_domains')
        self.start_urls = config.get('start_urls')
        self.config = config

    def parse(self, response):
        # 解析图片
        srcs = response.xpath('//img/@src').extract()
        for src in srcs:
            src = response.urljoin(src)
            # self.logger.debug('target_src:' + src)
            image_item = ImageItem()
            image_item['page_url'] = response.url
            image_item['img_src'] = src
            image_item['table'] = self.config.get('table')
            yield image_item
        # 生成新请求
        hrefs = response.xpath('//a/@href').extract()
        for href in hrefs:
            href = response.urljoin(href)
            # 过滤请求
            filter_urls = self.config.get('filter_urls')
            if filter_urls:
                for filter_url in filter_urls:
                    if filter_url in href:
                        href = None
                        break
            if href:
                # self.logger.debug('target_href:' + href)
                yield Request(href, callback=self.parse)
