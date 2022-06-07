# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

from commons.log import loggers
from commons.fileopera import Fileopera
from commons.config import ip140,user140,pwd140
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Savelink_tdtd(Publicmethods):
    """
        tdsql-tdsql，一对一，不开启分离
        实现：选择链路-选择源端主机
    """
    def __init__(self):
        super(Savelink_tdtd, self).__init__()
        # 获取taskname 和 follow_id
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 保存选择链路相关内容 saveRelMloderDetailValue
    def saveRelMloderDetail_tdtd(self):

        jsonstring = r'[{"link_type":"","source_db_name":"gsy","mapValue":"{\"source\":{\"activeIndex\":2,\"name\":\"TDSQL\",\"version\":\"103\",\"db_id\":1963,\"db_type\":\"tdsql\",\"versionObj\":{\"gid\":\"1\",\"level\":1,\"onlyOne\":false,\"engineType\":200,\"engineTypeCode\":900,\"version\":\"5.7.17-11-V2\",\"tid\":\"26\",\"imgName\":\"tdsql\",\"hideFlag\":false,\"name\":\"源端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"103\"},\"datasourceObj\":{\"db_type\":\"tdsql\",\"host_ip\":\"10.0.0.211\",\"host_port\":\"15002\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1963,\"db_name\":\"gsy\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-05-10 18:32:45\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"211-tdsql\"},\"Ip\":\"\"},\"target\":{\"activeIndex\":0,\"name\":\"TDSQL\",\"version\":\"104\",\"db_id\":1963,\"db_type\":\"tdsql\",\"versionObj\":{\"gid\":\"1\",\"level\":2,\"onlyOne\":false,\"engineType\":100,\"engineTypeCode\":901,\"version\":\"5.7.17-11-V2\",\"tid\":\"26\",\"imgName\":\"tdsql\",\"hideFlag\":false,\"name\":\"目标端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"104\"},\"datasourceObj\":{\"db_type\":\"tdsql\",\"host_ip\":\"10.0.0.211\",\"host_port\":\"15002\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1963,\"db_name\":\"gsy\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-05-10 18:32:45\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"211-tdsql\"},\"Ip\":\"\"},\"sourceTable\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1652971031000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"kkk\",\"username\":\"gtest\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"targetTable\":[{\"edit\":false,\"edit_prefix\":false,\"index\":0,\"indexPrefix\":\"\",\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1651042926000,\"id\":4,\"engineName\":\"InnoDB\",\"talbeRows\":\"0\",\"tableName\":\"customers\",\"isSeluser\":true,\"username\":\"dsg\"}],\"tableData_center\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1652971031000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"kkk\",\"username\":\"gtest\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"mappingData\":{\"engineID\":\"103\",\"moduleID\":1,\"engineTypeCode\":900,\"etypest\":900,\"etypett\":901,\"valueString\":\"{\\\"search_sql\\\":[],\\\"vagent_mapping\\\":[{\\\"sourceown\\\":\\\"gtest\\\",\\\"targetown\\\":\\\"dsg\\\",\\\"centerOwn\\\":\\\"\\\",\\\"tableName\\\":[{\\\"st\\\":\\\"kkk\\\",\\\"tt\\\":\\\"customers\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2}],\\\"addLType\\\":2,\\\"type\\\":\\\"\\\",\\\"selType\\\":\\\"drag\\\"}],\\\"vagent_location\\\":{\\\"users\\\":[[\\\"gtest\\\"],[\\\"dsg\\\"],[\\\"gtest\\\"],[\\\"dsg\\\"],[],[],[],[]],\\\"tables\\\":{\\\"0,gtest\\\":[\\\"kkk\\\"],\\\"1,dsg\\\":[\\\"customers\\\"],\\\"2,gtest\\\":[\\\"kkk\\\"],\\\"3,dsg\\\":[\\\"customers\\\"]}},\\\"vagent_location_line\\\":[\\\"0,1,gtest,kkk==1,1,dsg,customers\\\",\\\"2,1,gtest,kkk==3,1,dsg,customers\\\"],\\\"srcModuleID\\\":1,\\\"tarModuleID\\\":2,\\\"src_datasource_id\\\":1963,\\\"target_datasource_id\\\":1963}\"}}","source_host_ip":"10.0.0.211","target_db_name":"gsy","target_type":"tdsql","source_type":"tdsql","target_host_ip":"10.0.0.211","linkName":"autotest1td_td","timeIndex":1653633606738,"target":{"activeIndex":0,"name":"TDSQL","version":"104","db_id":1963,"db_type":"tdsql","versionObj":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":901,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"104"},"datasourceObj":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql"},"Ip":""},"source":{"activeIndex":2,"name":"TDSQL","version":"103","db_id":1963,"db_type":"tdsql","versionObj":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":900,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"103"},"datasourceObj":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql"},"Ip":""},"sourceTable":[{"engineVersion":"10","tableType":"BASE TABLE","create_time":1652971031000,"id":0,"engineName":"InnoDB","talbeRows":"5","tableName":"kkk","username":"gtest","addLType":2,"edit":false,"index":0,"src_type":1}],"targetTable":[{"edit":false,"edit_prefix":false,"index":0,"indexPrefix":"","engineVersion":"10","tableType":"BASE TABLE","create_time":1651042926000,"id":4,"engineName":"InnoDB","talbeRows":"0","tableName":"customers","isSeluser":true,"username":"dsg"}],"tableIndex":0,"status":"green"}]'
        params = {
            "flowID": self.follow_id,
            "jsonString": jsonstring,
            "tokenID": self.token
        }
        try:
            # 获取response
            code, newres = Taskpublicmethods().saveRelMloderDetailValue(datas=params)
            # 获取状态码和dataInfo
            datainfo = newres["dataInfo"]
            """
                判断是否保存成功
            """
            if code == 200 and datainfo == True:
                loggers.info("savelink_tdtd_pa.saveRelMloderDetail_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("savelink_tdtd_pa.saveRelMloderDetail_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.saveRelMloderDetail_tdtd执行异常,请检查".center(60, "@"))

    # 保存创建任务页面相关内容 saveModuleEngineFlowInfo
    def saveModuleEngineFlow_tdtd(self):
        modeldatas = '[{"istiming":0,"msg":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":900,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"103","linkName":"autotest1td_td","show":{"base":1,"mapping":1,"ddl":1}},"data":{},"data2":{"nowValue":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql"},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":901,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"104","KAFKA_DDL_TOPIC":"dsg","show":{"base":1,"yloader":1,"txad":1}},"data":{},"data2":{"nowValue":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
                "modelLines" : '[{"endOrderId":2,"endId":"104","startId":"103","startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
                "modelDatas" : modeldatas,
                "flowId" : self.follow_id,
                "flowName" : self.taskname,
                "flowDescribe" : self.taskname,
                "userID" : "1",
                "tokenID" : self.token
       }
        try:
            code,newres = Taskpublicmethods().saveModuleEngineFlowInfo(datas=params)
            resfollowid = newres["dataInfo"]["flowId"]
            """
                判断是否保存成功
            """
            if code == 200 and resfollowid == self.follow_id:
                loggers.info("savelink_tdtd_pa.saveModuleEngineFlow_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("savelink_tdtd_pa.saveModuleEngineFlow_tdtd执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.saveModuleEngineFlow_tdtd执行异常,请检查".center(60,"@"))

    # 保存log saveFlowLogInfo
    def saveFlowLogInfo_tdtd(self):
        operinfo = "dataxone创建了" + self.taskname + "流程"
        params = {
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName" : self.taskname,
                "operInfo" : operinfo,
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            code, newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            """
                判断log是否保存成功
            """
            if code == 200 and message == "success":
                loggers.info("savelink_tdtd_pa.saveFlowLogInfo_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("savelink_tdtd_pa.saveFlowLogInfo_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.saveFlowLogInfo_tdtd执行异常,请检查".center(60, "@"))

    # 再次保存 saveRelMloderDetailValue
    def saveRelMloderDetail0_tdtd(self):
        jsonstring = r'[{"link_type":"","source_db_name":"gsy","mapValue":"{\"source\":{\"activeIndex\":2,\"name\":\"TDSQL\",\"version\":\"103\",\"db_id\":1963,\"db_type\":\"tdsql\",\"versionObj\":{\"gid\":\"1\",\"level\":1,\"onlyOne\":false,\"engineType\":200,\"engineTypeCode\":900,\"version\":\"5.7.17-11-V2\",\"tid\":\"26\",\"imgName\":\"tdsql\",\"hideFlag\":false,\"name\":\"源端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"103\"},\"datasourceObj\":{\"db_type\":\"tdsql\",\"host_ip\":\"10.0.0.211\",\"host_port\":\"15002\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1963,\"db_name\":\"gsy\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-05-10 18:32:45\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"211-tdsql\"},\"Ip\":\"\"},\"target\":{\"activeIndex\":0,\"name\":\"TDSQL\",\"version\":\"104\",\"db_id\":1963,\"db_type\":\"tdsql\",\"versionObj\":{\"gid\":\"1\",\"level\":2,\"onlyOne\":false,\"engineType\":100,\"engineTypeCode\":901,\"version\":\"5.7.17-11-V2\",\"tid\":\"26\",\"imgName\":\"tdsql\",\"hideFlag\":false,\"name\":\"目标端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"104\"},\"datasourceObj\":{\"db_type\":\"tdsql\",\"host_ip\":\"10.0.0.211\",\"host_port\":\"15002\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1963,\"db_name\":\"gsy\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-05-10 18:32:45\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"211-tdsql\"},\"Ip\":\"\"},\"sourceTable\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1652971031000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"kkk\",\"username\":\"gtest\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"targetTable\":[{\"edit\":false,\"edit_prefix\":false,\"index\":0,\"indexPrefix\":\"\",\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1651042926000,\"id\":4,\"engineName\":\"InnoDB\",\"talbeRows\":\"0\",\"tableName\":\"customers\",\"isSeluser\":true,\"username\":\"dsg\"}],\"tableData_center\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1652971031000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"kkk\",\"username\":\"gtest\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"mappingData\":{\"engineID\":\"103\",\"moduleID\":1,\"engineTypeCode\":900,\"etypest\":900,\"etypett\":901,\"valueString\":\"{\\\"search_sql\\\":[],\\\"vagent_mapping\\\":[{\\\"sourceown\\\":\\\"gtest\\\",\\\"targetown\\\":\\\"dsg\\\",\\\"centerOwn\\\":\\\"\\\",\\\"tableName\\\":[{\\\"st\\\":\\\"kkk\\\",\\\"tt\\\":\\\"customers\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2}],\\\"addLType\\\":2,\\\"type\\\":\\\"\\\",\\\"selType\\\":\\\"drag\\\"}],\\\"vagent_location\\\":{\\\"users\\\":[[\\\"gtest\\\"],[\\\"dsg\\\"],[\\\"gtest\\\"],[\\\"dsg\\\"],[],[],[],[]],\\\"tables\\\":{\\\"0,gtest\\\":[\\\"kkk\\\"],\\\"1,dsg\\\":[\\\"customers\\\"],\\\"2,gtest\\\":[\\\"kkk\\\"],\\\"3,dsg\\\":[\\\"customers\\\"]}},\\\"vagent_location_line\\\":[\\\"0,1,gtest,kkk==1,1,dsg,customers\\\",\\\"2,1,gtest,kkk==3,1,dsg,customers\\\"],\\\"srcModuleID\\\":1,\\\"tarModuleID\\\":2,\\\"src_datasource_id\\\":1963,\\\"target_datasource_id\\\":1963}\"}}","source_host_ip":"10.0.0.211","target_db_name":"gsy","target_type":"tdsql","source_type":"tdsql","target_host_ip":"10.0.0.211","linkName":"autotest1td_td","timeIndex":1653633606738,"target":{"activeIndex":0,"name":"TDSQL","version":"104","db_id":1963,"db_type":"tdsql","versionObj":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":901,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"104"},"datasourceObj":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql"},"Ip":""},"source":{"activeIndex":2,"name":"TDSQL","version":"103","db_id":1963,"db_type":"tdsql","versionObj":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":900,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"103"},"datasourceObj":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql"},"Ip":""},"sourceTable":[{"engineVersion":"10","tableType":"BASE TABLE","create_time":1652971031000,"id":0,"engineName":"InnoDB","talbeRows":"5","tableName":"kkk","username":"gtest","addLType":2,"edit":false,"index":0,"src_type":1}],"targetTable":[{"edit":false,"edit_prefix":false,"index":0,"indexPrefix":"","engineVersion":"10","tableType":"BASE TABLE","create_time":1651042926000,"id":4,"engineName":"InnoDB","talbeRows":"0","tableName":"customers","isSeluser":true,"username":"dsg"}],"tableIndex":0,"status":"green"}]'
        params = {
                "flowID" : self.follow_id,
                "jsonString" : jsonstring,
                "tokenID" : self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveRelMloderDetailValue(datas=params)
            if codes == 200:
                loggers.info("savelink_tdtd_pa.saveRelMloderDetail0_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("savelink_tdtd_pa.saveRelMloderDetail0_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.saveRelMloderDetail0_tdtd执行异常，请检查".center(60, "@"))

    # 查询路径 getDefaultPathByMacID,返回路径供其它接口使用
    def getDefaultPathByMacID_tdtd_s(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "103",
                "engineType" : "ds",
                "serviceName" : self.taskname,
                "isContainYloader" : "false",
                "macID" : "1081",
                "path" : "",
                "tokenID" : self.token
        }
        try:
            codes, newres = Taskpublicmethods().getDefaultPathByMacID(datas=params)
            # 获取packagename，packagepath，installpath，返回
            packagename = newres["dataInfo"]["source"]["packageName"]
            packagepath = newres["dataInfo"]["source"]["packagePath"]
            installpath = newres["dataInfo"]["source"]["installPath"]
            return packagename, packagepath, installpath
        except Exception as e:
            loggers.info("savelink_tdtd_pa.getDefaultPathByMacID_tdtd_s执行异常，请检查".center(60, "@"))

    # 将源端路径放入txt
    def writepath_tdtd_s(self):
        try:
            pathes = "/dataxone218/data/tdtd_yuanduan.txt"
            # 获取packagename,packagepath,installpath
            packagename, packagepath, installpath = self.getDefaultPathByMacID_tdtd_s()
            content = str(packagename + "," + packagepath + "," + installpath)
            Fileopera().writefilepa1(contents=content,path=pathes)
            print("写入源端:",packagename)
            print("写入源端:",packagepath)
            print("写入源端:",installpath)
        except Exception as e:
            loggers.info("savelink_tdtd_pa.writepath_tdtd_s写入文件异常".center(60,"@"))

    # 保存源端主机相关信息1（默认路径） publicSaveFlowMacConfigureInfo
    def publicSaveFlowMacConf_tdtd(self):
        # 获取源端相关路径
        pathes = "/dataxone218/data/tdtd_yuanduan.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)
        params = {
                "packageName" : self.taskname,
                "packagePath" : packagepath,
                "engineID" : "103",
                "passWord" : pwd140,
                "hostName" : ip140,
                "path" : "",
                "port" : "22",
                "loginType" : "password",
                "ip": ip140,
                "linkMode": "ssh",
                "hostID": "1081",
                "userName": user140,
                "osName": "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
                "flowID": self.follow_id,
                "moduleID": "1",
                "tokenID": self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            message = newres["dataInfo"][0]["message"]
            if codes == 200 and message == "sucess":
                loggers.info("savelink_tdtd_pa.publicSaveFlowMacConf_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("savelink_tdtd_pa.publicSaveFlowMacConf_tdtd执行失败".center(60,"！"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.publicSaveFlowMacConf_tdtd执行异常,请检查".center(60,"@"))

    # 再次保存log saveFlowLogInfo
    def saveFlowLogInfoagain_tdtd(self):
        params = {
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName" : self.taskname,
                "operInfo" : "源端基础配置保存成功，ip地址："+ip140+"，安装目录：",
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and "success" in message:
                loggers.info("savelink_tdtd_pa.saveFlowLogInfoagain_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("savelink_tdtd_pa.saveFlowLogInfoagain_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.saveFlowLogInfoagain_tdtd执行异常，请检查".center(60, "@"))

    # 保存 publicSaveFlowMacConfigureInfo
    def publicSaveFlowMacConf1_tdtd(self):
        # 获取相关路径
        pathes = "/dataxone218/data/tdtd_yuanduan.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)
        baseconfginfo = '[{"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gsy","47":"10.0.0.211","49":1963,"50":"password","1005":51017,"1006":"'+installpath+'","1007":"$MDSD_HOME/elib","1112":"'+installpath+'"}]'
        params = {
                "flowID" : self.follow_id,
                "engineID" : "103",
                "moduleID" : 1,
                "db_id" : "1963",
                "baseConfigInfo" : baseconfginfo,
                "passWord" : pwd140,
                "hostName": ip140,
                "path": installpath,
                "port": "22",
                "loginType": "password",
                "ip": ip140,
                "linkMode": "ssh",
                "hostID": "1081",
                "userName": user140,
                "osName": "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
                "packagePath": packagepath,
                "installPath": installpath,
                "packageName": packagename,
                "createStat": "true",
                "docIsExist": "false",
                "MDSD_HOME" : installpath,
                "MDSD_PORT" : "51017",
                "LD_LIBRARY_PATH" : "$MDSD_HOME/elib",
                "db_name" : "gsy",
                "host_ip" : "10.0.0.211",
                "db_type" : "tdsql",
                "host_port" : "15002",
                "odbc": "",
                "pdb_flag": "",
                "pdb_name": "",
                "s3_url": "",
                "asm_sid": "",
                "srcFilePath": "",
                "db_stat": "1",
                "tns_name": "",
                "postgreSQL": "",
                "db_passwd": "Dsgdata@123",
                "db2": "",
                "createTime": "2022-05-10 18:32:45",
                "db_user": "dsg",
                "link_flag": "",
                "asm_oracle_home": "",
                "db_alias_name" : "211-tdsql",
                "flag": "true",
                "hostIp": ip140,
                "hostPort": "22",
                "tokenID": self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            mdsdhome = newres["dataInfo"][0]["pathInfo"]["MDSD_HOME"]
            if codes == 200 and installpath == mdsdhome:
                loggers.info("savelink_tdtd_pa.publicSaveFlowMacConf1_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("savelink_tdtd_pa.publicSaveFlowMacConf1_tdtd执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.publicSaveFlowMacConf1_tdtd执行异常，请检查".center(60,"@"))

    # 保存 publicSaveEngineModuleDataBaseID
    def SaveEngineDataBaseID_tdtd(self):
        # 获取相关路径
        pathes = "/dataxone218/data/tdtd_yuanduan.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)
        baseconfiginfo = '[{"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gsy","47":"10.0.0.211","49":1963,"50":"password","1005":51018,"1006":"'+installpath+'","1007":"$MDSD_HOME/elib","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "103",
            "moduleID": 1,
            "db_id": "1963",
            "baseConfigInfo": baseconfiginfo,
            "passWord": pwd140,
            "hostName": ip140,
            "path": installpath,
            "port": "22",
            "loginType": "password",
            "ip": ip140,
            "linkMode": "ssh",
            "hostID": "1081",
            "userName": user140,
            "osName": "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
            "packagePath": packagepath,
            "installPath": installpath,
            "packageName": packagename,
            "createStat": "true",
            "docIsExist": "false",
            "MDSD_HOME": installpath,
            "MDSD_PORT": "51018",
            "LD_LIBRARY_PATH": "$MDSD_HOME/elib",
            "db_name": "gsy",
            "host_ip": "10.0.0.211",
            "db_type": "tdsql",
            "host_port": "15002",
            "odbc": "",
            "pdb_flag": "",
            "pdb_name": "",
            "s3_url": "",
            "asm_sid": "",
            "srcFilePath": "",
            "db_stat": "1",
            "tns_name": "",
            "postgreSQL": "",
            "db_passwd": "Dsgdata@123",
            "db2": "",
            "createTime": "2022-05-10 18:32:45",
            "db_user": "dsg",
            "link_flag": "",
            "asm_oracle_home": "",
            "db_alias_name": "211-tdsql",
            "flag": "true",
            "hostIp": ip140,
            "hostPort": "22",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().publicSaveEngineModuleDataBaseID(datas=params)
            if codes == 200:
                loggers.info("savelink_tdtd_pa.SaveEngineDataBaseID_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("savelink_tdtd_pa.SaveEngineDataBaseID_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.SaveEngineDataBaseID_tdtd执行异常，请检查".center(60, "@"))

    # 保存 publicSaveFlowConfigureInfo
    def publicSaveFlowConfigure2_tdtd(self):
        # 获取相关路径
        pathes = "/dataxone218/data/tdtd_yuanduan.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)

        baseconfiginfo = '[{"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gsy","47":"10.0.0.211","49":1963,"50":"password","1005":51018,"1006":"'+installpath+'","1007":"$MDSD_HOME/elib","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "103",
            "moduleID": 1,
            "db_id": "1963",
            "baseConfigInfo": baseconfiginfo,
            "passWord": pwd140,
            "hostName": ip140,
            "path": installpath,
            "port": "22",
            "loginType": "password",
            "ip": ip140,
            "linkMode": "ssh",
            "hostID": "1081",
            "userName": user140,
            "osName": "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
            "packagePath": packagepath,
            "installPath": installpath,
            "packageName": packagename,
            "createStat": "true",
            "docIsExist": "false",
            "MDSD_HOME": installpath,
            "MDSD_PORT": "51018",
            "LD_LIBRARY_PATH": "$MDSD_HOME/elib",
            "db_name": "gsy",
            "host_ip": "10.0.0.211",
            "db_type": "tdsql",
            "host_port": "15002",
            "odbc": "",
            "pdb_flag": "",
            "pdb_name": "",
            "s3_url": "",
            "asm_sid": "",
            "srcFilePath": "",
            "db_stat": "1",
            "tns_name": "",
            "postgreSQL": "",
            "db_passwd": "Dsgdata@123",
            "db2": "",
            "createTime": "2022-05-10 18:32:45",
            "db_user": "dsg",
            "link_flag": "",
            "asm_oracle_home": "",
            "db_alias_name": "211-tdsql",
            "flag": "true",
            "hostIp": ip140,
            "hostPort": "22",
            "tokenID": self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowConfigureInfo(datas=params)
            if codes == 200 :
                loggers.info("savelink_tdtd_pa.publicSaveFlowConfigure2_tdtd执行成功".center(60,"~"))
            else:
                loggers.info("savelink_tdtd_pa.publicSaveFlowConfigure2_tdtd执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.publicSaveFlowConfigure2_tdtd执行异常".center(60,"@"))

    # 再次保存 saveModuleEngineFlowInfo
    def saveModuleEngineFlowagain_tdtd(self):
        # 获取相关路径
        pathes = "/dataxone218/data/tdtd_yuanduan.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("$$$$$$$$$$$$$$$$$$$$$$", self.follow_id)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)

        modeldatas = '[{"istiming":0,"msg":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":900,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"103","linkName":"autotest1td_td","show":{"base":1,"mapping":1,"ddl":1,"upload":1}},"data":{},"data2":{"nowValue":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":900,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"103","linkName":"autotest1td_td","show":{"base":1,"mapping":1,"ddl":1,"upload":1},"MDSD_HOME":"'+installpath+'","MDSD_PORT":51018,"LD_LIBRARY_PATH":"$MDSD_HOME/elib","flag":"true","dbID":1963},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":901,"version":"5.7.17-11-V2","tid":"26","imgName":"tdsql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"104","KAFKA_DDL_TOPIC":"dsg","show":{"base":1,"yloader":1,"txad":1,"upload":1}},"data":{},"data2":{"nowValue":{"db_type":"tdsql","host_ip":"10.0.0.211","host_port":"15002","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1963,"db_name":"gsy","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-05-10 18:32:45","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"211-tdsql"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
                "modelLines" : '[{"endOrderId":2,"endId":"104","startId":"103","startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
                "modelDatas" : modeldatas,
                "flowId" : self.follow_id,
                "flowName" : self.taskname,
                "flowDescribe" : self.taskname,
                "userID" : "1",
                "tokenID" : self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveModuleEngineFlowInfo(datas=params)
            flowid = newres["dataInfo"]["flowId"]
            if codes == 200 and flowid == self.follow_id:
                loggers.info("savelink_tdtd_pa.saveModuleEngineFlowagain_tdtd执行成功".center(60, "~"))
            else:
                loggers.info("savelink_tdtd_pa.saveModuleEngineFlowagain_tdtd执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_tdtd_pa.saveModuleEngineFlowagain_tdtd执行异常，请检查".center(60, "@"))



if __name__ == "__main__":
    s = Savelink_tdtd()
    # s.saveRelMloderDetail_tdtd()
    # s.saveModuleEngineFlow_tdtd()
    # s.saveFlowLogInfo_tdtd()
    # s.saveRelMloderDetail0_tdtd()
    # s.getDefaultPathByMacID_tdtd_s()
    # s.writepath_tdtd_s()
    # s.publicSaveFlowMacConf_tdtd()
    # s.saveFlowLogInfoagain_tdtd()
    # s.publicSaveFlowMacConf1_tdtd()
    # s.SaveEngineDataBaseID_tdtd()
    # s.publicSaveFlowConfigure2_tdtd()
    s.saveModuleEngineFlowagain_tdtd()