# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import time
import unittest
from commons.log import loggers
from interfaces.synmanage.clone_om_pa import Clone_om
from interfaces.synmanage.savelink_om_pa import Savelink_om
from interfaces.synmanage.aimmachine_om_pa import Aimmachine_om
from interfaces.synmanage.done_om_pa import Done_om
from interfaces.synmanage.start_om_pa import Start_om
from interfaces.synmanage.others_om_pa import Others_om
from interfaces.synmanage.quetaskname_om_pa import Quetaskname_om

class Sycnanage_om(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        loggers.info("开始执行oracle->mysql,1对1,非多目标端，实时任务".center(60,"-"))

    def test_1_quetaskname_om(self):
        """创建同步任务时相关查询接口"""

        """ # 查询任务名称是否重复  validateServiceNameInfo"""
        save = Quetaskname_om()
        save.validateServiceNameInfo_om()
        time.sleep(0.2)

        """查询 isalarm_om"""
        save.isalarm_om()
        time.sleep(0.2)

        """# 查询getAlarmMessage"""
        save.getAlarmMessage_om()
        time.sleep(0.2)

        """# 查询getAllUserAndFlowRelation"""
        save.getAllUserAndFlowRelation_om()
        time.sleep(0.2)

    def test_2_savelink_om(self):
        """同步管理-实时同步-创建任务-选择链路-选择源端主机"""

        """# 保存选择链路相关内容 saveRelMloderDetailValue"""
        save = Savelink_om()
        save.saveRelMloderDetailValue_om()
        time.sleep(0.2)

        """ # 保存创建任务页面相关内容 saveModuleEngineFlowInfo"""
        save.saveModuleEngineFlowInfo_om()
        time.sleep(0.2)

        """ # 保存log saveFlowLogInfo"""
        save.saveFlowLogInfo_om()
        time.sleep(0.2)

        """ # 再次保存 saveRelMloderDetailValue"""
        save.saveRelMloderDetailValuepa0_om()
        time.sleep(0.2)

        """ # 将路径放入txt"""
        save.writepath_om_s()
        time.sleep(0.2)

        """ #保存源端主机相关信息1（默认路径） publicSaveFlowMacConfigureInfo"""
        save.publicSaveFlowMacConfigureInfo_om()
        time.sleep(0.2)

        """ # 再次保存log saveFlowLogInfo"""
        save.saveFlowLogInfoagain_om()
        time.sleep(0.2)

        """ # 保存 publicSaveFlowMacConfigureInfo"""
        save.publicSaveFlowMacConfigureInfo1_om()
        time.sleep(0.2)

        """ # 保存 publicSaveEngineModuleDataBaseID"""
        save.publicSaveEngineModuleDataBaseID_om()
        time.sleep(0.2)

        """ # 保存 publicSaveFlowConfigureInfo"""
        save.publicSaveFlowConfigureInfo2_om()
        time.sleep(0.2)

        """# 再次保存 saveModuleEngineFlowInfo"""
        save.saveModuleEngineFlowInfoagain_om()
        time.sleep(0.2)

    def test_3_aimmachine_om(self):
        """设置目标端主机"""

        """ # 将目标端路径存入txt"""
        save = Aimmachine_om()
        save.writepath_om_d()
        time.sleep(0.2)

        """ # 保存目标端 publicSaveFlowMacConfigureInfo"""
        save.des_publicSaveConfigureInfo_om()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.des_saveFlowLogInfo_om()
        time.sleep(0.2)

        """ # 再次保存 publicSaveFlowMacConfigureInfo"""
        save.des_saveMacConfigureInfo_om()
        time.sleep(0.2)

        """# 保存 publicSaveEngineModuleDataBaseID"""
        save.des_publicDataBaseID_om()
        time.sleep(0.2)

        """# 保存 publicSaveFlowConfigureInfo"""
        save.des_SaveFlowConfigureInfo_om()
        time.sleep(0.2)

        """ # 保存 saveModuleEngineFlowInfo"""
        save.des_ModuleEngineFlowInfo_om()
        time.sleep(0.2)

    def test_4_done_om(self):
        """完成及以后的接口"""

        """# 点击完成 saveEngineModuleDetailsConfInfoNoFile"""
        save = Done_om()
        save.saveConfInfoNoFile_om()
        time.sleep(0.2)

        """ # 开始执行 startAuto"""
        save.startAuto_om()
        time.sleep(0.2)

        """# 检查 totalCheck(需要在case中执行，否则报错)"""
        save.totalCheck_om()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.done_saveFlowLogInfo_om()
        time.sleep(0.2)

        """# 保存 saveModuleEngineFlowInfo"""
        save.done_saveModuleEngineFlowInfo_om()
        time.sleep(0.2)

        """# 查询源端 getEngineModuleDetailsConfInfo"""
        save.done_getEngineModuleDetailsConfInfo_om()
        time.sleep(0.2)

        """# 查询源端 readEngineModuleDetailsConfInfo"""
        save.done_readModuleDetailsConfInfo_om()
        time.sleep(0.2)

        """ # 获取 getEngineModuleDetailsConfInfo(目标端)"""
        save.done_getEngineModuleDetailsConfInfo1_om()
        time.sleep(0.2)

        """# 读取 readEngineModuleDetailsConfInfo(目标端)"""
        save.readEngineModuleDetailsConfInfo1_om()
        time.sleep(0.2)

        """ # 获取文件名称 getFileNameByDbType"""
        save.done_getFileNameByDbType_om()
        time.sleep(0.2)

    def test_5_start_om(self):
        """点击启动及以后的接口"""

        """# getModuleInfomationByFlowIDpa"""
        save = Start_om()
        save.getModuleInfomationByFlowID_om()
        time.sleep(0.2)

        """# 源端execCommand,需在case中执行，单独执行失败"""
        save.done_execCommand_om()
        time.sleep(0.2)

        """# 查询 getModuelOperationInfomation"""
        save.done_getOperationInfomation_om()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.done_saveFlowLogInfo_om()
        time.sleep(0.2)

        """# 再次执行 execCommand（目标端）"""
        save.done_execCommand1_om()
        time.sleep(0.2)

        """# getModuelOperationInfomation（目标端）"""
        save.getModuelOperationInfomation1_om()
        time.sleep(0.2)

        """ # 目标端启动日志 saveFlowLogInfo"""
        save.saveFlowLogInfo1_om()
        time.sleep(0.2)

        """# 判断是否启动成功  getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID1_om()
        time.sleep(0.2)

    def test_6_others_om(self):
        """运行，停止运行，删除"""

        """# 运行 runningEngineModuleToRemotrHost"""
        save = Others_om()
        save.runningEngineModule_om()
        time.sleep(0.2)

        """# 获取运行后的状态信息判断是否运行成功 getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID_om()
        time.sleep(0.2)

        """ # 保存日志 saveFlowLogInfo"""
        save.run_saveFlowLogInfo_om()
        time.sleep(0.2)

        """ # 停止运行源端  execCommand(需要放到case中)"""
        save.stop_execCommand_s_om()
        time.sleep(0.2)

        """# 停止运行（目标端） execCommand(需要放到case中)"""
        save.stop_execCommand_d_om()
        time.sleep(0.2)

        """ # 获取停止后的状态信息判断是否停止成功 getModuleIn fomationByFlowID"""
        save.getModuleInfoByFlowID1_om()
        time.sleep(0.2)

        """-------------------克隆相关内容--------------------"""

        """检查名称是否重复 flowsClone"""
        cl = Clone_om()
        cl.clonePreCheck_om()
        time.sleep(0.2)

        """克隆流 flowsClone """
        cl.flowsClone_om()
        time.sleep(0.2)

        """ # 获取克隆进程  getCloneProgress"""
        cl.getCloneProgress_om()
        time.sleep(0.2)

        """删除克隆的任务 deleteModuleEngineFlowInfo"""
        cl.deleteModuleEngine_om()
        time.sleep(0.2)

        """ # 删除任务 deleteModuleEngineFlowInfo"""
        save.deletflowinfo_om()
        time.sleep(0.2)

    @classmethod
    def tearDownClass(self) -> None:
        loggers.info("oracle->mysql,1对1,非多目标端，实时任务执行结束".center(60,"-"))


if __name__ == "__main__":
    s = Sycnanage_om()
    s.test_1_quetaskname_om()
    s.test_2_savelink_om()
    s.test_3_savelink2_om()
    s.test_4_savelink3_om()