# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import time
import unittest
from commons.log import loggers
from interfaces.synmanage.clone_oo_pa import Clone_oo
from interfaces.synmanage.savelink_oo_pa import Savelink_oo
from interfaces.synmanage.aimmachine_oo_pa import Aimmachine_oo
from interfaces.synmanage.done_oo_pa import Done_oo
from interfaces.synmanage.start_oo_pa import Start_oo
from interfaces.synmanage.others_oo_pa import Others_oo
from interfaces.synmanage.quetaskname_oo_pa import Quetaskname_oo


class Syncmanage_oo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        loggers.info("开始执行oracle->oracle,1对1,非多目标端，实时任务".center(60,"-"))

    def test_1_quetaskname_oo(self):
        """创建同步任务时相关查询接口"""

        """ # 查询任务名称是否重复  validateServiceNameInfo"""
        save = Quetaskname_oo()
        save.validateServiceNameInfo_oo()
        time.sleep(0.2)

        """ # 查询 isalarm"""
        save.isalarm_oo()
        time.sleep(0.2)

        """# 查询getAlarmMessage"""
        save.getAlarmMessage_oo()
        time.sleep(0.2)

        """ # 查询getAllUserAndFlowRelation"""
        save.getAllUserAndFlowRelation_oo()
        time.sleep(0.2)

    def test_2_savelink_oo(self):
        """选择链路-选择源端主机"""

        """# 保存选择链路相关内容 saveRelMloderDetailValue"""
        save = Savelink_oo()
        save.saveRelMloderDetailValue_oo()
        time.sleep(0.2)

        """# 保存创建任务页面相关内容 saveModuleEngineFlowInfo"""
        save.saveModuleEngineFlowInfo_oo()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.saveFlowLogInfo_oo()
        time.sleep(0.2)

        """# 再次保存 saveRelMloderDetailValue"""
        save.saveRelMloderDetailValuepa0_oo()
        time.sleep(0.2)

        """ # 将源端路径放入txt"""
        save.writepath_oo_s()
        time.sleep(0.2)

        """#  保存源端主机相关信息1（默认路径） publicSaveFlowMacConfigureInfo"""
        save.publicSaveFlowMacConfigureInfo_oo()
        time.sleep(0.2)

        """# 再次保存log saveFlowLogInfo"""
        save.saveFlowLogInfoagain_oo()
        time.sleep(0.2)

        """# 保存 publicSaveFlowMacConfigureInfo"""
        save.publicSaveFlowMacConfigureInfo1_om()
        time.sleep(0.5)

        """ # 保存 publicSaveEngineModuleDataBaseID"""
        save.publicSaveEngineModuleDataBaseID_oo()
        time.sleep(0.2)

        """ # 保存 publicSaveFlowConfigureInfo"""
        save.publicSaveFlowConfigureInfo2_oo()
        time.sleep(0.2)

        """# 再次保存 saveModuleEngineFlowInfo"""
        save.saveModuleEngineFlowInfoagain_oo()
        time.sleep(0.2)

    def test_3_aimmachine_oo(self):
        """设置目标端主机"""

        """# 将目标端路径存入txt"""
        save = Aimmachine_oo()
        save.writepath_oo_d()
        time.sleep(0.2)

        """ # 保存目标端 publicSaveFlowMacConfigureInfo"""
        save.des_publicSaveConfigureInfo_oo()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.des_saveFlowLogInfo_oo()
        time.sleep(0.2)

        """# 再次保存 publicSaveFlowMacConfigureInfo"""
        save.des_saveMacConfigureInfo_oo()
        time.sleep(0.2)

        """# 保存 publicSaveEngineModuleDataBaseID"""
        save.des_publicDataBaseID_oo()
        time.sleep(0.2)

        """# 保存 publicSaveFlowConfigureInfo"""
        save.des_SaveFlowConfigureInfo_oo()
        time.sleep(0.2)

        """ # 保存 saveModuleEngineFlowInfo"""
        save.des_ModuleEngineFlowInfo_oo()
        time.sleep(0.2)

    def test_4_done_oo(self):
        """完成及以后的接口"""

        """# 点击完成 saveEngineModuleDetailsConfInfoNoFile"""
        save = Done_oo()
        save.saveConfInfoNoFile_oo()
        time.sleep(0.2)

        """# 开始执行 startAuto"""
        save.startAuto_oo()
        time.sleep(0.2)

        """# 检查 totalCheck(需要在case中执行，否则报错)"""
        save.totalCheck_oo()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.done_saveFlowLogInfo_oo()
        time.sleep(0.2)

        """ # 保存 saveModuleEngineFlowInfo"""
        save.done_saveModuleEngineFlowInfo_oo()
        time.sleep(0.2)

        """# 查询源端 getEngineModuleDetailsConfInfo"""
        save.done_getEngineModuleDetailsConfInfo_oo()
        time.sleep(0.2)

        """# 查询源端 readEngineModuleDetailsConfInfo"""
        save.done_readModuleDetailsConfInfo_oo()
        time.sleep(0.2)

        """# 获取 getEngineModuleDetailsConfInfo(目标端)"""
        save.done_getEngineModuleDetailsConfInfo1_oo()
        time.sleep(0.2)

        """# 读取 readEngineModuleDetailsConfInfo(目标端)"""
        save.readEngineModuleDetailsConfInfo1_oo()
        time.sleep(0.2)

        """ # 获取文件名称 getFileNameByDbType"""
        save.done_getFileNameByDbType_oo()
        time.sleep(0.2)

    def test_5_start_oo(self):
        """点击启动及以后的接口"""

        """# getModuleInfomationByFlowIDpa"""
        save = Start_oo()
        save.getModuleInfomationByFlowID_oo()
        time.sleep(0.2)

        """# 源端execCommand,需在case中执行，单独执行失败"""
        save.done_execCommand_oo()
        time.sleep(0.2)

        """# 查询 getModuelOperationInfomation"""
        save.done_getOperationInfomation_oo()
        time.sleep(0.2)

        """# 保存log saveFlowLogInfo"""
        save.done_saveFlowLogInfo_oo()
        time.sleep(0.2)

        """# 再次执行 execCommand（目标端）"""
        save.done_execCommand1_oo()
        time.sleep(0.2)

        """# getModuelOperationInfomation（目标端）"""
        save.getModuelOperationInfomation1_oo()
        time.sleep(0.2)

        """# 目标端启动日志 saveFlowLogInfo"""
        save.saveFlowLogInfo1_oo()
        time.sleep(0.2)

        """# 判断是否启动成功  getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID1_oo()
        time.sleep(0.2)

    def test_6_others_oo(self):
        """运行，停止运行，删除"""

        """# 运行 runningEngineModuleToRemotrHost"""
        save = Others_oo()
        save.runningEngineModule_oo()
        time.sleep(0.2)

        """ # 获取运行后的状态信息判断是否运行成功 getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID_oo()
        time.sleep(0.2)

        """# 保存日志 saveFlowLogInfo"""
        save.run_saveFlowLogInfo_oo()
        time.sleep(0.2)

        """ # 停止运行源端  execCommand(需要放到case中)"""
        save.stop_execCommand_s_oo()
        time.sleep(0.2)

        """ # 停止运行（目标端） execCommand(需要放到case中)"""
        save.stop_execCommand_d_oo()
        time.sleep(0.2)

        """# 获取停止后的状态信息判断是否停止成功 getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID1_oo()
        time.sleep(0.2)

        """-------------------克隆相关内容--------------------"""

        """检查名称是否重复 flowsClone"""
        cl = Clone_oo()
        cl.clonePreCheck_oo()
        time.sleep(0.2)

        """克隆流 flowsClone """
        cl.flowsClone_oo()
        time.sleep(0.2)

        """ # 获取克隆进程  getCloneProgress"""
        cl.getCloneProgress_oo()
        time.sleep(0.2)

        """删除克隆的任务 deleteModuleEngineFlowInfo"""
        cl.deleteModuleEngine_oo()
        time.sleep(0.2)

        """ # 删除任务 deleteModuleEngineFlowInfo"""
        save.deletflowinfo_oo()
        time.sleep(0.2)


    @classmethod
    def tearDownClass(cls) -> None:
        loggers.info("oracle->mysql,1对1,非多目标端，实时任务执行结束".center(60,"-"))




if __name__ == "__main__":
    s = Syncmanage_oo()
    s.test_1_quetaskname_oo()