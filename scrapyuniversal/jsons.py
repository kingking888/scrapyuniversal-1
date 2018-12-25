jsons = {
            "jia": {
                "spider": "jia",
                "website": "齐家网",
                "type": "家装",
                "table": "jia",
                "settings": {
                    "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
                },
                "allowed_domains": ["jia.com"],
                "start_urls": ["https://www.jia.com/xiamen/"],
                "filter_urls": ["tuku", "luntan", "javascript"]
            },
            "anjuke": {
                "spider": "anjuke",
                "website": "安居客",
                "type": "租房",
                "table": "anjuke",
                "settings": {
                    "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
                },
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
                "settings": {
                    "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
                },
                "allowed_domains": ["ooopic.com"],
                "start_urls": ["http://www.ooopic.com/shineisucai/", "http://www.ooopic.com/zhuangshihua/"]
            }
}
