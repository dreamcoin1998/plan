from django.views import View
from utils.response import CommonResponseMixin, ReturnCode
from django.http import JsonResponse

SHANGJIA = [{
    "name": "博思特Beast托教中心",
    "star": 4,
    "address": "湖南省衡阳市蒸湘区",
    "distance": "1.98Km",
    "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/bosite.jpg",
    "tuoguan":[
        {
            "checked": False,
            "date": "2019.02.19",
            "eatcost": 264,
            "hot": False,
            "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/bosite.jpg",
            "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
            "name": "2019第一学期午托班",
            "pay": 500,
            "renshu": 15,
            "shangjia": "博思特Beast托教中心",
            "student": "小小班，小班，中班，大班，，学前班，一年级，二年级，三年级，四年级，五年级，六年级，初一，初二，初三，高一，高二，高三",
            "type": "【午托】",
            'value': 0
        },
        {
            "checked": False,
            "date": "2019.02.19",
            "eatcost": 264,
            "hot": False,
            "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/bosite.jpg",
            "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
            "name": "2019第一学期晚托班",
            "pay": 1000,
            "renshu": 15,
            "shangjia": "博思特Beast托教中心",
            "student": "小小班，小班，中班，大班，学前班，一年级，二年级，三年级，四年级，五年级，六年级，初一，初二，初三，高一，高二，高三",
            "type": "【晚托】",
            'value': 1
        },
    ],
    "describe": "博思特Beast托教中心"
    },
    {
        "name": "佳音托教中心",
        "star": 5,
        "address": "湖南省衡阳市蒸湘区",
        "distance": "0.98Km",
        "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/jiayin.jpg",
        "tuoguan": [
            {
                "checked": False,
                "date": "2019.02.19",
                "eatcost": 264,
                "hot": False,
                "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/jiayin.jpg",
                "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
                "name": "2019第一学期午托班",
                "pay": 500,
                "renshu": 15,
                "shangjia": "佳音托教中心",
                "student": "0~2岁，小小班，小班，中班，大班，学前班，一年级，二年级，三年级，四年级，五年级，六年级",
                "type": "【午托】",
                'value': 0
            },
            {
                "checked": False,
                "date": "2019.02.19",
                "eatcost": 264,
                "hot": False,
                "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/jiayin.jpg",
                "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
                "name": "2019第一学期晚托班",
                "pay": 1000,
                "renshu": 15,
                "shangjia": "佳音托教中心",
                "student": "0~2岁，小小班，小班，中班，大班，学前班，一年级，二年级，三年级，四年级，五年级，六年级",
                "type": "【晚托】",
                'value': 1
            },
        ],
        "describe": "下午接放学+完成+作业辅导 佳音托教中心于2015年创办，优越的师资力量，周到的细节服务，妥贴的心灵关怀，让学生在旅途中每走一步，都感受到焦点感的愉悦。每学期，让我们都能创造出若干个孩子快速进步的神话。欢迎关注我们，期待加入我们。"
    },
    {
        "name": "向日葵托管中心",
        "star": 5,
        "address": "湖南省衡阳市蒸湘区",
        "distance": "1.47Km",
        "imagePath": "https://api.gaoblog.cn/api/v1.0/server/image?md5=xiangrikui",
        "tuoguan": [
            {
                "checked": False,
                "date": "2019.02.19",
                "eatcost": 280,
                "hot": False,
                "imagePath": "https://api.gaoblog.cn/api/v1.0/server/image?md5=xiangrikui",
                "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
                "name": "2019第一学期午托班",
                "pay": 750,
                "renshu": 20,
                "shangjia": "向日葵托管中心",
                "student": "0~2岁，小小班，小班，中班，大班，学前班，一年级，二年级，三年级，四年级，五年级，六年级",
                "type": "【午托】",
                'value': 0
            },
            {
                "checked": False,
                "date": "2019.02.19",
                "eatcost": 280,
                "hot": False,
                "imagePath": "https://api.gaoblog.cn/api/v1.0/server/image?md5=xiangrikui",
                "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
                "name": "2019第一学期晚托班",
                "pay": 1750,
                "renshu": 20,
                "shangjia": "向日葵托管中心",
                "student": "0~2岁，小小班，小班，中班，大班，学前班，一年级，二年级，三年级，四年级，五年级，六年级",
                "type": "【晚托】",
                'value': 1
            },
        ],
        "describe": "下午接放学+完成+作业辅导 向日葵托管中心中心于2015年创办，优越的师资力量，周到的细节服务，妥贴的心灵关怀，让学生在旅途中每走一步，都感受到焦点感的愉悦。每学期，让我们都能创造出若干个孩子快速进步的神话。欢迎关注我们，期待加入我们。"
    }
]

SHOUYE_SHANGJIA = {
        "name": "佳音托教中心",
        "star": 5,
        "address": "湖南省衡阳市蒸湘区",
        "distance": "0.98Km",
        "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/jiayin.jpg",
        "tuoguan": [
            {
                "checked": False,
                "date": "2019.02.19",
                "eatcost": 264,
                "hot": False,
                "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/jiayin.jpg",
                "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
                "name": "2019第一学期午托班",
                "pay": 500,
                "renshu": 15,
                "shangjia": "佳音托教中心",
                "student": "一年级，二年级，三年级，四年级，五年级，六年级",
                "type": "【午托】",
                'value': 0
            },
            {
                "checked": False,
                "date": "2019.02.19",
                "eatcost": 264,
                "hot": False,
                "imagePath": "https://api.gaoblog.cn/api/v1.0/server/job?md5=photos/2019/05/12/jiayin.jpg",
                "kecheng": "https://api.gaoblog.cn/api/v1.0/server/image?md5=kecheng",
                "name": "2019第一学期晚托班",
                "pay": 1000,
                "renshu": 15,
                "shangjia": "佳音托教中心",
                "student": "一年级，二年级，三年级，四年级，五年级，六年级",
                "type": "【晚托】",
                'value': 1
            },
        ],
        "describe": "下午接放学+完成+作业辅导 佳音托教中心于2015年创办，优越的师资力量，周到的细节服务，妥贴的心灵关怀，让学生在旅途中每走一步，都感受到焦点感的愉悦。每学期，让我们都能创造出若干个孩子快速进步的神话。欢迎关注我们，期待加入我们。"
    }


# 获取托管机构实例
class Tuoguan(View, CommonResponseMixin):
    def get(self, requesrt):
        date = self.wrap_json_response(data=SHANGJIA, code=ReturnCode.SUCCESS, message="shangjia data success.")
        return JsonResponse(data=date, safe=False)

    def post(self, request):
        date = self.wrap_json_response(data=SHANGJIA, code=ReturnCode.SUCCESS, message="shangjia data success.")
        return JsonResponse(data=date, safe=False)


# 首页获取托管机构资料
class Tuoguan_shouye(View, CommonResponseMixin):
    def get(self, request):
        data = self.wrap_json_response(data=SHOUYE_SHANGJIA, code=ReturnCode.SUCCESS, message="homepage shangjia success.")
        return JsonResponse(data=data, safe=False)
