# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseInfo(scrapy.Item):
    code = scrapy.Field()

    total_price = scrapy.Field()
    unit_price = scrapy.Field()

    room = scrapy.Field()
    floor = scrapy.Field()
    build_area = scrapy.Field()
    huxing = scrapy.Field()

    house_area = scrapy.Field()
    building_type = scrapy.Field()
    orientations = scrapy.Field()
    building_texture = scrapy.Field()

    decoration = scrapy.Field()
    elevator_house_proportion = scrapy.Field()
    heating = scrapy.Field()
    # is_elevator_exist = scrapy.Field()
    property_right = scrapy.Field()

    guapai_time = scrapy.Field()
    property_type = scrapy.Field()
    last_deal_time = scrapy.Field()
    house_usage = scrapy.Field()

    deal_year = scrapy.Field()
    property_ownership = scrapy.Field()
    mortgage = scrapy.Field()

    is_expire = scrapy.Field()

    xiaoqu = scrapy.Field()
    region = scrapy.Field()
    district = scrapy.Field()

    build_year = scrapy.Field()

    url = scrapy.Field()
    price_change = scrapy.Field()
