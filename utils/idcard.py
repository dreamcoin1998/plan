import requests
import hmac
import hashlib
import base64
import time
import random
from plan.settings import IMAGES_DIR


# 身份证照片识别
def Know_Idcard(image_list=[], face=0):
    # 信息
    # appid
    appid = '1258554384'
    # 秘密ID
    SecretID = "AKIDCGPL5mIvTr472jIksmQr30iFXeYIIEKA"
    # 秘密key
    SecretKey = 'kEYbWFk00mIfokRzHK6d083j9TXUDl37'
    # 签名的有效期
    expiredTime = time.time() + 2592000
    # 当前时间戳
    currentTime = time.time()
    # 随机串
    rand = ''.join(random.choice('0123456789') for i in range(10))

    # 拼接多次有效签名串
    info = "a=" + appid + '&k=' + SecretID + '&e=' + str(expiredTime) + '&t=' + str(currentTime) + '&r=' + rand

    signindex = hmac.new(bytes(SecretKey, 'utf-8'), bytes(info, 'utf-8'), hashlib.sha1).digest() # 加密
    sign = base64.b64encode(signindex + bytes(info, 'utf-8')) # 多次有效签名
    # 请求地址
    url = "https://recognition.image.myqcloud.com/ocr/idcard"
    # 请求头
    headers = {
        "Host": "recognition.image.myqcloud.com",
        "content-type": "application/json",
        "authorization": sign
    }
    # 请求数据
    data = {
        'appid': appid,
        'card_type': face,
        'url_list': image_list
    }
    # 发起请求
    r = requests.post(url, json=data, headers=headers)
    # 响应数据
    responseinfo = r.content
    data = responseinfo.decode('utf-8') # 解码

    print(data)
    return data


# 解析身份证照片识别返回数据,只传入一个图片
def idcard_info(image_list=[], face=0):
    shuju = {}
    # 获取请求到的数据
    data = Know_Idcard(image_list=image_list, face=face)
    data = eval(data)
    print(type(data))
    data = data['result_list'][0]
    data = data['data'] # 获取具体的数据
    try:
        if face == 0:
            shuju['name'] = data['name']
            shuju['sex'] = data['sex']
            shuju['nation'] = data['nation']
            shuju['birth'] = data['birth']
            shuju['address'] = data['address']
            shuju['id'] = data['id']
        elif face == 1:
            shuju['issue'] = data['authority']
            shijian = data['valid_date'].split('-')
            print(shijian)
            shuju['start_date'] = shijian[0] #身份证有效期起始时间
            shuju['end_date'] = shijian[1] #身份证有效期截止时间
    except Exception:
        shuju = {}
    print("传递的数据：", shuju)
    return shuju


if __name__ == "__main__":
    idcard_info(image_list=["http://a4.qpic.cn/psb?/V13Ailyy16KjTa/x5xVc2EsUXBOxvXnfL63X3z0Asayf.5QRuN4ta.5L.Q!/b/dL8AAAAAAAAA&ek=1&kp=1&pt=0&bo=OASgBQAAAAARF7k!&tl=3&vuin=1285338586&tm=1559912400&sce=60-2-2&rf=viewer_4"], face=1)