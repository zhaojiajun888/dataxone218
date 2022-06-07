# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'


from commons.log import loggers
from commons.fileopera import Fileopera
from commons.config import ip71,user71,pwd71
from commons.config import ip140,user140,pwd140
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Done_om(Publicmethods):
    """
        oracle-mysql，一对一，不开启分离
        承接 aimmachine_om_pa
        实现：完成及以后的接口
    """

    def __init__(self):
        super(Done_om, self).__init__()
        # 获取taskname和followid
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 点击完成 saveEngineModuleDetailsConfInfoNoFile
    def saveConfInfoNoFile_om(self):
        valuestring = '{"search_sql":[],"vagent_mapping":[{"sourceown":"CESHI","targetown":"duyu","ownindex":"","tableName":[{"st":"QQQ","tt":"tab1","addLType":2,"tabindex":""}],"addLType":2,"type":"","selType":"drag"}],"vagent_location":{"users":[["CESHI"],["duyu"],["CESHI"],["duyu"],[],[],[],[]],"tables":{"0,CESHI":["QQQ"],"1,duyu":["tab1"],"2,CESHI":["QQQ"],"3,duyu":["tab1"]}},"vagent_location_line":["0,1,CESHI,QQQ==1,1,duyu,tab1","2,1,CESHI,QQQ==3,1,duyu,tab1"],"srcModuleID":1,"tarModuleID":2,"src_datasource_id":1573,"target_datasource_id":1659}'
        params = {
            "flowID": self.follow_id,
            "engineID": "20",
            "moduleID": "1",
            "engineTypeCode": "100",
            "serviceName": self.taskname,
            "etypest": "100",
            "etypett": "201",
            "valueString": valuestring,
            "tokenID": self.token
        }
        codes, newres = Taskpublicmethods().saveConfInfoNoFile(datas=params)
        flag = newres["dataInfo"]["flag"]
        try:
            if codes == 200 and flag == True:
                loggers.info("done_om_pa.saveConfInfoNoFile_om执行成功".center(60, "~"))
            else:
                loggers.info("done_om_pa.saveConfInfoNoFile_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_om_pa.saveConfInfoNoFile_om执行异常,请检查".center(60, "@"))

    # 开始执行 startAuto
    def startAuto_om(self):
        params = {
            "flowID": self.follow_id,
            "jsonString": '[{"eid":20,"moduleID":1,"isUpload":true},{"eid":"31","moduleID":3,"isUpload":true}]',
            "isRegister": "true",
            "isETL": "true",
            "etlModel": "new",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().startAuto(datas=params)
            message = newres["message"]
            if codes == 200 and "finished" in message:
                loggers.info("done_om_pa.startAuto_om执行成功".center(60, "~"))
            else:
                loggers.info("done_om_pa.startAuto_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_om_pa.startAuto_om执行一场,请检查".center(60, "@"))

    # 检查 totalCheck(需要在case中执行，否则报错)
    def totalCheck_om(self):
        params = {
            "flowID": self.follow_id,
            "jsonString": '[{"eid":20,"moduleID":1,"isUpload":true},{"eid":"31","moduleID":3,"isUpload":true}]',
            "isRegister": "true",
            "isETL": "false",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().totalCheck(datas=params)
            name = newres["dataInfo"]["dataInfo"][0]["name"]
            if codes == 200 and "配置" in name:
                loggers.info("done_om_pa.totalCheck_om执行成功".center(60, "~"))
            else:
                loggers.info("done_om_pa.totalCheck_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_om_pa.totalCheck_om执行异常，请检查".center(60, "@"))

    # 保存log saveFlowLogInfo
    def done_saveFlowLogInfo_om(self):
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
                loggers.info("done_om_pa.done_saveFlowLogInfo_om执行成功".center(60,"~"))
            else:
                loggers.info("done_om_pa.done_saveFlowLogInfo_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_om_pa.done_saveFlowLogInfo_om执行异常，请检查".center(60,"@"))

    # 保存 saveModuleEngineFlowInfo
    def done_saveModuleEngineFlowInfo_om(self):
        # 获取目标端packagename,packagepath,installpath
        pathes_d = "/dataxone218/data/om_mubiaoduanpath.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes_d)
        print("目标端:",packagename)
        print("目标端:",packagepath)
        print("目标端:",installpath)
        # 获取源端 packagename和packagepath
        pathes_s = "/dataxone218/data/om_yuanduanpath.txt"
        packagename1, packagepath1, installpath1 = Fileopera().readfilepa1(path=pathes_s)
        print("源端:",packagename1)
        print("源端:",packagepath1)
        print("源端:",installpath1)

        modeldatas = '[{"istiming":0,"msg":{"dbType":"oracle","id":20,"imgName":"oracle","engineTypeCode":100,"name":"源端组件","linkName":"autotest1o_m","show":{"base":1,"mapping":1,"ddl":1,"upload":1},"version":"11.2","details":"Linux-3.10.x86_64"},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"'+ip71+'","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora","passWord":"'+pwd71+'","hostName":"'+ip71+'","path":"'+installpath1+'","port":"22","loginType":"password","ip":"'+ip71+'","linkMode":"ssh","hostID":1011,"userName":"'+user71+'","osName":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath1+'","installPath":"'+installpath1+'","packageName":"'+packagename1+'","createStat":"true","docIsExist":"false","OXAD_HOST":"127.0.0.1","PORT":42754,"OXAD_PORT":42757,"AOX_PORT":42756,"dbpsdPort":42755,"TIMING_SYNC_EXPORT":"","DBPS_HOME":"'+installpath1+'","ASM_CONF_FILENAME":"$DBPS_HOME/config/asm.conf","XLDR_HOME":"$DBPS_HOME/rmp","AOX_CONF_FILE":"$DBPS_HOME/config/aoxd.ini","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true","dbID":1573},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"duyu","show":{"base":1,"yloader":1,"txad":1,"upload":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","xagentdPort":50943,"yxadIpAddress":"127.0.0.1","yxadPort":50944,"DBPS_HOME":"'+installpath+'","XLDR_HOME":"$DBPS_HOME/rmp","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
            "modelLines": '[{"endOrderId":2,"endId":"31","startId":20,"startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
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
                loggers.info("done_om_pa.done_saveModuleEngineFlowInfo_om执行成功".center(60, "~"))
            else:
                loggers.info("done_om_pa.done_saveModuleEngineFlowInfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_om_pa.done_saveModuleEngineFlowInfo_om执行异常，请检查".center(60, "@"))

    # 查询源端 getEngineModuleDetailsConfInfo
    def done_getEngineModuleDetailsConfInfo_om(self):
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
                loggers.info("done_om_pa.done_getEngineModuleDetailsConfInfo_om执行成功".center(69,"~"))
            else:
                loggers.info("done_om_pa.done_getEngineModuleDetailsConfInfo_om执行失败".center(69,"!"))
        except Exception as e:
            loggers.info("done_om_pa.done_getEngineModuleDetailsConfInfo_om执行异常，请检查".center(69,"@"))

    # 查询源端 readEngineModuleDetailsConfInfo
    def done_readModuleDetailsConfInfo_om(self):
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
                loggers.info("done_om_pa.done_readModuleDetailsConfInfo_om执行成功".center(60, "~"))
            else:
                loggers.info("done_om_pa.done_readModuleDetailsConfInfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("done_om_pa.done_readModuleDetailsConfInfo_om执行异常，请检查".center(60, "@"))

    # 获取 getEngineModuleDetailsConfInfo(目标端)
    def done_getEngineModuleDetailsConfInfo1_om(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "31",
                "moduleID" : "3",
                "groupType" : "mysql",
                "engineTypeCode" : "201",
                "serviceName" : self.taskname,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_om_pa.done_getEngineModuleDetailsConfInfo1_om执行成功".center(60,"~"))
            else:
                loggers.info("done_om_pa.done_getEngineModuleDetailsConfInfo1_om执行失败".center(60,"!"))
        except  Exception as e:
            loggers.info("done_om_pa.done_getEngineModuleDetailsConfInfo1_om执行异常，请检查".center(60,"@"))

    # 读取 readEngineModuleDetailsConfInfo(目标端)
    # 单独执行报错
    def readEngineModuleDetailsConfInfo1_om(self):
        params = {
                "flowID" : self.follow_id,
                "engineTypeCode" : "201",
                "serviceName" : self.taskname,
                "engineID" : "31",
                "moduleID" : "3",
                "uploadStatus" : "1",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().readEngineModuleDetailsConfInfo(datas=params)
            targetdbid = newres["dataInfo"]["targetDbID"]
            if codes == 200 and targetdbid == "1659":
                loggers.info("done_om_pa.readEngineModuleDetailsConfInfo1_om执行成功".center(60,"~"))
            else:
                loggers.info("done_om_pa.readEngineModuleDetailsConfInfo1_om执行失败".center(60,"!"))
        except:
            loggers.info("done_om_pa.readEngineModuleDetailsConfInfo1_om执行异常,请检查".center(60,"@"))

    # 获取文件名称 getFileNameByDbType
    def done_getFileNameByDbType_om(self):
        params = {
                "dbType" : "mysql",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getFileNameByDbType(datas=params)
            statflag = newres["statFlag"]
            if codes == 200 and statflag == 0:
                loggers.info("done_om_pa.done_getFileNameByDbType_om执行成功".center(60,"~"))
            else:
                loggers.info("done_om_pa.done_getFileNameByDbType_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_om_pa.done_getFileNameByDbType_om执行异常，请检查".center(60,"@"))

if __name__ == "__main__":
    s = Done_om()
    # s.saveConfInfoNoFile_om()
    # s.startAuto_om()
    # s.totalCheck_om()
    # s.done_saveFlowLogInfo_om()
    # s.done_saveModuleEngineFlowInfo_om()
    # s.done_getEngineModuleDetailsConfInfo_om()
    # s.done_readModuleDetailsConfInfo_om()
    # s.done_getEngineModuleDetailsConfInfo1_om()
    # s.readEngineModuleDetailsConfInfo1_om()
    s.done_getFileNameByDbType_om()