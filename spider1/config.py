import os
from typing import List

MAX_PRICE = 900
MIN_PRICE = 650
BUILD_AGE = {'0-5': 'y1', '0-10': 'y2', '0-15': 'y3', '0-20': 'y4', }
HOUSE_TYPE = {'1': 'l1', '2': 'l2', '3': 'l3', '4': 'l4'}
# BOUND = '{}{}bp{}ep{}'.format(BUILD_AGE['0-20'], HOUSE_TYPE['2'] + HOUSE_TYPE['3'], MIN_PRICE, MAX_PRICE)
BOUND = '{}bp{}ep{}'.format(HOUSE_TYPE['2'] + HOUSE_TYPE['3'], MIN_PRICE, MAX_PRICE)

SLEEP_TIME = 0
PROJ_PATH = '/home/wy/proj/spider1/spider1/'
PROCESS_NUM = 10

# 各区在售二手房爬取开始页面
l_sale_start_urls: List[str] = [
    'https://bj.ke.com/ershoufang/dongcheng/pg{}{}'.format(1, BOUND),
    'https://bj.ke.com/ershoufang/xicheng/pg{}{}'.format(1, BOUND),
    'https://bj.ke.com/ershoufang/chaoyang/pg{}{}'.format(1, BOUND),
    'https://bj.ke.com/ershoufang/haidian/pg{}{}'.format(1, BOUND),
    'https://bj.ke.com/ershoufang/fengtai/pg{}{}'.format(1, BOUND),
    # 'https://bj.ke.com/ershoufang/shijingshan/pg{}{}'.format(1, BOUND),
    # 'https://bj.ke.com/ershoufang/tongzhou/pg{}{}'.format(1, BOUND),
    'https://bj.ke.com/ershoufang/changping/pg{}{}'.format(1, BOUND)
]
# 各区下属区片名称爬取
dict_district_start_url = {
    u'东城': 'https://bj.ke.com/xiaoqu/dongcheng/',
    u'西城': 'https://bj.ke.com/xiaoqu/xicheng/',
    u'朝阳': 'https://bj.ke.com/xiaoqu/chaoyang/',
    u'海淀': 'https://bj.ke.com/xiaoqu/haidian/',
    u'丰台': 'https://bj.ke.com/xiaoqu/fengtai/',
    u'石景山': 'https://bj.ke.com/xiaoqu/shijingshan/',
    u'通州': 'https://bj.ke.com/xiaoqu/tongzhou/',
    u'昌平': 'https://bj.ke.com/xiaoqu/changping/'
}
# 各区历史成交二手房爬取
l_deal_start_urls = [
    # 'https://bj.ke.com/chengjiao/dongcheng/',
    # 'https://bj.ke.com/chengjiao/xicheng/',
    # 'https://bj.ke.com/chengjiao/chaoyang/',
    # 'https://bj.ke.com/chengjiao/haidian/',
    'https://bj.ke.com/chengjiao/fengtai/',
    # 'https://bj.ke.com/chengjiao/shijingshan/',
    # 'https://bj.ke.com/chengjiao/tongzhou/',
    # 'https://bj.ke.com/chengjiao/changping/'
]

far_region = [
    # 朝阳区
    '北工大', '百子湾', '成寿寺', '常营', 'CBD', '东坝', '大望路', '东大桥', '大山子', '豆各庄', '定福庄', '方庄',
    '垡头', '广渠门', '高碑店', '国展', '甘露园', '管庄', '欢乐谷', '华威桥', '酒仙桥', '劲松', '潘家园', '首都机场',
    '双井', '十里河', '十八里店', '双桥', '三里屯', '四惠', '通州北苑', '太阳宫', '甜水园', '西坝河', '燕莎',
    '中央别墅区', '朝阳其它',
    # 丰台区
    '丰台其它', '五里店', '刘家窑', '北大地', '十里河', '卢沟桥', '和义', '大红门', '七里庄',
    '太平桥', '宋家庄', '岳各庄', '广安门', '成寿寺', '新宫', '方庄', '旧宫', '木樨园', '洋桥', '玉泉营', '看丹桥', '科技园区',
    '花乡', '草桥', '菜户营', '蒲黄榆', '西红门', '西罗园', '角门', '赵公口', '青塔', '马家堡',
    #
]
