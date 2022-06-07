# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'


from commons.log import loggers
from commons.fileopera import Fileopera
from commons.config import ip71,user71,pwd71
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Done_oo(Publicmethods):
    """
        oracle-oracle，一对一，不开启分离
        承接 aimmachine_oo_pa
        实现：完成及以后的接口
    """
    def __init__(self):
        super(Done_oo, self).__init__()
        # 获取taskname和followid
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 点击完成 saveEngineModuleDetailsConfInfoNoFile
    def saveConfInfoNoFile_oo(self):
        valuestring = '{"search_sql":[],"vagent_mapping":[{"sourceown":"CESHI","targetown":"AQ","ownindex":"","tableName":[{"st":"QQQ","tt":"YQ_TEST","addLType":2,"tabindex":""}],"addLType":2,"type":"","selType":"drag"}],"vagent_location":{"users":[["CESHI"],["AQ"],["CESHI"],["AQ"],[],[],[],[]],"tables":{"0,CESHI":["QQQ"],"1,AQ":["YQ_TEST"],"2,CESHI":["QQQ"],"3,AQ":["YQ_TEST"]}},"vagent_location_line":["0,1,CESHI,QQQ==1,1,AQ,YQ_TEST","2,1,CESHI,QQQ==3,1,AQ,YQ_TEST"],"srcModuleID":1,"tarModuleID":2,"src_datasource_id":1573,"target_datasource_id":1573}'
        params = {
            "flowID": self.follow_id,
            "engineID": "20",
            "moduleID": "1",
            "engineTypeCode": "100",
            "serviceName": self.taskname,
            "etypest": "100",
            "etypett": "101",
            "valueString": valuestring,
            "tokenID": self.token
        }
        codes, newres = Taskpublicmethods().saveConfInfoNoFile(datas=params)
        flag = newres["dataInfo"]["flag"]
        try:
            if codes == 200 and flag == True:
                loggers.info("done_oo_pa.saveConfInfoNoFile_oo执行成功".center(60, "~"))
            else:
                loggers.info("done_oo_pa.saveConfInfoNoFile_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_oo_pa.saveConfInfoNoFile_oo执行异常,请检查".center(60, "@"))

    # 开始执行 startAuto
    def startAuto_oo(self):
        params = {
            "flowID": self.follow_id,
            "jsonString": '[{"eid":20,"moduleID":1,"isUpload":true},{"eid":21,"moduleID":3,"isUpload":true}]',
            "isRegister": "true",
            "isETL": "true",
            "etlModel": "new",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().startAuto(datas=params)
            message = newres["message"]
            if codes == 200 and "finished" in message:
                loggers.info("done_oo_pa.startAuto_oo执行成功".center(60, "~"))
            else:
                loggers.info("done_oo_pa.startAuto_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_oo_pa.startAuto_oo执行一场,请检查".center(60, "@"))

    # 检查 totalCheck(需要在case中执行，否则报错)
    def totalCheck_oo(self):
        params = {
            "flowID": self.follow_id,
            "jsonString": '[{"eid":20,"moduleID":1,"isUpload":true},{"eid":21,"moduleID":3,"isUpload":true}]',
            "isRegister": "true",
            "isETL": "false",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().totalCheck(datas=params)
            name = newres["dataInfo"]["dataInfo"][0]["name"]
            if codes == 200 and "配置" in name:
                loggers.info("done_oo_pa.totalCheck_oo执行成功".center(60, "~"))
            else:
                loggers.info("done_oo_pa.totalCheck_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_oo_pa.totalCheck_oo执行异常，请检查".center(60, "@"))

    # 保存log saveFlowLogInfo
    def done_saveFlowLogInfo_oo(self):
        params = {
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName": self.taskname,
                "operInfo" : self.taskname+"流程校验成功",
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and message == "success":
                loggers.info("done_oo_pa.done_saveFlowLogInfo_oo执行成功".center(60,"~"))
            else:
                loggers.info("done_oo_pa.done_saveFlowLogInfo_oo执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_oo_pa.done_saveFlowLogInfo_oo执行异常，请检查".center(60,"@"))

    # 保存 saveModuleEngineFlowInfo
    def done_saveModuleEngineFlowInfo_oo(self):
        # 获取目标端packagename,packagepath,installpath
        pathes_d = "/dataxone218/data/oo_mubiaoduanpath.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes_d)
        print("目标端:",packagename)
        print("目标端:",packagepath)
        print("目标端:",installpath)
        # 获取源端 packagename和packagepath
        pathes_s = "/dataxone218/data/oo_yuanduanpath.txt"
        packagename1, packagepath1, installpath1 = Fileopera().readfilepa1(path=pathes_s)
        print("源端:",packagename1)
        print("源端:",packagepath1)
        print("源端:",installpath1)

        modeldatas = '[{"istiming":0,"msg":{"dbType":"oracle","id":20,"imgName":"oracle","engineTypeCode":100,"name":"源端组件","linkName":"autotest1o_o","show":{"base":1,"mapping":1,"ddl":1,"upload":1},"version":"11.2","details":"Linux-3.10.x86_64"},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"'+ip71+'","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora","passWord":"'+pwd71+'","hostName":"'+ip71+'","path":"'+installpath1+'","port":"22","loginType":"password","ip":"'+ip71+'","linkMode":"ssh","hostID":1011,"userName":"'+user71+'","osName":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath1+'","installPath":"'+installpath1+'","packageName":"'+packagename1+'","createStat":"true","docIsExist":"false","OXAD_HOST":"127.0.0.1","PORT":42210,"OXAD_PORT":42213,"AOX_PORT":42212,"dbpsdPort":42211,"TIMING_SYNC_EXPORT":"","DBPS_HOME":"'+installpath1+'","ASM_CONF_FILENAME":"$DBPS_HOME/config/asm.conf","XLDR_HOME":"$DBPS_HOME/rmp","AOX_CONF_FILE":"$DBPS_HOME/config/aoxd.ini","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true","dbID":1573},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"dbType":"oracle","id":21,"imgName":"oracle","engineTypeCode":101,"name":"目标端组件","KAFKA_DDL_TOPIC":"AQ","show":{"base":1,"yloader":1,"txad":1,"upload":1},"version":"11.2","details":"Linux-3.10.x86_64"},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"'+ip71+'","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora","passWord":"'+pwd71+'","hostName":"'+ip71+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip71+'","linkMode":"ssh","hostID":1011,"userName":"'+user71+'","osName":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","xagentdPort":42220,"yxadIpAddress":"127.0.0.1","yxadPort":42221,"DBPS_HOME":"'+installpath+'","XLDR_HOME":"$DBPS_HOME/rmp","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
            "modelLines": '[{"endOrderId":2,"endId":21,"startId":20,"startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
            "modelDatas": modeldatas,
            "tasktype" : "1",
            "flowId": self.follow_id,
            "flowName": self.taskname,
            "flowDescribe": self.taskname,
            "userID": "1",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveModuleEngineFlowInfo(datas=params)
            followid = newres["dataInfo"]["flowId"]
            if codes == 200 and followid == self.follow_id:
                loggers.info("done_oo_pa.done_saveModuleEngineFlowInfo_oo执行成功".center(60, "~"))
            else:
                loggers.info("done_oo_pa.done_saveModuleEngineFlowInfo_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_oo_pa.done_saveModuleEngineFlowInfo_oo执行异常，请检查".center(60, "@"))

    # 查询源端 getEngineModuleDetailsConfInfo
    def done_getEngineModuleDetailsConfInfo_oo(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "20",
                "moduleID" : "1",
                "groupType" : "oracle",
                "engineTypeCode" : "100",
                "serviceName" : self.taskname,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_oo_pa.done_getEngineModuleDetailsConfInfo_oo执行成功".center(69,"~"))
            else:
                loggers.info("done_oo_pa.done_getEngineModuleDetailsConfInfo_oo执行失败".center(69,"!"))
        except Exception as e:
            loggers.info("done_oo_pa.done_getEngineModuleDetailsConfInfo_oo执行异常，请检查".center(69,"@"))

    # 查询源端 readEngineModuleDetailsConfInfo
    def done_readModuleDetailsConfInfo_oo(self):
        params = {
            "flowID": self.follow_id,
            "engineTypeCode": 100,
            "serviceName": self.taskname,
            "engineID": "20",
            "moduleID": "1",
            "uploadStatus": "1",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().readEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_oo_pa.done_readModuleDetailsConfInfo_oo执行成功".center(60, "~"))
            else:
                loggers.info("done_oo_pa.done_readModuleDetailsConfInfo_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_oo_pa.done_readModuleDetailsConfInfo_oo执行异常，请检查".center(60, "@"))

    # 获取 getEngineModuleDetailsConfInfo(目标端)
    def done_getEngineModuleDetailsConfInfo1_oo(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "21",
                "moduleID" : "3",
                "groupType" : "oracle",
                "engineTypeCode" : "101",
                "serviceName" : self.taskname,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_oo_pa.done_getEngineModuleDetailsConfInfo1_oo执行成功".center(60,"~"))
            else:
                loggers.info("done_oo_pa.done_getEngineModuleDetailsConfInfo1_oo执行失败".center(60,"!"))
        except  Exception as e:
            loggers.info("done_oo_pa.done_getEngineModuleDetailsConfInfo1_oo执行异常，请检查".center(60,"@"))

    # 读取 readEngineModuleDetailsConfInfo(目标端)
    # 单独执行报错
    def readEngineModuleDetailsConfInfo1_oo(self):
        params = {
                "flowID" : self.follow_id,
                "engineTypeCode" : "101",
                "serviceName" : self.taskname,
                "engineID" : "21",
                "moduleID" : "3",
                "uploadStatus" : "1",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().readEngineModuleDetailsConfInfo(datas=params)
            targetdbid = newres["dataInfo"]["targetDbID"]
            if codes == 200 and targetdbid == "1573":
                loggers.info("done_oo_pa.readEngineModuleDetailsConfInfo1_oo执行成功".center(60,"~"))
            else:
                loggers.info("done_oo_pa.readEngineModuleDetailsConfInfo1_oo执行失败".center(60,"!"))
        except:
            loggers.info("done_oo_pa.readEngineModuleDetailsConfInfo1_oo执行异常,请检查".center(60,"@"))

    # 获取文件名称 getFileNameByDbType
    def done_getFileNameByDbType_oo(self):
        params = {
                "dbType" : "oracle",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getFileNameByDbType(datas=params)
            statflag = newres["statFlag"]
            if codes == 200 and statflag == 0:
                loggers.info("done_oo_pa.done_getFileNameByDbType_oo执行成功".center(60,"~"))
            else:
                loggers.info("done_oo_pa.done_getFileNameByDbType_oo执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_oo_pa.done_getFileNameByDbType_oo执行异常，请检查".center(60,"@"))





if __name__ == "__main__":
    s = Done_oo()
    # s.saveConfInfoNoFile_oo()
    # s.startAuto_oo()
    # s.totalCheck_oo()
    # s.done_saveFlowLogInfo_oo()
    # s.done_saveModuleEngineFlowInfo_oo()
    # s.done_getEngineModuleDetailsConfInfo_oo()
    # s.done_readModuleDetailsConfInfo_oo()
    # s.done_getEngineModuleDetailsConfInfo1_oo()
    # s.readEngineModuleDetailsConfInfo1_oo()
    s.done_getFileNameByDbType_oo()