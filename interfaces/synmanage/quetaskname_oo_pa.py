# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import json
from commons.log import loggers
from commons.config import host,newhost
from commons.fileopera import Fileopera
from interfaces.publics.publicmethods import Publicmethods


class Quetaskname_oo(Publicmethods):
    """
        oracle-oracle，一对一，不开启分离
        创建同步任务时先查询 名称是否重复
        创建同步任务时相关查询接口及创建任务
    """
    def __init__(self):
        super(Quetaskname_oo, self).__init__()
        # 生成taskname和followid并存入txt
        self.getfollowid()
        # 获取taskname和followid
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 查询任务名称是否重复  validateServiceNameInfo
    def validateServiceNameInfo_oo(self):

        path = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/validateServiceNameInfo.do"
        url = newhost + path
        params = {
            "serviceName": self.taskname,
            "tokenID": self.token
        }
        response = self.post_data(url=url, data=params)
        newres = json.loads(response.text)
        # 获取状态码和message
        codes = response.status_code
        message = newres["message"]
        """
            判断是否有重复的任务名称
            如果没有则查询成功
        """
        try:
            if codes == 200 and "success" in message:
                loggers.info("quetaskname_oo_pa.validateServiceNameInfo_oo执行成功".center(60, "~"))
            else:
                loggers.info("quetaskname_oo_pa.validateServiceNameInfo_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("quetaskname_oo_pa.validateServiceNameInfo_oo执行异常，请检查".center(60, "@"))

    # 查询 isalarm
    def isalarm_oo(self):
        path = "/permission//roleController/isAlarm.do"
        url = host + path
        datas = {
            "tokenID": self.token
        }
        try:
            response = self.post_data(url=url, data=datas)
            codes1 = response.status_code
            newres = json.loads(response.text)
            message = newres["message"]
            if codes1 == 200 and "success" in message:
                loggers.info("quetaskname_oo_pa.isalarm_oo执行成功".center(60, "~"))
            else:
                loggers.info("quetaskname_oo_pa.isalarm_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("quetaskname_oo_pa.isalarm_oo执行异常,请检查".center(60, "@"))

    # 查询getAlarmMessage
    def getAlarmMessage_oo(self):

        path = "/autoMaticEngineBoot-1.0.0/monitorController/getAlarmMessage.do"
        url = newhost + path
        datas = {
            "serviceName": self.taskname,
            "tokenID": self.token
        }
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            newres = json.loads(response.text)
            message = newres["message"]
            if codes == 200 and "success" in message:
                loggers.info("quetaskname_oo_pa.getAlarmMessage_oo执行成功".center(60, "~"))
            else:
                loggers.info("quetaskname_oo_pa.getAlarmMessage_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("quetaskname_oo_pa.getAlarmMessage_oo执行异常，请检查".center(60, "@"))

    # 查询getAllUserAndFlowRelation
    def getAllUserAndFlowRelation_oo(self):
        path = "/autoMaticEngineBoot-1.0.0/serviceByUserInfo/getAllUserAndFlowRelation.do"
        url = newhost + path
        datas = {
            "flowID": self.follow_id,
            "userID": "1",
            "tokenID": self.token
        }
        try:
            response = self.post_data(url=url, data=datas)
            text = response.text
            newres = json.loads(text)
            codes = response.status_code
            uid = newres["dataInfo"][0]["u_id"]
            if codes == 200 and uid == 1:
                loggers.info("quetaskname_oo_pa.getAllUserAndFlowRelation_oo执行成功".center(60, "~"))
            else:
                loggers.info("quetaskname_oo_pa.getAllUserAndFlowRelation_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("quetaskname_oo_pa.getAllUserAndFlowRelation_oo执行异常，请检查".center(60, "@"))





if __name__ == "__main__":
    q = Quetaskname_oo()
    q.validateServiceNameInfo_oo()
    q.isalarm_oo()
    q.getAlarmMessage_oo()
    q.getAllUserAndFlowRelation_oo()