# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import time
from commons.log import loggers
from commons.fileopera import Fileopera
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods


class Others_om(Publicmethods):
    """
        oracle-mysql，一对一，不开启分离
        承接 Start_om_pa
        实现:运行，停止运行，删除
    """
    def __init__(self):
        super(Others_om, self).__init__()
        # 获取taskname 和follow_id
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 运行 runningEngineModuleToRemotrHost
    def runningEngineModule_om(self):
        params = {
                "flowID" : self.follow_id,
                "serviceName" : self.taskname,
                "pathList" : "{}",
                "oper_code": "1-0",
                "value1":"",
                "value2":"",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().runningEngineModuleToRemotrHost(datas=params)
            flag = newres["dataInfo"]["flag"]
            if codes == 200 and flag == True:
                loggers.info("others_om_pa.runningEngineModule_om执行成功".center(60,"~"))
            else:
                loggers.info("others_om_pa.runningEngineModule_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("others_om_pa.runningEngineModule_om执行异常，请检查".center(60,"@"))

    # 获取运行后的状态信息判断是否运行成功 getModuleInfomationByFlowID
    def getModuleInfoByFlowID_om(self):
        """此处需要循环遍历查询，有时间延迟导致operationStat字段值为start而不是run"""
        params = {
            "flowID": self.follow_id,
            "statType": "run",
            "tokenID": self.token
        }
        try:
            for i in range(1, 17):
                time.sleep(2)
                codes, newres = Taskpublicmethods().getModuleInfomationByFlowID(datas=params)
                stat_s = newres["dataInfo"]["replicateList"][0]["relationList"][0]["operationStat"]
                stat_d = newres["dataInfo"]["replicateList"][0]["relationList"][1]["operationStat"]
                print("运行后源端状态：", stat_s)
                print("运行后目标端状态：", stat_d)
                if stat_s == "run" and stat_d == "run" and i <= 15:
                    loggers.info("others_om_pa.getModuleInfoByFlowID_om执行成功".center(60, "~"))
                    break
                elif i >= 16:
                    loggers.info("others_om_pa.getModuleInfoByFlowID_om执行失败,不再尝试，请检查".center(60, "!"))
                else:
                    loggers.info("others_om_pa.getModuleInfoByFlowID_om执行失败,继续尝试".center(60, "!"))
        except Exception as e:
            loggers.info("others_om_pa.getModuleInfoByFlowID_om执行异常,请检查".center(60, "@"))

    # 保存日志 saveFlowLogInfo
    def run_saveFlowLogInfo_om(self):
        params = {
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName" : self.taskname,
                "operInfo" : "流程运行成功",
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and message == "success":
                loggers.info("others_om_pa.run_saveFlowLogInfo_om执行成功".center(60,"~"))
            else:
                loggers.info("others_om_pa.run_saveFlowLogInfo_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("others_om_pa.run_saveFlowLogInfo_om执行异常，请检查".center(60,"@"))


    # 停止运行源端  execCommand(需要放到case中)
    def stop_execCommand_s_om(self):
        params = {
            "flowID": self.follow_id,
            "operType": "stop",
            "flowName": "",
            "engineID": "20",
            "moduleID": "1",
            "engineTypeCode": "100",
            "pathList": "",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().execCommand(datas=params)
            datainfo = newres["dataInfo"]
            if codes == 200 and datainfo == "true":
                loggers.info("others_om_pa.stop_execCommand_s_om执行成功".center(60, "~"))
            else:
                loggers.info("others_om_pa.stop_execCommand_s_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("others_om_pa.stop_execCommand_s_om执行异常，请检查".center(60, "@"))

    # 停止运行（目标端） execCommand(需要放到case中)
    def stop_execCommand_d_om(self):
        params = {
                "flowID" : self.follow_id,
                "operType" : "stop",
                "flowName" : "",
                "engineID" : "31",
                "moduleID" : "3",
                "engineTypeCode" : "201",
                "pathList" : "",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().execCommand(datas=params)
            datainfo = newres["dataInfo"]
            if codes == 200 and datainfo == "true":
                loggers.info("others_om_pa.stop_execCommand_d_om执行成功".center(60, "~"))
            else:
                loggers.info("others_om_pa.stop_execCommand_d_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("others_om_pa.stop_execCommand_d_om执行异常，请检查".center(60,"@"))

    # 获取停止后的状态信息判断是否停止成功 getModuleInfomationByFlowID
    def getModuleInfoByFlowID1_om(self):
        """此处需要循环遍历查询，有时间延迟导致operationStat字段值错误"""
        params = {
            "flowID": self.follow_id,
            "statType": "stop",
            "tokenID": self.token
        }
        try:
            for i in range(1, 17):
                time.sleep(2)
                codes, newres = Taskpublicmethods().getModuleInfomationByFlowID(datas=params)
                stat_s = newres["dataInfo"]["replicateList"][0]["relationList"][0]["operationStat"]
                stat_d = newres["dataInfo"]["replicateList"][0]["relationList"][1]["operationStat"]
                print("停止后源端状态：", stat_s)
                print("停止后目标端状态：", stat_d)
                if stat_s == "stop" and stat_d == "stop" and i <= 15:
                    loggers.info("others_om_pa.getModuleInfoByFlowID1_om执行成功".center(60, "~"))
                    break
                elif i >= 16:
                    loggers.info("others_om_pa.getModuleInfoByFlowID1_om执行失败,不再尝试，请检查".center(60, "!"))
                else:
                    loggers.info("others_om_pa.getModuleInfoByFlowID1_om执行失败,继续尝试".center(60, "!"))
        except Exception as e:
            loggers.info("others_om_pa.getModuleInfoByFlowID1_om执行异常,请检查".center(60, "@"))

    # 删除任务 deleteModuleEngineFlowInfo
    def deletflowinfo_om(self):
        params = {
            "deleteFlag": "false",
            "flowId": self.follow_id,
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().deleteModuleEngineFlowInfo(datas=params)
            followid = newres["dataInfo"]["flowId"]
            if codes == 200 and followid == self.follow_id:
                loggers.info("others_om_pa.deletflowinfo_om执行成功".center(60, "~"))
            else:
                loggers.info("others_om_pa.deletflowinfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("others_om_pa.deletflowinfo_om执行异常，请检查".center(60, "@"))


if __name__ == "__main__":
    s = Others_om()
    # s.getModuleInfomationByFlowID_om()
    # s.runningEngineModule_om()
    # s.run_saveFlowLogInfo_om()
    # s.stop_execCommand_s_om()
    # s.stop_execCommand_d_om()
    s.deletflowinfo_om()