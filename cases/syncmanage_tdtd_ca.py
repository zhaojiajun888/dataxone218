# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import time
import unittest
from commons.log import loggers
from interfaces.synmanage.clone_tdtd_pa import Clone_tdtd
from interfaces.synmanage.savelink_tdtd_pa import Savelink_tdtd
from interfaces.synmanage.aimmachine_tdtd_pa import Aimmachine_tdtd
from interfaces.synmanage.done_tdtd_pa import Done_tdtd
from interfaces.synmanage.start_tdtd_pa import Start_tdtd
from interfaces.synmanage.others_tdtd_pa import Others_tdtd
from interfaces.synmanage.quetaskname_tdtd_pa import Quetaskname_tdtd


class Syncmanage_tdtd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        loggers.info("开始执行tdsql->tdsql,1对1,非多目标端，实时任务".center(60,"-"))

    def test_1_quetaskname_tdtd(self):
        """创建同步任务时相关查询接口"""

        """# 查询任务名称是否重复  validateServiceNameInfo"""
        save = Quetaskname_tdtd()
        save.validateServiceName_tdtd()
        time.sleep(0.2)

        """# 查询 isalarm"""
        save.isalarm_tdtd()
        time.sleep(0.2)

        """# 查询getAlarmMessage"""
        save.getAlarmMessage_tdtd()
        time.sleep(0.2)

    def test_2_savelink_tdtd(self):
        """实现：选择链路-选择源端主机"""

        """ # 保存选择链路相关内容 saveRelMloderDetailValue"""
        save = Savelink_tdtd()
        save.saveRelMloderDetail_tdtd()
        time.sleep(0.2)

        """# 保存创建任务页面相关内容 saveModuleEngineFlowInfo"""
        save.saveModuleEngineFlow_tdtd()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.saveFlowLogInfo_tdtd()
        time.sleep(0.2)

        """# 再次保存 saveRelMloderDetailValue"""
        save.saveRelMloderDetail0_tdtd()
        time.sleep(0.2)

        """# 将源端路径放入txt"""
        save.writepath_tdtd_s()
        time.sleep(0.2)

        """# 保存源端主机相关信息1（默认路径） publicSaveFlowMacConfigureInfo"""
        save.publicSaveFlowMacConf_tdtd()
        time.sleep(0.2)

        """# 再次保存log saveFlowLogInfo"""
        save.saveFlowLogInfoagain_tdtd()
        time.sleep(0.2)

        """# 保存 publicSaveFlowMacConfigureInfo"""
        save.publicSaveFlowMacConf1_tdtd()
        time.sleep(0.2)

        """# 保存 publicSaveEngineModuleDataBaseID"""
        save.SaveEngineDataBaseID_tdtd()
        time.sleep(0.2)

        """# 保存 publicSaveFlowConfigureInfo"""
        save.publicSaveFlowConfigure2_tdtd()
        time.sleep(0.2)

        """# 再次保存 saveModuleEngineFlowInfo"""
        save.saveModuleEngineFlowagain_tdtd()
        time.sleep(0.2)

    def test_3_aimmachine_tdtd(self):
        """设置目标端主机"""

        """ # 将目标端路径存入txt"""
        save = Aimmachine_tdtd()
        save.writepath_tdtd_d()
        time.sleep(0.2)

        """# 保存目标端 publicSaveFlowMacConfigureInfo"""
        save.des_publicSaveConf_tdtd()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.des_saveFlowLogInfo_tdtd()
        time.sleep(0.2)

        """# 再次保存 publicSaveFlowMacConfigureInfo"""
        save.des_saveMacConfigure_tdtd()
        time.sleep(0.2)

        """ # 保存 publicSaveEngineModuleDataBaseID"""
        save.des_publicDataBaseID_tdtd()
        time.sleep(0.2)

        """ # 保存 publicSaveFlowConfigureInfo"""
        save.des_SaveFlowConfigure_tdtd()
        time.sleep(0.2)

        """# 保存 saveModuleEngineFlowInfo"""
        save.des_ModuleEngineFlow_tdtd()
        time.sleep(0.2)

    def test_4_done_tdtd(self):
        """完成及以后的接口"""

        """#点击完成 saveEngineModuleDetailsConfInfoNoFile"""
        save = Done_tdtd()
        save.saveConfInfoNoFile_tdtd()
        time.sleep(0.2)

        """ # 开始执行 startAuto"""
        save.startAuto_tdtd()
        time.sleep(0.2)

        """ # 检查 totalCheck(需要在case中执行，否则报错)"""
        save.totalCheck_tdtd()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.done_saveFlowLog_tdtd()
        time.sleep(0.2)

        """#保存 saveModuleEngineFlowInfo"""
        save.done_saveModuleEngineFlow_tdtd()
        time.sleep(0.2)

        """# 查询源端 getEngineModuleDetailsConfInfo"""
        save.done_getEngineModuleDetails_tdtd()
        time.sleep(0.2)

        """# 查询源端 readEngineModuleDetailsConfInfo"""
        save.done_readModuleDetails_tdtd()
        time.sleep(0.2)

        """# 获取 getEngineModuleDetailsConfInfo(目标端)"""
        save.done_getEngineModuleDetail1_tdtd()
        time.sleep(0.2)

        """ # 读取 readEngineModuleDetailsConfInfo(目标端)"""
        save.readEngineModuleDetail1_tdtd()
        time.sleep(0.2)

        """# 获取文件名称 getFileNameByDbType"""
        save.done_getFileNameByDbType_tdtd()
        time.sleep(0.2)

    def test_5_start_tdtd(self):
        """点击启动及以后的接口"""

        """ # getModuleInfomationByFlowID"""
        save = Start_tdtd()
        save.getModuleInfomation_tdtd()
        time.sleep(0.2)

        """# 启动源端execCommand"""
        save.done_execCommand_tdtd()
        time.sleep(0.2)

        """# 查询 getModuelOperationInfomation"""
        save.done_getOperationInfo_tdtd()
        time.sleep(0.2)

        """ # 保存log saveFlowLogInfo"""
        save.done_saveFlowLog_tdtd()
        time.sleep(0.2)

        """# 再次执行 execCommand（目标端）"""
        save.done_execCommand1_tdtd()
        time.sleep(0.2)

        """# getModuelOperationInfomation（目标端）"""
        save.getModuelOperationInfo1_tdtd()
        time.sleep(0.2)

        """# 目标端启动日志 saveFlowLogInfo"""
        save.saveFlowLog1_tdtd()
        time.sleep(0.2)

        """# 判断是否启动成功  getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID1_tdtd()
        time.sleep(0.2)

    def test_6_others_tdtd(self):
        """运行，停止运行，删除"""

        """# 运行 runningEngineModuleToRemotrHost"""
        save = Others_tdtd()
        save.runningEngineModule_tdtd()
        time.sleep(0.2)

        """ # 获取运行后的状态信息判断是否运行成功 getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID_tdtd()
        time.sleep(0.2)

        """ # 保存日志 saveFlowLogInfo"""
        save.run_saveFlowLog_tdtd()
        time.sleep(0.2)

        """ # 停止运行源端  execCommand"""
        save.stop_execCommand_s_tdtd()
        time.sleep(0.2)

        """ # 停止运行（目标端） execCommand"""
        save.stop_execCommand_d_tdtd()
        time.sleep(0.2)

        """ # 获取停止后的状态信息判断是否停止成功 getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID1_tdtd()
        time.sleep(0.2)

        """-------------------克隆相关内容--------------------"""

        """检查名称是否重复 flowsClone"""
        cl = Clone_tdtd()
        cl.clonePreCheck_tdtd()
        time.sleep(0.2)

        """克隆流 flowsClone """
        cl.flowsClone_tdtd()
        time.sleep(0.2)

        """ # 获取克隆进程  getCloneProgress"""
        cl.getCloneProgress_tdtd()
        time.sleep(0.2)

        """删除克隆的任务 deleteModuleEngineFlowInfo"""
        cl.deleteModuleEngine_tdtd()
        time.sleep(0.2)

        """ # 删除任务 deleteModuleEngineFlowInfo"""
        save.deletflowinfo_tdtd()
        time.sleep(0.2)



if __name__ == "__main__":
    s = Syncmanage_tdtd()
    s.test_1_quetaskname_tdtd()
    s.test_2_savelink_tdtd()