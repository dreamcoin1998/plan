import requests
import hmac
import hashlib
import base64
import time
import random


# 营业执照照片识别
def Know_Bizlicense(image_url):
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
    url = "https://recognition.image.myqcloud.com/ocr/bizlicense"
    # 请求头
    headers = {
        "Host": "recognition.image.myqcloud.com",
        "content-type": "application/json",
        "authorization": sign
    }
    # 请求数据
    data = {
        'appid': appid,
        'url': image_url
    }
    # 发起请求
    print('请求地址：', url)
    print('图片地址：', image_url)
    r = requests.post(url, json=data, headers=headers)
    print(r)
    # 响应数据
    responseinfo = r.content
    data = responseinfo.decode('utf-8') # 解码

    print(data)
    return data


# 解析营业执照照片识别返回数据,只传入一个图片
def bizlicense_info(image_url):
    # 获取请求到的数据
    data = Know_Bizlicense(image_url)
    try:
        data = eval(data)
        data = data['data']
        data = data['items'] # 获取具体的数据集
        print(data)
    except Exception:
        print('解析失败')
        data = []
    shuju = {}
    # 解析具体的数据
    for i in data:
        shuju[i['item']] = i['itemstring']
    print('得到的数据：', shuju)
    return shuju


if __name__ == '__main__':
    bizlicense_info('https://mimg.127.net/p/3c/img/zz_1_2019.jpg')