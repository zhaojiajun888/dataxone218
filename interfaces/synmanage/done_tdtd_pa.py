# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'


from commons.log import loggers
from commons.fileopera import Fileopera
from commons.config import ip140,user140,pwd140
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Done_tdtd(Publicmethods):
    """
        tdsql-tdsql，一对一，不开启分离
        承接 aimmachine_tdtd_pa
        实现：完成及以后的接口
    """
    def __init__(self):
        super(Done_tdtd, self).__init__()
        # 获取taskname和followid
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 点击完成 saveEngineModuleDetailsConfInfoNoFile
    def saveConfInfoNoFile_tdtd(self):
        valuestring = '{"search_sql":[],"vagent_mapping":[{"sourceown":"gtest","targetown":"dsg","ownindex":"","tableName":[{"st":"kkk","tt":"customers","addLType":2,"tabindex":""}],"addLType":2,"type":"","selType":"drag"}],"vagent_location":{"users":[["gtest"],["dsg"],["gtest"],["dsg"],[],[],[],[]],"tables":{"0,gtest":["kkk"],"1,dsg":["customers"],"2,gtest":["kkk"],"3,dsg":["customers"]}},"vagent_location_line":["0,1,gtest,kkk==1,1,dsg,customers","2,1,gtest,kkk==3,1,dsg,customers"],"srcModuleID":1,"tarModuleID":2,"src_datasource_id":1963,"target_datasource_id":1963}'
        params = {
            "flowID": self.follow_id,
            "engineID": "103",
            "moduleID": "1",
            "engineTypeCode": "900",
            "serviceName": self.taskname,
            "etypest": "900",
            "etypett": "901",
            "valueString": valuestring,
            "tokenID": self.token
        }
        codes, newres = Taskpublicmethods().saveConfInfoNoFile(datas=params)
        flag = newres["dataInfo"]["flag"]
        try:
            if codes == 200 and flag == True:
                loggers.info("done_tdtd_pa.saveConfInfoNoFile_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("done_tdtd_pa.saveConfInfoNoFile_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.saveConfInfoNoFile_tdtd执行异常,请检查".center(60, "@"))

    # 开始执行 startAuto
    def startAuto_tdtd(self):
        params = {
            "flowID": self.follow_id,
            "jsonString": '[{"eid":"103","moduleID":1,"isUpload":true},{"eid":"104","moduleID":3,"isUpload":true}]',
            "isRegister": "true",
            "isETL": "true",
            "etlModel": "new",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().startAuto(datas=params)
            message = newres["message"]
            if codes == 200 and "finished" in message:
                loggers.info("done_tdtd_pa.startAuto_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("done_tdtd_pa.startAuto_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.startAuto_tdtd执行一场,请检查".center(60, "@"))

    # 检查 totalCheck(需要在case中执行，否则报错)
    def totalCheck_tdtd(self):
        params = {
            "flowID": self.follow_id,
            "jsonString": '[{"eid":"103","moduleID":1,"isUpload":true},{"eid":"104","moduleID":3,"isUpload":true}]',
            "isRegister": "true",
            "isETL": "false",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().totalCheck(datas=params)
            name = newres["dataInfo"]["dataInfo"][0]["name"]
            if codes == 200 and "配置" in name:
                loggers.info("done_tdtd_pa.totalCheck_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("done_tdtd_pa.totalCheck_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.totalCheck_tdtd执行异常，请检查".center(60, "@"))

    # 保存log saveFlowLogInfo
    def done_saveFlowLog_tdtd(self):
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
                loggers.info("done_tdtd_pa.done_saveFlowLog_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("done_tdtd_pa.done_saveFlowLog_tdtd执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.done_saveFlowLog_tdtd执行异常，请检查".center(60,"@"))

    # 保存 saveModuleEngineFlowInfo
    def done_saveModuleEngineFlow_tdtd(self):
        # 获取目标端packagename,packagepath,installpath
        pathes_d = "/dataxone218/data/tdtd_mubiaoduan.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes_d)
        print("目标端:",packagename)
        print("目标端:",packagepath)
        print("目标端:",installpath)
        # 获取源端 packagename和packagepath
        pathes_s = "/dataxone218/data/tdtd_yuanduan.txt"
        packagename1, packagepath1, installpath1 = Fileopera().readfilepa1(path=pathes_s)
        print("源端:",packagename1)
        print("源端:",packagepath1)
        print("源端:",installpath1)

        modeldatas = '[{"istiming":0,"msg":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":900,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"103","linkName":"autotest1td_td","show":{"base":1,"mapping":1,"ddl":1,"upload":1}},"data":{},"data2":{"nowValue":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath1+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath1+'","installPath":"'+installpath1+'","packageName":"'+packagename1+'","createStat":"true","docIsExist":"false","gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":900,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"103","linkName":"autotest1td_td","show":{"base":1,"mapping":1,"ddl":1,"upload":1},"MDSD_HOME":"'+installpath1+'","MDSD_PORT":51018,"LD_LIBRARY_PATH":"$MDSD_HOME/elib","flag":"true","dbID":1963},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":901,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"104","KAFKA_DDL_TOPIC":"dsg","show":{"base":1,"yloader":1,"txad":1,"upload":1}},"data":{},"data2":{"nowValue":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","xagentdPort":51025,"yxadIpAddress":"127.0.0.1","yxadPort":51026,"DBPS_HOME":"'+installpath+'","XLDR_HOME":"$DBPS_HOME/rmp","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":901,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"104","KAFKA_DDL_TOPIC":"dsg","show":{"base":1,"yloader":1,"txad":1,"upload":1},"flag":"true"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
            "modelLines": '[{"endOrderId":2,"endId":"104","startId":"103","startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
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
                loggers.info("done_tdtd_pa.done_saveModuleEngineFlow_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("done_tdtd_pa.done_saveModuleEngineFlow_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.done_saveModuleEngineFlow_tdtd执行异常，请检查".center(60, "@"))

    # 查询源端 getEngineModuleDetailsConfInfo
    def done_getEngineModuleDetails_tdtd(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "103",
                "moduleID" : "1",
                "groupType" : "tdsql",
                "engineTypeCode" : "900",
                "serviceName" : self.taskname,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_tdtd_pa.done_getEngineModuleDetails_tdtd执行成功".center(69,"~"))
            else:
                loggers.info("done_tdtd_pa.done_getEngineModuleDetails_tdtd执行失败".center(69,"!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.done_getEngineModuleDetails_tdtd执行异常，请检查".center(69,"@"))

    # 查询源端 readEngineModuleDetailsConfInfo
    def done_readModuleDetails_tdtd(self):
        params = {
            "flowID": self.follow_id,
            "engineTypeCode": 900,
            "serviceName": self.taskname,
            "engineID": "103",
            "moduleID": "1",
            "uploadStatus": "1",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().readEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_tdtd_pa.done_readModuleDetails_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("done_tdtd_pa.done_readModuleDetails_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.done_readModuleDetails_tdtd执行异常，请检查".center(60, "@"))

    # 获取 getEngineModuleDetailsConfInfo(目标端)
    def done_getEngineModuleDetail1_tdtd(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "104",
                "moduleID" : "3",
                "groupType" : "tdsql",
                "engineTypeCode" : "901",
                "serviceName" : self.taskname,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_tdtd_pa.done_getEngineModuleDetail1_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("done_tdtd_pa.done_getEngineModuleDetail1_tdtd执行失败".center(60,"!"))
        except  Exception as e:
            loggers.info("done_tdtd_pa.done_getEngineModuleDetail1_tdtd执行异常，请检查".center(60,"@"))

    # 读取 readEngineModuleDetailsConfInfo(目标端)
    # 单独执行报错
    def readEngineModuleDetail1_tdtd(self):
        params = {
                "flowID" : self.follow_id,
                "engineTypeCode" : "901",
                "serviceName" : self.taskname,
                "engineID" : "104",
                "moduleID" : "3",
                "uploadStatus" : "1",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().readEngineModuleDetailsConfInfo(datas=params)
            targetdbid = newres["dataInfo"]["targetDbID"]
            if codes == 200 and targetdbid == "1963":
                loggers.info("done_tdtd_pa.readEngineModuleDetail1_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("done_tdtd_pa.readEngineModuleDetail1_tdtd执行失败".center(60,"!"))
        except:
            loggers.info("done_tdtd_pa.readEngineModuleDetail1_tdtd执行异常,请检查".center(60,"@"))

    # 获取文件名称 getFileNameByDbType
    def done_getFileNameByDbType_tdtd(self):
        params = {
                "dbType" : "tdsql",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getFileNameByDbType(datas=params)
            statflag = newres["statFlag"]
            if codes == 200 and statflag == 0:
                loggers.info("done_tdtd_pa.done_getFileNameByDbType_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("done_tdtd_pa.done_getFileNameByDbType_tdtd执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_tdtd_pa.done_getFileNameByDbType_tdtd执行异常，请检查".center(60,"@"))


if __name__ == "__main__":
    s = Done_tdtd()
    # s.saveConfInfoNoFile_tdtd()
    # s.startAuto_tdtd()
    # s.totalCheck_tdtd()
    # s.done_saveFlowLog_tdtd()
    # s.done_saveModuleEngineFlow_tdtd()
    # s.done_getEngineModuleDetails_tdtd()
    # s.done_readModuleDetails_tdtd()
    # s.done_getEngineModuleDetail1_tdtd()
    # s.readEngineModuleDetail1_tdtd()
    s.done_getFileNameByDbType_tdtd()