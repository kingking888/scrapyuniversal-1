import json
import time
import pymysql
import pymongo
from redis import StrictRedis


class TimePipeline:
    def process_item(self, item, spider):
        # if isinstance(item, ImageItem):
        #     if '.html' in item['img_src']:
        #         raise DropItem('wrong image')
        item['crawled_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return item


class MysqlPipeline:
    def __init__(self, mysql_host, mysql_database, mysql_user, mysql_password, mysql_port,
                 reids_host, reids_database, reids_password, reids_port):
        self.mysql_host = mysql_host
        self.mysql_database = mysql_database
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_port = mysql_port
        self.reids_host = reids_host
        self.reids_database = reids_database
        self.reids_password = reids_password
        self.reids_port = reids_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_database=crawler.settings.get('MYSQL_DATABASE'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_password=crawler.settings.get('MYSQL_PASSWORD'),
            mysql_port=crawler.settings.get('MYSQL_PORT'),
            reids_host=crawler.settings.get('REDIS_HOST'),
            reids_database=crawler.settings.get('REDIS_DATABASE'),
            reids_password=crawler.settings.get('REDIS_PASSWORD'),
            reids_port=crawler.settings.get('REDIS_PORT')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.mysql_host, self.mysql_user, self.mysql_password,
                                  self.mysql_database, charset='utf8', port=self.mysql_port)
        self.cursor = self.db.cursor()
        self.redis = StrictRedis(host=self.reids_host, port=self.reids_port,
                                 db=self.reids_database, password=self.reids_password)

    def close_spider(self, spider):
        self.db.close()

    # 先在redis缓存100条数据，后批量插入mysql
    # 不适用分布式爬虫
    def process_item(self, item, spider):
        if not self.redis.exists(item['table']):
            self.redis.rpush(item['table'], item)
            return item
        if self.redis.rpush(item['table'], item) >= 100:
            imgs = self.redis.lrange(item['table'], 0, self.redis.llen(item['table']))
            self.redis.delete(item['table'])
            for img in imgs:
                data = dict(json.loads(img.decode('utf-8').replace("\'", "\"")))
                data.pop('table')
                keys = ', '.join(data.keys())
                values = ', '.join(['%s'] * len(data))
                sql = 'insert into %s (%s) values (%s)' % (item['table'], keys, values)
                self.cursor.execute(sql, tuple(data.values()))
                self.db.commit()
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        item_dict = dict(item)
        item_dict.pop('table')
        collection = item['table']
        self.db[collection].insert(item_dict)
        return item

    def close_spider(self, spider):
        self.client.close()
