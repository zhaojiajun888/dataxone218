# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import uuid
from commons.log import loggers
from commons.fileopera import Fileopera
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.clonepublicmethods import Clonebase

class Clone_tdtd(Publicmethods):
    """
        tdsql-tdsql，一对一，不开启分离
        在savelink5_tdtd_pa,停止运行后进行克隆,删除
        实现:克隆,删除克隆数据
    """
    def __init__(self):
        super(Clone_tdtd, self).__init__()
        # 获取taskname 和follow_id
        self.taskname, self.follow_id = Fileopera().readfilepa()
        # 获取克隆任务名称
        self.name1, self.name2 = Clonebase().setclonename()
        # 生成uuid
        self.uuids = uuid.uuid1()

    # 检查克隆任务名称  clonePreCheck
    def clonePreCheck_tdtd(self):
        servicename = self.name1 + "," + self.name2
        params = {
            "serviceNameList": servicename,
            "tokenID": self.token
        }
        try:
            codes, newres = Clonebase().clonePreCheck(datas=params)
            rename1 = newres["dataInfo"]["rows"][0]["serviceName"]
            rename2 = newres["dataInfo"]["rows"][1]["serviceName"]
            if self.name1 == rename1 and self.name2 == rename2:
                loggers.info("Clone_tdtd_pa.clonePreCheck_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("Clone_tdtd_pa.clonePreCheck_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("Clone_tdtd_pa.clonePreCheck_tdtd执行异常".center(60, "@"))

    # 克隆流 flowsClone(单独执行报错)
    def flowsClone_tdtd(self):
        servicename = self.name1 + "," + self.name2
        params = {
            "flowIds": self.follow_id,
            "cloneCount": 2,
            "batch_id": self.uuids,
            "serviceNameList": servicename,
            "tokenID": self.token
        }
        try:
            codes, newres = Clonebase().flowsClone(datas=params)
            info = newres["dataInfo"]
            if codes == 200 and "completed" in info:
                loggers.info("clone_tdtd_pa.flowsClone_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("clone_tdtd_pa.flowsClone_tdtd执行异常".center(60, "!"))
        except Exception as e:
            loggers.info("clone_tdtd_pa.flowsClone_tdtd执行异常".center(60, "@"))

    # 获取克隆进程  getCloneProgress
    def getCloneProgress_tdtd(self):
        params = {
            "flowIds": self.follow_id,
            "batch_id": self.uuids,
            "tokenID": self.token
        }
        codes, newres = Clonebase().getCloneProgress(datas=params)
        flag = newres["statFlag"]
        if codes == 200 and flag == 0:
            loggers.info("clone_tdtd_pa.getCloneProgress_tdtd执行成功".center(60, "~"))
        else:
            loggers.info("clone_tdtd_pa.getCloneProgress_tdtd执行失败".center(60, "!"))

    """通过克隆数据名称查询flowid  以便于删除 getAllSaveModuleEngineFlowDescInfo"""

    def getflowid(self):
        namelist = [self.name1, self.name2]
        flowid_list = []
        for name in namelist:
            params = {
                "tokenID": self.token,
                "limit": "10",
                "offset": "0",
                "flowName": name,
                "dbContent": "",
                "createTimeStart": "",
                "createTimeEnd": "",
                "sortOrder": "",
                "userID": "1"
            }
            try:
                codes, newres = Clonebase().getFlowDescInfo(datas=params)
                flowid = newres["dataInfo"]["rows"][0]["flowId"]
                flowid_list.append(flowid)
            except Exception as e:
                loggers.info("clone_tdtd_pa.getflowid执行异常".center(60, "@"))
        return flowid_list

    # 删除克隆的任务 deleteModuleEngineFlowInfo
    def deleteModuleEngine_tdtd(self):
        flowidlist = self.getflowid()
        print(flowidlist)
        for flowid in flowidlist:
            params = {
                "tokenID": self.token,
                "deleteFlag": "false",
                "flowId": flowid
            }
            try:
                codes, newres = Clonebase().deleteModuleEngine(datas=params)
                reflowid = newres["dataInfo"]["flowId"]
                if codes == 200 and reflowid == flowid:
                    loggers.info("clone_tdtd_pa.deleteModuleEngine_tdtd执行成功".center(60, "~"))
                else:
                    loggers.info("clone_tdtd_pa.deleteModuleEngine_tdtd执行失败".center(60, "!"))
            except Exception as e:
                loggers.info("clone_tdtd_pa.deleteModuleEngine_tdtd执行异常".center(60, "@"))
