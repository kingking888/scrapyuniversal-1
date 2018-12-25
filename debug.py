import os
import sys
from scrapy.cmdline import execute

# 调试scrapy执行流程
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'anjuke'])
