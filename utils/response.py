"在此文件确定相应的状态码"

# 响应状态码
class ReturnCode:
    SUCCESS = 0 # 成功则返回0

    FAILED = -100
    WRONG_PARMAS = -101
    RESOURCE_NOT_FOUND = -102

    UNAUTHORIZED = -500
    BROKEN_AUTHORIZED_DATA = -501
    SESSION_EXPIRED = -502

    @classmethod
    def message(cls, code):
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorized'
        elif code == cls.WRONG_PARMAS:
            return 'wrong params'
        elif code == cls.RESOURCE_NOT_FOUND:
            return 'resources not found'
        elif code == cls.UNAUTHORIZED:
            return 'request unauthorized'
        elif code == cls.BROKEN_AUTHORIZED_DATA:
            return 'broken authorized data'
        elif code == cls.SESSION_EXPIRED:
            return 'session expired'

# Mixin类
class CommonResponseMixin(object):
    @classmethod
    def wrap_json_response(cls, data=None, code=None, message=None):
        response = {}
        if not code: # 如果成功则返回
            code = ReturnCode.SUCCESS
        if not message: # 为None则返回状态吗相应的message，不为None则返回定义好的message
            message = ReturnCode.message(code)
        if data is not None: # 数据为空，则不返回data，数据不为空则返回传递的data
            response['data'] = data
        response['result_code'] = code
        response['message'] = message
        return response