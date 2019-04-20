"用于处理找工作函数的排序算法"
from math import radians, cos, sin, asin, sqrt
from evaluation.models import Evaluation
from api.models import Shangjia

# 商家评价排序
def zineng(city):
    zidian = {}
    data = []
    # 筛选出本城市内所有的shangjia
    shangjia = Shangjia.objects.filter(city=city)
    for sj in shangjia:
        zidian[sj] = sj.score
    shangjia = sorted(zidian.items(), key=lambda x: x[1], reverse=True)
    for sj in shangjia:
        list1 = sj.recruitment_set.all()  # 找出商家所发布的招聘信息
        for i in list1:
            duixiang = {}
            duixiang['position'] = i.position
            duixiang['description'] = i.description
            duixiang['work_location'] = i.work_location
            duixiang['academic'] = i.academic
            duixiang['subject'] = i.subject
            duixiang['price'] = i.price
            duixiang['type'] = i.type
            duixiang['pub_time'] = i.pub_time
            duixiang['shangjia'] = sj.name
            data.append(duixiang)
    return duixiang

# 距离最近算法
def zuijin(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) # 将角度转换为弧度
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000 # 返回距离，单位为米


# 按照地区查找
def max_star(city):
    # 筛选出所在地区商家
    data = []
    shangjia = Shangjia.objects.filter(city=city)
    # 查找对应的招聘信息
    for sj in shangjia:
        list1 = sj.recruitment_set.all() # 找出商家所发布的招聘信息
        for i in list1:
            duixiang = {}
            duixiang['position'] = i.position
            duixiang['description'] = i.description
            duixiang['work_location'] = i.work_location
            duixiang['academic'] = i.academic
            duixiang['subject'] = i.subject
            duixiang['price'] = i.price
            duixiang['type'] = i.type
            duixiang['pub_time'] = i.pub_time
            duixiang['shangjia'] = sj.name
            data.append(duixiang)
    return duixiang

#用户自定义排序算法
def self_make():
    pass