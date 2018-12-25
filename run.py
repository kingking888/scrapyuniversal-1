import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.spiders.jia import JiaSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess


# 读取配置，启动爬虫
def run():
    # debug
    # name = 'jia'
    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get('spider', 'jia')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()


# 运行入口，命令如：python run.py jia
if __name__ == '__main__':
    run()
