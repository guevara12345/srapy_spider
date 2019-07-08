from sqlalchemy.orm import sessionmaker
from models import db_connect, SaleInfo, RegionInfo
from sqlalchemy import and_, or_
import csv
import os
import time

from config import PROJ_PATH


def show_sale_info():
    engine = db_connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(SaleInfo, RegionInfo). \
        filter(and_(SaleInfo.region == RegionInfo.region,
                    SaleInfo.district == RegionInfo.district,
                    SaleInfo.house_usage == '普通住宅',
                    RegionInfo.is_too_far == 0,
                    SaleInfo.total_price >= '650',
                    SaleInfo.total_price <= '850',
                    SaleInfo.is_expire == 0)). \
        filter(or_(SaleInfo.district == '朝阳', SaleInfo.district == '海淀', SaleInfo.district == '丰台')). \
        order_by(SaleInfo.district).order_by(SaleInfo.region).order_by(SaleInfo.xiaoqu)
    l_r = query.all()
    l_t_r = [(sale.xiaoqu, sale.total_price, sale.unit_price, sale.district, sale.region, sale.build_area,
              sale.house_area, sale.room, sale.orientations, sale.guapai_time, sale.build_year, sale.price_change, sale.url)
             for sale, region in l_r]
    with open(os.path.join(PROJ_PATH, 'result/HouseInfo-{}.csv'.format(time.strftime("%Y%b%d-%H%M%S"))),
              'w', encoding='utf_8_sig', newline='') as f:
        f_csv = csv.writer(f, dialect='excel')
        f_csv.writerow(
            ['xiaoqu', 'total_price', 'unit_price', 'district', 'region', 'build_area', 'house_area', 'room',
             'orientations', 'guapai_time', 'build_year', 'price_change', 'url'])
        f_csv.writerows(l_t_r)


def test():
    engine = db_connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(SaleInfo).filter().update({SaleInfo.is_expire: 0})
    session.commit()


if __name__ == '__main__':
    show_sale_info()
    # test()
