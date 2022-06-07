# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import  json
from commons.base import Base
from commons.config import host
from commons.log import loggers

class Get_token(Base):

    def gettokepa(self):
        #数据集
        path = "/permission//serviceByUserInfo/validateUser.do"
        url = host + path
        datas = {
                "tokenID":"0",
                "account":"dataxone",
                "pwd":"123456"
        }
        """
            判断是否登录成功，登录成功后获取token
        """
        try:
            # 获取response
            response = self.post_data(url=url,data=datas)
            newres = json.loads(response.text)

            # 获取tokenID
            token = newres["dataInfo"]["tokenID"]
            # 获取状态码和message
            code = response.status_code
            message = newres["message"]
            if code == 200 and "正常登录" in message:
                return token
            else:
                loggers.info("获取token失败".center(50,"!"))
        except Exception as e:
            loggers.info("获取token异常".center(50,"@"))



if __name__ == "__main__":
    g = Get_token()
    g.gettokepa()