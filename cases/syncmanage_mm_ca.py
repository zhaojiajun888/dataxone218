# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import time
import unittest
from commons.log import loggers
from interfaces.synmanage.clone_mm_pa import Clone_mm
from interfaces.synmanage.savelink_mm_pa import Savelink
from interfaces.synmanage.aimmachine_mm_pa import Aimmachine_mm
from interfaces.synmanage.done_mm_pa import Done_mm
from interfaces.synmanage.start_mm_pa import Start_mm
from interfaces.synmanage.others_mm_pa import Others_mm
from interfaces.synmanage.quetaskname_mm_pa import Quetask_mm


class Syncmanage_mm(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        loggers.info("开始执行mysql->mysql,1对1,非多目标端，实时任务".center(60,"-"))
        loggers.info("测试jenkins拉取代码".center(60, "-"))
    def test_1_quetaskname(self):
        """创建同步任务时相关查询接口"""

        """查询任务名称是否重复"""
        que = Quetask_mm()
        que.validateServiceNameInfo_mm()
        time.sleep(0.2)

        """查询isalarm"""
        que.isalarm_mm()
        time.sleep(0.2)

        """查询getAlarmMessage"""
        que.getAlarmMessage_mm()
        time.sleep(0.2)

        """查询getAllUserAndFlowRelation"""
        que.getUserAndFlowRelation_mm()
        time.sleep(0.2)


    def test_2_savelink(self):
        """同步管理-实时同步-创建任务-选择链路-选择源端主机"""

        """保存选择链路相关内容"""
        save = Savelink()
        save.saveRelMloderDetailValue_mm()
        time.sleep(0.2)

        """保存创建任务页面相关内容"""
        save.saveModuleEngineFlowInfo_mm()
        time.sleep(0.2)

        """保存log"""
        save.saveFlowLogInfo_mm()
        time.sleep(0.2)

        """再次保存saveRelMloderDetailValue"""
        save.saveRelMloderDetailValue0_mm()
        time.sleep(0.2)

        """queryMachineConfigureInfopa"""
        save.queryMachineConfInfo_mm()
        time.sleep(0.2)

        """将源端路径存入txt"""
        save.writepath_s()
        time.sleep(0.2)

        """publicSaveFlowMacConfigureInfopa"""
        save.publicSaveFlowMacConfInfo_mm()
        time.sleep(0.2)

        """savelogagain"""
        save.savelogagain()
        time.sleep(0.2)

        """publicSaveFlowMacConfigureInfopa"""
        save.publicSaveFlowMacConfInfo1_mm()
        time.sleep(0.2)

        """publicSaveEngineModuleDataBaseIDpa"""
        save.publicSaveEngineModuleDataID_mm()
        time.sleep(0.2)

        """publicSaveFlowConfigureInfopa"""
        save. publicSaveFlowConfInfo2_mm()
        time.sleep(0.2)

        """saveModuleEngineFlowInfoagainpa"""
        save.saveModuleEngineInfoagain_mm()
        time.sleep(0.2)


    def test_3_aimmachine(self):
        """设置目标端主机"""

        """将目标端路径存入txt"""
        save = Aimmachine_mm()
        save.writepath_d()
        time.sleep(0.2)

        """publicSaveFlowMacConfigureInfo"""
        save.des_publicSaveConfInfo_mm()
        time.sleep(0.2)

        """saveFlowLogInfo"""
        save.des_saveFlowLogInfo_mm()
        time.sleep(0.2)

        """publicSaveFlowMacConfigureInfo"""
        save.des_saveMacConfInfo_mm()
        time.sleep(0.2)

        """publicSaveEngineModuleDataBaseID"""
        save.des_publicDataBaseID_mm()
        time.sleep(0.2)

        """publicSaveFlowConfigureInfo"""
        save.des_SaveFlowConfInfo_mm()
        time.sleep(0.2)

        """saveModuleEngineFlowInfo"""
        save.des_ModuleEngineFlowInfo_mm()
        time.sleep(0.2)

    def test_4_done(self):
        """完成及以后的接口"""

        """保存操作"""
        save = Done_mm()
        save.saveConfInfoNoFile_mm()
        time.sleep(0.2)

        """开始执行"""
        save.startAuto_mm()
        time.sleep(0.2)

        """totalCheck"""
        save.totalCheck_mm()
        time.sleep(0.2)

        """saveFlowLogInfo"""
        save.done_saveFlowLogInfo_mm()
        time.sleep(0.2)

        """saveModuleEngineFlowInfo"""
        save.done_saveModuleEngineInfo_mm()
        time.sleep(0.2)

        """getEngineModuleDetailsConfInfo"""
        save.done_getEngineModuleConfInfo_mm()
        time.sleep(0.2)

        """readEngineModuleDetailsConfInfo"""
        save.done_readModuleConfInfo_mm()
        time.sleep(0.2)

        """# 获取 getEngineModuleDetailsConfInfo(目标端)"""
        save.done_getEngineModuleConfInfo1_mm()
        time.sleep(0.2)

        """ # 读取 readEngineModuleDetailsConfInfo"""
        save.readEngineModuleConfInfo1_mm()
        time.sleep(0.2)

        """getFileNameByDbType"""
        save.done_getFileNameByDbType_mm()
        time.sleep(0.2)

        """getYldCustomConfInfo"""
        save.done_getYldCustomConf_mm()
        time.sleep(0.2)

    def test_5_start(self):
        """点击启动及以后的接口"""

        """getModuleInfomationByFlowIDpa"""
        save = Start_mm()
        save.getModuleInfoByFlowID_mm()
        time.sleep(0.2)

        """execCommand"""
        save.done_execCommand_mm()
        time.sleep(0.2)

        """getModuelOperationInfomation"""
        save.done_getOperationInfo_mm()
        time.sleep(0.2)

        """saveFlowLogInfo"""
        save.done_saveFlowLogInfo_mm()
        time.sleep(0.2)

        """execCommand"""
        save.done_execCommand1_mm()
        time.sleep(0.2)

        """# getModuelOperationInfomation（目标端）"""
        save.getModuelOperaInfo1_mm()
        time.sleep(0.2)

        """# 目标端启动日志 saveFlowLogInfo"""
        save.saveFlowLogInfo1_mm()
        time.sleep(0.2)

        """ # 流程启动日志 saveFlowLogInfo"""
        save.saveFlowLogInfo2_mm()
        time.sleep(0.2)

        """# 判断是否启动成功  getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID1_mm()
        time.sleep(0.2)

    def test_6_others(self):
        """运行，停止运行，删除"""

        """# 运行 runningEngineModuleToRemotrHost"""
        save = Others_mm()
        save.runningEngineModule_mm()
        time.sleep(5)

        """ # 获取运行后的状态信息判断是否运行成功 getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID_mm()
        time.sleep(0.2)

        """ # 保存日志 saveFlowLogInfo"""
        save.run_saveFlowLogInfo_mm()
        time.sleep(0.2)

        """# 停止运行源端  execCommand(需要放到case中)"""
        save.stop_execCommand_s()
        time.sleep(0.2)

        """# 停止运行目标端  execCommand(需要放到case中)"""
        save.stop_execCommand_d()
        time.sleep(0.2)

        """# 获取停止后的状态信息判断是否停止成功 getModuleInfomationByFlowID"""
        save.getModuleInfoByFlowID1_mm()
        time.sleep(0.2)

        """-------------------克隆相关内容--------------------"""

        """检查名称是否重复 flowsClone"""
        cl = Clone_mm()
        cl.clonePreCheck_mm()
        time.sleep(0.2)

        """克隆流 flowsClone """
        cl.flowsClone_mm()
        time.sleep(0.2)

        """ # 获取克隆进程  getCloneProgress"""
        cl.getCloneProgress_mm()
        time.sleep(0.2)

        """删除克隆的任务 deleteModuleEngineFlowInfo"""
        cl.deleteModuleEngine_mm()
        time.sleep(0.2)

        """ # 删除任务 deleteModuleEngineFlowInfo"""
        save.deletflowinfo_mm()
        time.sleep(0.2)
    @classmethod
    def tearDownClass(self) -> None:
        loggers.info("mysql->mysql,1对1,非多目标端，实时任务执行结束".center(60,"-"))

if __name__ == "__main__":
    # unittest.main()
    sy = Syncmanage_mm()
    sy.test_1_quetaskname()
    sy.test_2_savelink()
    sy.test_3_savelink2()
