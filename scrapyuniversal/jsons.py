jsons = {
            "jia": {
                "spider": "jia",
                "website": "齐家网",
                "type": "家装",
                "table": "jia",
                "allowed_domains": ["jia.com"],
                "start_urls": ["https://www.jia.com/xiamen/"],
                "filter_urls": ["tuku", "luntan", "javascript"]
            },
            "anjuke": {
                "spider": "anjuke",
                "website": "安居客",
                "type": "租房",
                "table": "anjuke",
                "allowed_domains": ["anjuke.com"],
                "start_urls": ["https://www.anjuke.com/fz/cm/"],
                "filter_urls": [],
                "target_urls": ["/fz/", "/xm/", "/zhangzhou/", "/quanzhou/", "/sanming/", "/putian/", "/nanping/",
                                "/longyan/", "/ningde/"]
            },
            "ooopic": {
                "spider": "ooopic",
                "website": "我图网",
                "type": "素材",
                "table": "ooopic",
                "allowed_domains": ["ooopic.com"],
                "start_urls": ["http://www.ooopic.com/shineisucai/", "http://www.ooopic.com/zhuangshihua/"]
            },
            "taobao": {
                "spider": "taobao",
                "website": "淘宝网",
                "type": "电子商城",
                "table": "taobao",
                "allowed_domains": ["taobao.com"],
                "start_urls": ["https://www.taobao.com/"],
                "filter_urls": ["javascript"]
            },
            "jd": {
                "spider": "jd",
                "website": "京东商城",
                "type": "电子商城",
                "table": "jd",
                "allowed_domains": ["jd.com"],
                "start_urls": ["https://www.jd.com/"],
                "filter_urls": ["javascript"]
            },
            "tmall": {
                "spider": "tmall",
                "website": "天猫商城",
                "type": "电子商城",
                "table": "tmall",
                "allowed_domains": ["tmall.com"],
                "start_urls": ["https://www.tmall.com/"],
                "filter_urls": ["javascript"]
            },
            "alibaba": {
                "spider": "alibaba",
                "website": "阿里巴巴批发网",
                "type": "电子商城",
                "table": "alibaba",
                "allowed_domains": ["1688.com"],
                "start_urls": ["https://www.1688.com/"],
                "filter_urls": ["javascript"]
            },
            "tmkoo": {
                "spider": "tmkoo",
                "website": "标库网",
                "type": "商标",
                "table": "tmkoo",
                "allowed_domains": ["tmkoo.com"],
                "start_urls": ["http://www.tmkoo.com/tmtuxing.php"]
            }
}
