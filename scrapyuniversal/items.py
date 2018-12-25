from scrapy import Field, Item

class ImageItem(Item):
    table = Field()
    page_url = Field()
    img_src = Field()
    crawled_at = Field()

class AnjukeItem(Item):
    table = Field()
    page_url = Field()
    crawled_at = Field()
    navigation = Field()
    name = Field()
    av_price = Field()
    plate = Field()
    total_households = Field()
    greening_rate = Field()
    parking_space = Field()
    property_type = Field()
    completion_time = Field()


class OoopicItem(Item):
    table = Field()
    page_url = Field()
    crawled_at = Field()
    pic_src = Field()
