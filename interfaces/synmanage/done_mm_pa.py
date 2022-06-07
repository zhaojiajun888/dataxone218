# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

from commons.log import loggers
from commons.fileopera import Fileopera
from commons.config import ip140,user140,pwd140
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods



class Done_mm(Publicmethods):
    """
        mysql-mysql，一对一，不开启分离
        承接 aimmachine_mm_pa
        实现：完成及以后的接口
    """
    def __init__(self):
        super(Done_mm, self).__init__()
        # 获取taskname和followid
        self.taskname,self.follow_id = Fileopera().readfilepa()

    # 点击完成 saveEngineModuleDetailsConfInfoNoFile
    def saveConfInfoNoFile_mm(self):
        valuestring = '{"search_sql":[],"vagent_mapping":[{"sourceown":"gxds","targetown":"gxdt","ownindex":"","tableName":[{"st":"t1_m5","tt":"t1_m5","addLType":2,"tabindex":""},{"st":"t2_m5","tt":"t2_m5","addLType":2,"tabindex":""},{"st":"t3_m5","tt":"t3_m5","addLType":2,"tabindex":""}],"addLType":2,"type":"","selType":"drag"}],"vagent_location":{"users":[["gxds"],["gxdt"],["gxds"],["gxdt"],[],[],[],[]],"tables":{"0,gxds":["t1_m5","t2_m5","t3_m5"],"1,gxdt":["t1_m5","t2_m5","t3_m5"],"2,gxds":["t1_m5","t2_m5","t3_m5"],"3,gxdt":["t1_m5","t2_m5","t3_m5"]}},"vagent_location_line":["0,1,gxds,t1_m5==1,1,gxdt,t1_m5","2,1,gxds,t1_m5==3,1,gxdt,t1_m5","0,1,gxds,t2_m5==1,1,gxdt,t2_m5","2,1,gxds,t2_m5==3,1,gxdt,t2_m5","0,1,gxds,t3_m5==1,1,gxdt,t3_m5","2,1,gxds,t3_m5==3,1,gxdt,t3_m5"],"srcModuleID":1,"tarModuleID":2,"src_datasource_id":1659,"target_datasource_id":1659}'
        params = {
                "flowID" : self.follow_id,
                "engineID" : "89",
                "moduleID" : "1",
                "engineTypeCode" : "200",
                "serviceName" : self.taskname,
                "etypest" : "200",
                "etypett" : "201",
                "valueString" : valuestring,
                "tokenID" : self.token
        }
        codes,newres = Taskpublicmethods().saveConfInfoNoFile(datas=params)
        flag = newres["dataInfo"]["flag"]
        try:
            if codes == 200 and flag == True:
                loggers.info("done_mm_pa.saveConfInfoNoFile_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.saveConfInfoNoFile_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.saveConfInfoNoFile_mm执行异常,请检查".center(60,"@"))

    # 开始执行 startAuto
    def startAuto_mm(self):
        params = {
                "flowID" : self.follow_id,
                "jsonString" : '[{"eid":"89","moduleID":1,"isUpload":true},{"eid":"31","moduleID":3,"isUpload":true}]',
                "isRegister" : "true",
                "isETL" : "true",
                "etlModel" : "new",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().startAuto(datas=params)
            message = newres["message"]
            if codes == 200 and "finished" in message:
                loggers.info("done_mm_pa.startAuto_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.startAuto_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.startAuto_mm执行一场,请检查".center(60,"@"))

    # 检查 totalCheck(需要在case中执行，否则报错)
    def totalCheck_mm(self):
        params = {
                "flowID" : self.follow_id,
                "jsonString" : '[{"eid":"89","moduleID":1,"isUpload":true},{"eid":"31","moduleID":3,"isUpload":true}]',
                "isRegister" : "true",
                "isETL" : "false",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().totalCheck(datas=params)
            name = newres["dataInfo"]["dataInfo"][0]["name"]
            if codes == 200 and "配置" in name:
                loggers.info("done_mm_pa.totalCheck_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.totalCheck_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.totalCheck_mm执行异常，请检查".center(60,"@"))

    # 保存log saveFlowLogInfo
    def done_saveFlowLogInfo_mm(self):
        params = {
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName" : self.taskname,
                "operInfo" : self.taskname+"流程校验成功",
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and message == "success":
                loggers.info("done_mm_pa.done_saveFlowLogInfo_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.done_saveFlowLogInfo_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.done_saveFlowLogInfo_mm执行异常，请检查".center(60,"@"))

    # 保存 saveModuleEngineFlowInfo
    def done_saveModuleEngineInfo_mm(self):
        # 获取目标端packagename,packagepath,installpath
        pathes = "/dataxone218/data/mubiaopath.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端:",packagename)
        print("目标端:",packagepath)
        print("目标端:",installpath)
        # 获取源端 packagename和packagepath
        packagename1, packagepath1, installpath1 = Fileopera().readfilepa1()
        print("源端:",packagename1)
        print("源端:",packagepath1)
        print("源端:",installpath1)

        modeldatas = '[{"istiming":0,"msg":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":200,"version":"5.1-8.0","tid":"12","imgName":"mysql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"89","linkName":"gx-mysql-mysql-84","show":{"base":1,"mapping":1,"ddl":1,"upload":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath1+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath1+'","installPath":"'+installpath1+'","packageName":"'+packagename1+'","createStat":"true","docIsExist":"false","MDSD_HOME":"'+installpath1+'","MDSD_PORT":50313,"LD_LIBRARY_PATH":"$MDSD_HOME/elib","flag":"true","dbID":1659},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"gxdt","show":{"base":1,"yloader":1,"txad":1,"upload":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","xagentdPort":50334,"yxadIpAddress":"127.0.0.1","yxadPort":50335,"DBPS_HOME":"'+installpath+'","XLDR_HOME":"$DBPS_HOME/rmp","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"gxdt","show":{"base":1,"yloader":1,"txad":1},"flag":"true"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
                "modelLines" : '[{"endOrderId":2,"endId":"31","startId":"89","startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
                "modelDatas" : modeldatas,
                "flowId" : self.follow_id,
                "flowName" : self.taskname,
                "flowDescribe" : self.taskname,
                "userID" : "1",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().saveModuleEngineFlowInfo(datas=params)
            followid = newres["dataInfo"]["flowId"]
            if codes == 200 and followid == self.follow_id:
                loggers.info("done_mm_pa.done_saveModuleEngineInfo_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.done_saveModuleEngineInfo_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.done_saveModuleEngineInfo_mm执行异常，请检查".center(60,"@"))

    # 查询源端 getEngineModuleDetailsConfInfo
    def done_getEngineModuleConfInfo_mm(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "89",
                "moduleID" : "1",
                "groupType" : "mysql",
                "engineTypeCode" : "200",
                "serviceName" : self.taskname,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getEngineModuleDetailsConfInfo(datas=params)
            if codes == 200 :
                loggers.info("done_mm_pa.done_getEngineModuleConfInfo_mm执行成功".center(69,"~"))
            else:
                loggers.info("done_mm_pa.done_getEngineModuleConfInfo_mm执行失败".center(69,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.done_getEngineModuleConfInfo_mm执行异常，请检查".center(69,"@"))

    # 查询源端 readEngineModuleDetailsConfInfo
    def done_readModuleConfInfo_mm(self):
        params = {
                "flowID" : self.follow_id,
                "engineTypeCode" : 200,
                "serviceName" : self.taskname,
                "engineID" : "89",
                "moduleID" : "1",
                "uploadStatus" : "1",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().readEngineModuleDetailsConfInfo(datas=params)
            targetdbname = newres["dataInfo"]["targetDbName"]
            if codes == 200 and targetdbname == "gxds":
                loggers.info("done_mm_pa.done_readModuleConfInfo_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.done_readModuleConfInfo_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.done_readModuleConfInfo_mm执行异常，请检查".center(60,"@"))

    # 获取 getEngineModuleDetailsConfInfo(目标端)
    def done_getEngineModuleConfInfo1_mm(self):
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
                loggers.info("done_mm_pa.done_getEngineModuleConfInfo1_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.done_getEngineModuleConfInfo1_mm执行失败".center(60,"!"))
        except  Exception as e:
            loggers.info("done_mm_pa.done_getEngineModuleConfInfo1_mm执行异常，请检查".center(60,"@"))

    # 读取 readEngineModuleDetailsConfInfo(目标端)
    def readEngineModuleConfInfo1_mm(self):
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
                loggers.info("done_mm_pa.readEngineModuleConfInfo1_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.readEngineModuleConfInfo1_mm执行失败".center(60,"!"))
        except:
            loggers.info("done_mm_pa.readEngineModuleConfInfo1_mm执行异常,请检查".center(60,"@"))

    # 获取文件名称 getFileNameByDbType
    def done_getFileNameByDbType_mm(self):
        params = {
                "dbType" : "mysql",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getFileNameByDbType(datas=params)
            statflag = newres["statFlag"]
            if codes == 200 and statflag == 0:
                loggers.info("done_mm_pa.done_getFileNameByDbType_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.done_getFileNameByDbType_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.done_getFileNameByDbType_mm执行异常，请检查".center(60,"@"))

    # 查询 getYldCustomConfInfo
    def done_getYldCustomConf_mm(self,):

        params = {
                "flowID" : self.follow_id,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getYldCustomConfInfo(datas=params)
            if codes == 200:
                loggers.info("done_mm_pa.done_getYldCustomConf_mm执行成功".center(60,"~"))
            else:
                loggers.info("done_mm_pa.done_getYldCustomConf_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("done_mm_pa.done_getYldCustomConf_mm执行异常，请检查".center(60,"!"))



if __name__ == "__main__":
    s = Done_mm()
    # s.saveSourceDetailConfigInfopa()
    # s.saveModuleEngineFlowInfo0()
    # s.saveConfInfoNoFilepa1()
    # s.done_saveYldCustomConfInfo()
    # s.done_saveModuleEngineFlowInfo1()
    # s.saveConfInfoNoFilepa()
    # s.startAutopa()
    # s.totalCheckpa()
    # s.done_saveFlowLogInfo()
    # s.done_saveModuleEngineFlowInfo()
    # s.done_getEngineModuleDetailsConfInfo()
    # s.done_readModuleDetailsConfInfo()
    # s.done_getEngineModuleDetailsConfInfo1()
    # s.readEngineModuleDetailsConfInfo1()
    # s.done_getFileNameByDbType()
    # s.done_getYldCustomConfInfo()
