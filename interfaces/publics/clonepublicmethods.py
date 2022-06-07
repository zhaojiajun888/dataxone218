# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import json
import time

from commons.log import loggers
from commons.config import newhost
from interfaces.publics.publicmethods import Publicmethods

class Clonebase(Publicmethods):

    # 设置克隆流程任务名称
    def setclonename(self):
        namelist = []
        name = "autoclone"
        times = time.strftime("%M%S", time.localtime())
        # 设置两个克隆任务名称
        for num in range(1,3):
            strnum = str(num)
            newname = name + times + strnum
            namelist.append(newname)
        return namelist

    # 检查克隆任务名称  clonePreCheck
    path1 = "/autoMaticEngineBoot-1.0.0/TemplateOperationController/clonePreCheck.do"
    url1 = newhost + path1
    def clonePreCheck(self,url=url1,datas=None):
        try:
            response = self.post_data(url=url,data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes,newres
        except:
           loggers.info("clonepublicmethods.clonePreCheck异常，请检查".center(60,"@"))

    # 克隆流 flowsClone
    path2 = "/autoMaticEngineBoot-1.0.0/serviceByAutomatedDeployment/flowsClone.do"
    url2 = newhost + path2
    def flowsClone(self,url=url2,datas=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except:
            loggers.info("clonepublicmethods.flowsClone异常，请检查".center(60,"@"))

    # 获取克隆进程  getCloneProgress
    path3 = "/autoMaticEngineBoot-1.0.0/serviceByAutomatedDeployment/getCloneProgress.do"
    url3 = newhost + path3
    def getCloneProgress(self,url=url3,datas=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except:
            loggers.info("clonepublicmethods.getCloneProgress异常，请检查".center(60,"@"))

    # 查询任务 getAllSaveModuleEngineFlowDescInfo
    path4 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/getAllSaveModuleEngineFlowDescInfo.do"
    url4 = newhost + path4
    def getFlowDescInfo(self,url=url4,datas=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except:
            loggers.info("clonepublicmethods.getFlowDescInfo异常，请检查".center(60,"@"))

    # 删除数据 deleteModuleEngineFlowInfo
    path5 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/deleteModuleEngineFlowInfo.do"
    url5 = newhost + path5
    def deleteModuleEngine(self,url=url5,datas=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except:
            loggers.info("clonepublicmethods.deleteModuleEngine异常，请检查".center(60,"@"))



if __name__ == "__main__":
    c = Clonebase()
    # c.setclonename()
    c.flowsClone()