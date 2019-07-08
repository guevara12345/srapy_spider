import scrapy
from urllib.parse import urljoin
from scrapy.spiders import Spider

from spider1.config import l_sale_start_urls
from spider1.log import logger
from spider1.items import HouseInfo

from sqlalchemy.orm import sessionmaker
from spider1.models import db_connect, SaleInfo
import traceback
import re



class GetHouseUrlSpider(Spider):
    name = 'LianjiaHouseUrlSprider'
    # allowed_domains = ['bj.ke.com']
    # start_urls = l_sale_start_urls

    def start_requests(self):
        self.clear_table()
        for url in l_sale_start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        list_urls = response.xpath(
            r"//div[@class='leftContent']//ul[@class='sellListContent']"
            r"//li[@class='clear']//div[@class='title']/a/@href").extract()
        url_list_page_total = \
            int(response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").re(r':(\d+)')[0])
        url_list_page_current = \
            int(response.xpath("//div[@class='page-box house-lst-page-box']/@page-data").re(r':(\d+)')[1])
        format_url_for_page_need_todo = \
            response.xpath("//div[@class='page-box house-lst-page-box']/@page-url").extract_first()

        if url_list_page_current < url_list_page_total:
            url_for_page_need_todo = urljoin(
                'https://bj.ke.com/', format_url_for_page_need_todo.format(page=url_list_page_current + 1))
            logger.info('format_url_for_page_need_todo={}'.format(format_url_for_page_need_todo))
            yield scrapy.Request(url_for_page_need_todo, callback=self.parse)

        for url in list_urls:
            logger.info('forward_url={}, from_url = {}'.format(url, response.url))
            yield scrapy.Request(url, callback=self.parse_house_info)

    def parse_house_info(self, response):
        try:
            info = HouseInfo()
            info['code'] = re.match('https://bj.ke.com/ershoufang/(\d+)\.html', response.url).group(1)
            if response.xpath(r"//div[@class ='title-wrapper']//h1/span"):
                info['is_expire'] = 1
            else:
                info['is_expire'] = 0
            info['total_price'] = response.xpath(
                r"//div[@class='overview']//div[@class='price ']//span[@class='total']/text()"). \
                get(default='not-found').strip()
            info['unit_price'] = response.xpath(
                r"//div[@class='overview']//div[@class='price ']//span[@class='unitPriceValue']/text()"). \
                get(default='not-found').strip()

            info['room'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='房屋户型']/text()"). \
                get(default='not-found').strip()
            info['floor'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='所在楼层']/text()"). \
                get(default='not-found').strip()
            info['build_area'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='建筑面积']/text()"). \
                get(default='not-found').strip()
            info['huxing'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='户型结构']/text()"). \
                get(default='not-found').strip()
            info['house_area'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='套内面积']/text()"). \
                get(default='not-found').strip()
            info['building_type'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='建筑类型']/text()"). \
                get(default='not-found').strip()
            info['orientations'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='房屋朝向']/text()"). \
                get(default='not-found').strip()
            info['building_texture'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='建筑结构']/text()"). \
                get(default='not-found').strip()
            info['decoration'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='装修情况']/text()"). \
                get(default='not-found').strip()
            info['elevator_house_proportion'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='梯户比例']/text()"). \
                get(default='not-found').strip()
            info['heating'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='供暖方式']/text()"). \
                get(default='not-found').strip()
            # r.is_elevator_exist'] = response.xpath(
            #     r"//div[@class='introContent']//div[@class='base']//li[12]/text()").
            #     get(default='not-found').strip()
            info['property_right'] = response.xpath(
                r"//div[@class='introContent']//div[@class='base']//li[span='产权年限']/text()"). \
                get(default='not-found').strip()
            #####################################################################################
            info['guapai_time'] = response.xpath(
                r"//div[@class='introContent']//div[@class='transaction']//li[span='挂牌时间']/text()"). \
                get(default='not-found').strip()
            info['property_type'] = response.xpath(
                r"//div[@class='introContent']//div[@class='transaction']//li[span='交易权属']/text()"). \
                get(default='not-found').strip()
            info['last_deal_time'] = response.xpath(
                r"//div[@class='introContent']//div[@class='transaction']//li[span='上次交易']/text()"). \
                get(default='not-found').strip()
            info['house_usage'] = response.xpath(
                r"//div[@class='introContent']//div[@class='transaction']//li[span='房屋用途']/text()"). \
                get(default='not-found').strip()
            info['deal_year'] = response.xpath(
                r"//div[@class='introContent']//div[@class='transaction']//li[span='房屋年限']/text()"). \
                get(default='not-found').strip()
            info['property_ownership'] = response.xpath(
                r"//div[@class='introContent']//div[@class='transaction']//li[span='产权所属']/text()"). \
                get(default='not-found').strip()
            info['mortgage'] = response.xpath(
                r"//div[@class='introContent']//div[@class='transaction']//li[span='抵押信息']/text()"). \
                get(default='not-found').strip()

            info['xiaoqu'] = response.xpath(
                r"//div[@class='overview']//div[@class='aroundInfo']/div[@class='communityName']/a[1]/text()"). \
                get(default='not-found').strip()
            info['region'] = response.xpath(
                r"//div[@class='overview']//div[@class='aroundInfo']/div[@class='areaName']//a[2]/text()"). \
                get(default='not-found').strip()
            info['district'] = response.xpath(
                r"//div[@class='overview']//div[@class='aroundInfo']/div[@class='areaName']//a[1]/text()").\
                get(default='not-found').strip()
            #####################################################################################
            info['build_year'] = response.xpath(
                r"//div[@class='houseInfo']/div[@class='area']/div[@class='subInfo']/text()").\
                re_first(r"(\d{4})", default='not-found')
            #####################################################################################
            info['url'] = response.url
            info['price_change'] = 0
            yield info
        except Exception as e:
            print(e)
            logger.exception(response.url)

    def clear_table(self):
        try:
            engine = db_connect()
            Session = sessionmaker(bind=engine)
            session = Session()
            session.query(SaleInfo).filter().update({SaleInfo.is_expire: 1})
            session.commit()
            logger.info('clear done')
        except Exception as e:
            session.rollback()
            logger.error(e)
            logger.exception()
        finally:
            session.close()
