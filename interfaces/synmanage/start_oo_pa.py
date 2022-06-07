# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'


import json
import time

from commons.log import loggers
from commons.config import newhost,ip71
from commons.fileopera import Fileopera
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Start_oo(Publicmethods):
    """
       oracle-oracle，一对一，不开启分离
        承接 done_oo_pa
        实现:点击启动及以后的接口
    """
    def __init__(self):
        super(Start_oo, self).__init__()
        # 获取taskname 和follow_id
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # getModuleInfomationByFlowID
    # 单独执行报错
    def getModuleInfomationByFlowID_oo(self):
        path = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/getModuleInfomationByFlowID.do"
        url = newhost + path
        params = {
            "flowID": self.follow_id,
            "statType": "start",
            "tokenID": self.token
        }
        try:
            response = self.post_data(url=url, data=params)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            servicename = newres["dataInfo"]["replicateList"][0]["serviceName"]
            if codes == 200 and servicename == self.taskname:
                loggers.info("start_oo_pa.getModuleInfomationByFlowID_oo执行成功".center(60, "~"))
            else:
                loggers.info("start_oo_pa.getModuleInfomationByFlowID_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("start_oo_pa.getModuleInfomationByFlowID_oo执行异常，请检查".center(60, "@"))

    # 源端execCommand,需在case中执行，单独执行失败
    def done_execCommand_oo(self):
        params = {
                "flowID" : self.follow_id,
                "operType" : "start",
                "flowName" : "",
                "engineID" : "20",
                "moduleID" : "1",
                "engineTypeCode" : "100",
                "pathList" : "",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().execCommand(datas=params)
            datainfo = newres["dataInfo"]
            if codes == 200 and datainfo == "true":
                loggers.info("start_oo_pa.done_execCommand_oo执行成功".center(60,"~"))
            else:
                loggers.info("start_oo_pa.done_execCommand_oo执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("start_oo_pa.done_execCommand_oo执行异常,请检查".center(60,"@"))

    # 查询 getModuelOperationInfomation
    def done_getOperationInfomation_oo(self):
        params = {
            "flowID": self.follow_id,
            "logType": "start",
            "flowName": "",
            "engineID": "20",
            "moduleID": "1",
            "hostIp": ip71,
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().getModuelOperationInfomation(datas=params)
            flowid = newres["dataInfo"]["flowID"]
            if codes == 200 and flowid == self.follow_id:
                loggers.info("start_oo_pa.done_getOperationInfomation_oo执行成功".center(60, "~"))
            else:
                loggers.info("start_oo_pa.done_getOperationInfomation_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("start_oo_pa.done_getOperationInfomation_oo执行异常，请检查".center(60, "@"))

    # 保存log saveFlowLogInfo
    def done_saveFlowLogInfo_oo(self):
        params = {
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName" : self.taskname,
                "operInfo" : "源端启动成功",
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            datainfo = newres["dataInfo"]
            if codes == 200 and datainfo == "true":
                loggers.info("start_oo_pa.done_saveFlowLogInfo_oo执行成功".center(60,"~"))
            else:
                loggers.info("start_oo_pa.done_saveFlowLogInfo_oo执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("start_oo_pa.done_saveFlowLogInfo_oo执行异常，请检查".center(60,"@"))

    # 再次执行 execCommand（目标端）
    def done_execCommand1_oo(self):
        print("$$$$$$$$$$$$$$$$$$$$$$", self.follow_id)
        params = {
                "flowID" : self.follow_id,
                "operType" : "start",
                "flowName" : "",
                "engineID" : "21",
                "moduleID" : "3",
                "engineTypeCode" : "101",
                "pathList" : "",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().execCommand(datas=params)
            datainfo = newres["dataInfo"]
            if codes == 200 and datainfo == "true":
                loggers.info("start_oo_pa.done_execCommand1_oo执行成功".center(60,"~"))
            else:
                loggers.info("start_oo_pa.done_execCommand1_oo执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("start_oo_pa.done_execCommand1_oo执行异常,请检查".center(60,"@"))

    # getModuelOperationInfomation（目标端）
    def getModuelOperationInfomation1_oo(self):
        params = {
                "flowID" : self.follow_id,
                "logType" : "start",
                "flowName" : "",
                "engineID" : "21",
                "moduleID" : "3",
                "hostIp" : ip71,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getModuelOperationInfomation(datas=params)
            followid = newres["dataInfo"]["flowID"]
            if codes == 200 and followid == self.follow_id:
                loggers.info("start_oo_pa.getModuelOperationInfomation1_oo执行成功".center(60,"~"))
            else:
                loggers.info("start_oo_pa.getModuelOperationInfomation1_oo执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("start_oo_pa.getModuelOperationInfomation1_oo执行异常，请检查".center(60, "@"))

    # 目标端启动日志 saveFlowLogInfo
    def saveFlowLogInfo1_oo(self):
        params = {
            "flowID": self.follow_id,
            "moduleID": "",
            "serviceName": self.taskname,
            "operInfo": "目标端启动成功",
            "operStat": "success",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and message == "success":
                loggers.info("start_oo_pa.saveFlowLogInfo1_oo执行成功".center(60, "~"))
            else:
                loggers.info("start_oo_pa.saveFlowLogInfo1_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("start_oo_pa.saveFlowLogInfo1_oo执行异常,请检查".center(60, "@"))

    # 判断是否启动成功  getModuleInfomationByFlowID
    def getModuleInfoByFlowID1_oo(self):

        path = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/getModuleInfomationByFlowID.do"
        url = newhost + path
        params = {
                "flowID" : self.follow_id,
                "statType" : "start",
                "tokenID" : self.token
        }
        try:
            for i in range(1,17):
                time.sleep(2)
                response = self.post_data(url=url, data=params)
                res = response.text
                newres = json.loads(res)
                # 判断源端和目标端的状态是否返回
                console_s = "operationStat" in newres["dataInfo"]["replicateList"][0]["relationList"][0]
                print("console_s:",console_s)
                console_d = "operationStat" in newres["dataInfo"]["replicateList"][0]["relationList"][1]
                print("console_d:",console_d)
                if console_s == True  and console_d == True and i<=15:
                    # 源端状态
                    status_s = newres["dataInfo"]["replicateList"][0]["relationList"][0]["operationStat"]
                    # 目标端状态
                    status_d = newres["dataInfo"]["replicateList"][0]["relationList"][1]["operationStat"]
                    break
                elif i>=16:
                    loggers.info("start_oo_pa.getModuleInfoByFlowID1_oo状态获取失败不再尝试".center(70,"!"))
                else:
                    loggers.info("start_oo_pa.getModuleInfoByFlowID1_oo状态获取失败继续尝试".center(70, "!"))
            print("status_s:",status_s)
            print("status_d:",status_d)
            # 判断是否启动成功
            if status_s == "start" and status_d == "start":
                loggers.info((self.taskname + "启动成功").center(60,"~"))
            else:
                loggers.info((self.taskname + "启动失败").center(60,"!"))
        except Exception as e:
            loggers.info("start_oo_pa.getModuleInfoByFlowID1_oo执行异常，请检查".center(60,"@"))



if __name__ == "__main__":
    s = Start_oo()
    # s.getModuleInfomationByFlowID_oo()
    # s.done_execCommand_oo()
    # s.done_getOperationInfomation_oo()
    # s.done_saveFlowLogInfo_oo()
    # s.done_execCommand1_oo()
    # s.getModuelOperationInfomation1_oo()
    s.saveFlowLogInfo1_oo()