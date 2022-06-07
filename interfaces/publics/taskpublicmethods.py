# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import json
from commons.log import loggers
from commons.config import newhost,host
from interfaces.publics.publicmethods import Publicmethods

class Taskpublicmethods(Publicmethods):
    """
        同步管理公共方法
    """

    # # 保存公共操作
    # def saveopera(self,url,datas=None,header=None):
    #         response = self.post_data(url=url,data=datas,headers=header)
    #         return response

    # 同步管理-选择链路相关
    path = "/autoMaticEngineBoot-1.0.0/MloaderOperationController/saveRelMloderDetailValue.do"
    url = newhost + path
    def saveRelMloderDetailValue(self,urls=url,datas=None,headers=None):
        try:
            response = self.post_data(url=urls,data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes,newres
        except:
           loggers.info("taskpublicmethods.saveRelMloderDetailValue异常，请检查".center(60,"@"))

    # 保存创建任务页面相关内容
    path1 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/saveModuleEngineFlowInfo.do"
    url1 = newhost + path1
    def saveModuleEngineFlowInfo(self,url=url1,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except:
            loggers.info("taskpublicmethods.saveModuleEngineFlowInfo异常，请检查".center(60, "@"))

    # 保存log
    path2 = "/autoMaticEngineBoot-1.0.0/operatorLogController/saveFlowLogInfo.do"
    url2 = newhost + path2
    def saveFlowLogInfo(self,url=url2,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except:
            loggers.info("taskpublicmethods.saveFlowLogInfopa异常，请检查".center(60, "@"))

    # 保存publicSaveFlowMacConfigureInfo.do
    path3 = "/autoMaticEngineBoot-1.0.0//serviceByDynamicFlow/publicSaveFlowMacConfigureInfo.do"
    url3 = newhost + path3
    def publicSaveFlowMacConfigureInfo(self,url=url3,datas=None,headers=None):
        try:
            response = self.post_data(url=url,data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes,newres
        except Exception as e:
            loggers.info("taskpublicmethods.publicSaveFlowMacConfigureInfo，请检查".center(60, "@"))

    # 保存 publicSaveEngineModuleDataBaseID
    path4 = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/publicSaveEngineModuleDataBaseID.do"
    url4 = newhost + path4
    def publicSaveEngineModuleDataBaseID(self,url=url4,datas=None,headers=None):
        try:
            response = self.post_data(url=url,data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.publicSaveEngineModuleDataBaseID执行异常，请检查".center(60, "@"))

    # 查询源端/目标端 ip  queryMachineConfigureInfo
    path5 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/queryMachineConfigureInfo.do"
    url5 = newhost + path5
    def queryMachineConfigureInfo(self,url=url5,datas=None,headers=None):
        try:
            response = self.post_data(url=url,data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.queryMachineConfigureInfo，请检查".center(60,"@"))

    # 查询路径 getDefaultPathByMacID
    path6 = "/autoMaticEngineBoot-1.0.0/hostAndDataSourceConfig/getDefaultPathByMacID.do"
    url6 = newhost + path6
    def getDefaultPathByMacID(self,url=url6,datas=None,headers=None):
        try:
            response = self.post_data(url=url,data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.getDefaultPathByMacID执行异常，请检查".center(60,"@"))

    # 保存 publicSaveFlowConfigureInfo
    path7 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/publicSaveFlowConfigureInfo.do"
    url7 = newhost + path7
    def publicSaveFlowConfigureInfo(self,url=url7,datas=None,headers=None):
        try:
            response = self.post_data(url=url,data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.publicSaveFlowConfigureInfo执行异常，请检查".center(60,"@"))

    # 点击完成 saveEngineModuleDetailsConfInfoNoFile
    path8 = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/saveEngineModuleDetailsConfInfoNoFile.do"
    url8 = newhost + path8
    def saveConfInfoNoFile(self,url=url8,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.saveConfInfoNoFile执行异常，请检查".center(60, "@"))

    # 开始执行 startAuto
    path9 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/startAuto.do"
    url9 = newhost + path9
    def startAuto(self,url=url9,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.startAuto执行异常，请检查".center(60, "@"))

    # 检查 totalCheck
    path10 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/totalCheck.do"
    url10 = newhost + path10
    def totalCheck(self,url=url10,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.totalCheck执行异常，请检查".center(60, "@"))

    # 查询 getEngineModuleDetailsConfInfo
    path11 = "/autoMaticEngineBoot-1.0.0/ddlDetailConfigController/getEngineModuleDetailsConfInfo.do"
    url11 = newhost + path11
    def getEngineModuleDetailsConfInfo(self,url=url11,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.getEngineModuleDetailsConfInfo执行异常，请检查".center(60, "@"))

    # 查询 readEngineModuleDetailsConfInfo
    path12 = "/autoMaticEngineBoot-1.0.0/ddlDetailConfigController/readEngineModuleDetailsConfInfo.do"
    url12 = newhost + path12
    def readEngineModuleDetailsConfInfo(self,url=url12,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.readEngineModuleDetailsConfInfo执行异常，请检查".center(60, "@"))

    # 获取文件名称 getFileNameByDbType
    path13 = "/autoMaticEngineBoot-1.0.0/engineDetailConfigController/getFileNameByDbType.do"
    url13 = newhost + path13
    def getFileNameByDbType(self,url=url13,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.getFileNameByDbType执行异常，请检查".center(60, "@"))

    # 查询 getYldCustomConfInfo
    path14 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/getYldCustomConfInfo.do"
    url14 = newhost + path14
    def getYldCustomConfInfo(self,url=url14,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.getYldCustomConfInfo执行异常，请检查".center(60,"@"))

    # 查询 getModuelOperationInfomation
    path15 = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/getModuelOperationInfomation.do"
    url15 = newhost + path15
    def getModuelOperationInfomation(self,url=url15,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.getModuelOperationInfomation执行异常，请检查".center(60,"@"))

    # execCommand
    path16 = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/execCommand.do"
    url16 = newhost + path16
    def execCommand(self,url=url16,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.gexecCommand执行异常，请检查".center(60,"@"))

    # 保存saveYldCustomConfInfo
    path17 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/saveYldCustomConfInfo.do"
    url17 = newhost + path17
    def saveYldCustomConfInfo(self,url=url17,datas= None,headers= None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.gsaveYldCustomConfInfo执行异常，请检查".center(60,"@"))

    # 保存 saveSourceDetailConfigInfo
    path18 = "/autoMaticEngineBoot-1.0.0/ddlDetailConfigController/saveSourceDetailConfigInfo.do"
    url18 = newhost + path18
    def saveSourceDetailConfigInfo(self,url=url18,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.saveSourceDetailConfigInfo执行异常，请检查".center(60,"@"))

    # 获取运行信息  getModuleInfomationByFlowID
    path19 = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/getModuleInfomationByFlowID.do"
    url19 = newhost + path19
    def getModuleInfomationByFlowID(self,url=url19,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.getModuleInfomationByFlowID执行异常，请检查".center(60,"@"))

    # 运行 runningEngineModuleToRemotrHost
    path20 = "/autoMaticEngineBoot-1.0.0/serviceByModuleOperation/runningEngineModuleToRemotrHost.do"
    url20 = newhost + path20
    def runningEngineModuleToRemotrHost(self,url=url20,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.runningEngineModuleToRemotrHost执行异常，请检查".center(60,"@"))

    # 删除任务 deleteModuleEngineFlowInfo
    path21 = "/autoMaticEngineBoot-1.0.0/serviceByDynamicFlow/deleteModuleEngineFlowInfo.do"
    url21 = newhost + path21
    def deleteModuleEngineFlowInfo(self,url=url21,datas=None,headers=None):
        try:
            response = self.post_data(url=url, data=datas)
            codes = response.status_code
            res = response.text
            newres = json.loads(res)
            return codes, newres
        except Exception as e:
            loggers.info("taskpublicmethods.deleteModuleEngineFlowInfo执行异常，请检查".center(60,"@"))



if __name__ == "__main__":
        p = Publicmethods()
