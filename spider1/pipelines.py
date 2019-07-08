# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from spider1.models import db_connect, SaleInfo
from spider1.log import logger
import traceback


class GetHouseUrlSpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if spider.name == 'LianjiaHouseUrlSprider':
            session = self.Session()
            si = SaleInfo()
            si.code = item['code']

            si.total_price = item['total_price']
            si.unit_price = item['unit_price']

            si.room = item['room']
            si.floor = item['floor']
            si.build_area = item['build_area']
            si.huxing = item['huxing']

            si.house_area = item['house_area']
            si.building_type = item['building_type']
            si.orientations = item['orientations']
            si.building_texture = item['building_texture']

            si.decoration = item['decoration']
            si.elevator_house_proportion = item['elevator_house_proportion']
            si.heating = item['heating']
            # si.is_elevator_exist = item['is_elevator_exist']
            si.property_right = item['property_right']

            si.guapai_time = item['guapai_time']
            si.property_type = item['property_type']
            si.last_deal_time = item['last_deal_time']
            si.house_usage = item['house_usage']

            si.deal_year = item['deal_year']
            si.property_ownership = item['property_ownership']
            si.mortgage = item['mortgage']

            si.is_expire = item['is_expire']

            si.xiaoqu = item['xiaoqu']
            si.region = item['region']
            si.district = item['district']

            si.build_year = item['build_year']

            si.url = item['url']
            # si.price_change = item['price_change']
            try:
                if si.is_expire is 0:
                    l_stored_data = session.query(SaleInfo).filter(SaleInfo.code == si.code).all()
                    if l_stored_data:
                        price_change = float(si.total_price) - float(l_stored_data[0].total_price)
                        if price_change != 0:
                            si.price_change = str(price_change)
                    session.merge(si)
                else:
                    session.query(SaleInfo).filter(SaleInfo.code == si.code).update({SaleInfo.is_expire: 1})
                session.commit()
                logger.info('persist house info data code={}'.format(si.code))
            except:
                session.rollback()
                logger.error(traceback.print_exc())
            finally:
                session.close()
        return item
