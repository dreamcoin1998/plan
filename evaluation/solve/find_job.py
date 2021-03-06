"用于处理找工作函数的排序算法"
from math import radians, cos, sin, asin, sqrt
from evaluation.models import Evaluation
from api.models import Shangjia, Image
from django.contrib.contenttypes.models import ContentType
from order.models import Recruitment

# 结算方式
def pay_chinese(English):
    if English == 'Day':
        return '/天'
    elif English == 'Week':
        return '/周'
    elif English == 'Month':
        return '/月'
    elif English == 'Term':
        return '/学期'

# 查找商家对应的招聘信息
def get_xinxi(shangjia):
    data = []
    image = ContentType.objects.get_for_model(Recruitment)
    for sj in shangjia:
        print('对象：', sj)
        list1 = sj[0].recruitment_set.all()  # 找出商家所发布的招聘信息
        for i in list1:
            duixiang = {}
            duixiang['id'] = i.id
            duixiang['position'] = i.position
            duixiang['description'] = i.description
            duixiang['work_location'] = i.work_location
            duixiang['renshu'] = i.peo_num
            duixiang['academic'] = i.academic
            duixiang['subject'] = i.subject
            duixiang['price'] = str(i.price) + pay_chinese(i.pay_method)
            duixiang['type'] = i.type
            duixiang['pub_time'] = i.pub_time.strftime("%Y-%m-%d")
            duixiang['shangjia'] = sj[0].name
            duixiang['address'] = i.shangjia.province + i.shangjia.city + i.shangjia.location
            try:
                tupian = []
                tp_duixiang = Image.objects.filter(content_type=image, object_id=i.id)
                for i in tp_duixiang:
                    tupian.append(i.image.url)
                duixiang['image'] = tupian
            except:
                duixiang['image'] = ''
            data.append(duixiang)
    return data

# 商家评分排序
def pingfen(city):
    zidian = {}
    # 筛选出本城市内所有的shangjia
    shangjia = Shangjia.objects.filter(city=city)
    # 按照商家评分排序
    for sj in shangjia:
        zidian[sj] = sj.score
    shangjia = sorted(zidian.items(), key=lambda x: x[1], reverse=True)
    return get_xinxi(shangjia)

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
def chengshi(city):
    data = []
    image = ContentType.objects.get_for_model(Recruitment)
    # 筛选出所在地区商家
    shangjia = Shangjia.objects.filter(city=city)
    print(type(shangjia))
    # 查找对应的招聘信息
    for sj in shangjia:
        print('对象：', sj)
        list1 = sj.recruitment_set.all()  # 找出商家所发布的招聘信息
        for i in list1:
            duixiang = {}
            duixiang['id'] = i.id
            duixiang['position'] = i.position
            duixiang['description'] = i.description
            duixiang['work_location'] = i.work_location
            duixiang['renshu'] = i.peo_num
            duixiang['academic'] = i.academic
            duixiang['subject'] = i.subject
            duixiang['price'] = str(i.price) + pay_chinese(i.pay_method)
            duixiang['type'] = i.type
            duixiang['pub_time'] = i.pub_time.strftime("%Y-%m-%d")
            duixiang['shangjia'] = sj.name
            duixiang['address'] = i.shangjia.province + i.shangjia.city + i.shangjia.location
            try:
                tupian = []
                tp_duixiang = Image.objects.filter(content_type=image, object_id=i.id)
                for i in tp_duixiang:
                    tupian.append(i.image.url)
                duixiang['image'] = tupian
            except:
                duixiang['image'] = ''
            data.append(duixiang)
    print(data)
    return data

#用户自定义排序算法
def self_make():
    pass