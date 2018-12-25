import time
from scrapy import Request, Spider
from scrapyuniversal.items import AnjukeItem
from scrapyuniversal.utils import get_config


# 安居客爬虫
class AnjukeSpider(Spider):
    name = 'anjuke'

    def __init__(self, *name, **kwargs):
        super().__init__(self.name, **kwargs)
        config = get_config(self.name)
        self.allowed_domains = config.get('allowed_domains')
        self.start_urls = config.get('start_urls')
        self.config = config

    def parse(self, response):
        time.sleep(1)
        # 获取各小区大全入口
        collections = response.css('.P3')[1].css('a::attr(href)').extract() + response.css('.P3')[2].css('a::attr(href)').extract()
        for collection in collections:
            # for target_url in self.config.get('target_urls'):
            #     if target_url in collection:
            #         yield Request(collection, callback=self.parse_communities)
            yield Request(collection, callback=self.parse_communities)

    def parse_communities(self, response):
        time.sleep(1)
        # 翻页
        pages = response.css('.P4 a::attr(href)').extract()
        for page in pages:
            yield Request(page, callback=self.parse_communities)
        # 获取各小区详情入口
        communities = response.css('.P3')[0].css('a::attr(href)').extract()
        for community in communities:
            yield Request(community, callback=self.parse_community)

    def parse_community(self, response):
        time.sleep(1)
        # 获取当前小区详情
        anjuke_item = AnjukeItem()
        anjuke_item['table'] = self.config.get('table')
        anjuke_item['page_url'] = response.url
        anjuke_item['navigation'] = '>'.join(response.css('.cb-crumbs a::text').extract())
        anjuke_item['name'] = response.css('.infos-box h3::text').extract_first()
        anjuke_item['av_price'] = response.css('.price em::text').extract_first()
        span_texts = response.css('.basic-parms span::text').extract()
        for i in range(0, len(span_texts)):
            if i == 0:
                anjuke_item['plate'] = span_texts[i]
            elif i == 1:
                anjuke_item['total_households'] = span_texts[i]
            elif i == 2:
                anjuke_item['greening_rate'] = span_texts[i]
            elif i == 3:
                anjuke_item['parking_space'] = span_texts[i]
            elif i == 4:
                anjuke_item['property_type'] = span_texts[i]
            else:
                anjuke_item['completion_time'] = span_texts[i]
        yield anjuke_item
