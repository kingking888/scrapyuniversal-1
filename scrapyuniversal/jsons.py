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
            }
}
