# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

from commons.log import loggers
from commons.fileopera import Fileopera
from commons.config import ip71,user71,pwd71
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Savelink_om(Publicmethods):

    """
         oracle-mysql，一对一，不开启分离
        实现：选择链路-选择源端主机
    """
    def __init__(self):
        super(Savelink_om, self).__init__()
        self.taskname,self.follow_id = Fileopera().readfilepa()

    # 保存选择链路相关内容 saveRelMloderDetailValue
    def saveRelMloderDetailValue_om(self):

        jsonstring = r'[{"link_type":"","source_db_name":"orcl","mapValue":"{\"source\":{\"activeIndex\":4,\"name\":\"LINUX_ORACLE\",\"version\":\"\",\"db_id\":1573,\"db_type\":\"oracle\",\"versionObj\":{\"dbType\":\"oracle\",\"id\":\"\",\"imgName\":\"oracle\",\"engineTypeCode\":100,\"name\":\"源端组件\"},\"datasourceObj\":{\"db_type\":\"oracle\",\"host_ip\":\"10.0.0.71\",\"host_port\":\"1521\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1573,\"db_name\":\"orcl\",\"postgreSQL\":null,\"db_passwd\":\"dsg\",\"db2\":null,\"createTime\":\"2022-01-05 11:12:59\",\"db_user\":\"dsg\",\"link_flag\":\"SID\",\"asm_oracle_home\":\"/u01/app/oracle/product/11.2.0\",\"db_alias_name\":\"71ora\"},\"Ip\":\"\"},\"target\":{\"activeIndex\":1,\"name\":\"MYSQL\",\"version\":\"31\",\"db_id\":1659,\"db_type\":\"mysql\",\"versionObj\":{\"gid\":\"1\",\"level\":2,\"onlyOne\":false,\"engineType\":100,\"engineTypeCode\":201,\"version\":\"5.1+\",\"tid\":\"10,12\",\"imgName\":\"mysql\",\"hideFlag\":false,\"name\":\"目标端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"31\"},\"datasourceObj\":{\"db_type\":\"mysql\",\"host_ip\":\"10.0.0.84\",\"host_port\":\"3306\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1659,\"db_name\":\"gxds\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-03-01 17:51:13\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"84-mysql\"},\"Ip\":\"\"},\"sourceTable\":[{\"engineVersion\":10,\"tableType\":\"CESHI\",\"create_time\":1642082520000,\"id\":4,\"engineName\":\"USERS\",\"talbeRows\":8,\"tableName\":\"QQQ\",\"username\":\"CESHI\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"targetTable\":[{\"edit\":false,\"edit_prefix\":false,\"index\":0,\"indexPrefix\":\"\",\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1648172555000,\"id\":1,\"engineName\":\"InnoDB\",\"talbeRows\":\"452200\",\"tableName\":\"tab1\",\"isSeluser\":true,\"username\":\"duyu\"}],\"tableData_center\":[{\"engineVersion\":10,\"tableType\":\"CESHI\",\"create_time\":1642082520000,\"id\":4,\"engineName\":\"USERS\",\"talbeRows\":8,\"tableName\":\"QQQ\",\"username\":\"CESHI\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"mappingData\":{\"engineID\":\"\",\"moduleID\":1,\"engineTypeCode\":100,\"etypest\":100,\"etypett\":201,\"valueString\":\"{\\\"search_sql\\\":[],\\\"vagent_mapping\\\":[{\\\"sourceown\\\":\\\"CESHI\\\",\\\"targetown\\\":\\\"duyu\\\",\\\"centerOwn\\\":\\\"\\\",\\\"tableName\\\":[{\\\"st\\\":\\\"QQQ\\\",\\\"tt\\\":\\\"tab1\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2}],\\\"addLType\\\":2,\\\"type\\\":\\\"\\\",\\\"selType\\\":\\\"drag\\\"}],\\\"vagent_location\\\":{\\\"users\\\":[[\\\"CESHI\\\"],[\\\"duyu\\\"],[\\\"CESHI\\\"],[\\\"duyu\\\"],[],[],[],[]],\\\"tables\\\":{\\\"0,CESHI\\\":[\\\"QQQ\\\"],\\\"1,duyu\\\":[\\\"tab1\\\"],\\\"2,CESHI\\\":[\\\"QQQ\\\"],\\\"3,duyu\\\":[\\\"tab1\\\"]}},\\\"vagent_location_line\\\":[\\\"0,1,CESHI,QQQ==1,1,duyu,tab1\\\",\\\"2,1,CESHI,QQQ==3,1,duyu,tab1\\\"],\\\"srcModuleID\\\":1,\\\"tarModuleID\\\":2,\\\"src_datasource_id\\\":1573,\\\"target_datasource_id\\\":1659}\"}}","source_host_ip":"10.0.0.71","target_db_name":"gxds","target_type":"mysql","source_type":"oracle","target_host_ip":"10.0.0.84","linkName":"autotest1o_m","timeIndex":1653573960377,"target":{"activeIndex":1,"name":"MYSQL","version":"31","db_id":1659,"db_type":"mysql","versionObj":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31"},"datasourceObj":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"Ip":""},"source":{"activeIndex":4,"name":"LINUX_ORACLE","version":"","db_id":1573,"db_type":"oracle","versionObj":{"dbType":"oracle","id":"","imgName":"oracle","engineTypeCode":100,"name":"源端组件"},"datasourceObj":{"db_type":"oracle","host_ip":"10.0.0.71","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora"},"Ip":""},"sourceTable":[{"engineVersion":10,"tableType":"CESHI","create_time":1642082520000,"id":4,"engineName":"USERS","talbeRows":8,"tableName":"QQQ","username":"CESHI","addLType":2,"edit":false,"index":0,"src_type":1}],"targetTable":[{"edit":false,"edit_prefix":false,"index":0,"indexPrefix":"","engineVersion":"10","tableType":"BASE TABLE","create_time":1648172555000,"id":1,"engineName":"InnoDB","talbeRows":"452200","tableName":"tab1","isSeluser":true,"username":"duyu"}],"tableIndex":0,"status":"green"}]'
        params = {
                "flowID" : self.follow_id,
                "jsonString" : jsonstring,
                "tokenID" : self.token
        }
        try:
            # 获取response
            code,newres = Taskpublicmethods().saveRelMloderDetailValue(datas=params)
            # 获取状态码和dataInfo
            datainfo = newres["dataInfo"]
            """
                判断是否保存成功
            """
            if code == 200 and datainfo == True:
                loggers.info("savelink_om_pa.saveRelMloderDetailValue_om执行成功".center(60,"~"))
            else:
                loggers.info("savelink_om_pa.saveRelMloderDetailValue_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_om_pa.saveRelMloderDetailValue_om执行异常,请检查".center(60,"@"))

    # 保存创建任务页面相关内容 saveModuleEngineFlowInfo
    def saveModuleEngineFlowInfo_om(self):
        modeldatas = '[{"istiming":0,"msg":{"dbType":"oracle","id":"","imgName":"oracle","engineTypeCode":100,"name":"源端组件","linkName":"autotest1o_m","show":{"base":1,"mapping":1,"ddl":1}},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"10.0.0.71","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora"},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"duyu","show":{"base":1,"yloader":1,"txad":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
                "modelLines" : '[{"endOrderId":2,"endId":"31","startId":"","startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
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
                loggers.info("savelink_om_pa.saveModuleEngineFlowInfo_om执行成功".center(60,"~"))
            else:
                loggers.info("savelink_om_pa.saveModuleEngineFlowInfo_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_om_pa.saveModuleEngineFlowInfo_om执行异常,请检查".center(60,"@"))

    # 保存log saveFlowLogInfo
    def saveFlowLogInfo_om(self):
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
                loggers.info("savelink_om_pa.saveFlowLogInfo_om执行成功".center(60, "~"))
            else:
                loggers.info("savelink_om_pa.saveFlowLogInfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_om_pa.saveFlowLogInfo_om执行异常,请检查".center(60, "@"))

    # 再次保存 saveRelMloderDetailValue
    def saveRelMloderDetailValuepa0_om(self):
        jsonstring = r'[{"link_type":"","source_db_name":"orcl","mapValue":"{\"source\":{\"activeIndex\":4,\"name\":\"LINUX_ORACLE\",\"version\":\"\",\"db_id\":1573,\"db_type\":\"oracle\",\"versionObj\":{\"dbType\":\"oracle\",\"id\":\"\",\"imgName\":\"oracle\",\"engineTypeCode\":100,\"name\":\"源端组件\"},\"datasourceObj\":{\"db_type\":\"oracle\",\"host_ip\":\"10.0.0.71\",\"host_port\":\"1521\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1573,\"db_name\":\"orcl\",\"postgreSQL\":null,\"db_passwd\":\"dsg\",\"db2\":null,\"createTime\":\"2022-01-05 11:12:59\",\"db_user\":\"dsg\",\"link_flag\":\"SID\",\"asm_oracle_home\":\"/u01/app/oracle/product/11.2.0\",\"db_alias_name\":\"71ora\"},\"Ip\":\"\"},\"target\":{\"activeIndex\":1,\"name\":\"MYSQL\",\"version\":\"31\",\"db_id\":1659,\"db_type\":\"mysql\",\"versionObj\":{\"gid\":\"1\",\"level\":2,\"onlyOne\":false,\"engineType\":100,\"engineTypeCode\":201,\"version\":\"5.1+\",\"tid\":\"10,12\",\"imgName\":\"mysql\",\"hideFlag\":false,\"name\":\"目标端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"31\"},\"datasourceObj\":{\"db_type\":\"mysql\",\"host_ip\":\"10.0.0.84\",\"host_port\":\"3306\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1659,\"db_name\":\"gxds\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-03-01 17:51:13\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"84-mysql\"},\"Ip\":\"\"},\"sourceTable\":[{\"engineVersion\":10,\"tableType\":\"CESHI\",\"create_time\":1642082520000,\"id\":4,\"engineName\":\"USERS\",\"talbeRows\":8,\"tableName\":\"QQQ\",\"username\":\"CESHI\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"targetTable\":[{\"edit\":false,\"edit_prefix\":false,\"index\":0,\"indexPrefix\":\"\",\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1648172555000,\"id\":1,\"engineName\":\"InnoDB\",\"talbeRows\":\"452200\",\"tableName\":\"tab1\",\"isSeluser\":true,\"username\":\"duyu\"}],\"tableData_center\":[{\"engineVersion\":10,\"tableType\":\"CESHI\",\"create_time\":1642082520000,\"id\":4,\"engineName\":\"USERS\",\"talbeRows\":8,\"tableName\":\"QQQ\",\"username\":\"CESHI\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1}],\"mappingData\":{\"engineID\":\"\",\"moduleID\":1,\"engineTypeCode\":100,\"etypest\":100,\"etypett\":201,\"valueString\":\"{\\\"search_sql\\\":[],\\\"vagent_mapping\\\":[{\\\"sourceown\\\":\\\"CESHI\\\",\\\"targetown\\\":\\\"duyu\\\",\\\"centerOwn\\\":\\\"\\\",\\\"tableName\\\":[{\\\"st\\\":\\\"QQQ\\\",\\\"tt\\\":\\\"tab1\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2}],\\\"addLType\\\":2,\\\"type\\\":\\\"\\\",\\\"selType\\\":\\\"drag\\\"}],\\\"vagent_location\\\":{\\\"users\\\":[[\\\"CESHI\\\"],[\\\"duyu\\\"],[\\\"CESHI\\\"],[\\\"duyu\\\"],[],[],[],[]],\\\"tables\\\":{\\\"0,CESHI\\\":[\\\"QQQ\\\"],\\\"1,duyu\\\":[\\\"tab1\\\"],\\\"2,CESHI\\\":[\\\"QQQ\\\"],\\\"3,duyu\\\":[\\\"tab1\\\"]}},\\\"vagent_location_line\\\":[\\\"0,1,CESHI,QQQ==1,1,duyu,tab1\\\",\\\"2,1,CESHI,QQQ==3,1,duyu,tab1\\\"],\\\"srcModuleID\\\":1,\\\"tarModuleID\\\":2,\\\"src_datasource_id\\\":1573,\\\"target_datasource_id\\\":1659}\"}}","source_host_ip":"10.0.0.71","target_db_name":"gxds","target_type":"mysql","source_type":"oracle","target_host_ip":"10.0.0.84","linkName":"autotest1o_m","timeIndex":1653573960377,"target":{"activeIndex":1,"name":"MYSQL","version":"31","db_id":1659,"db_type":"mysql","versionObj":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31"},"datasourceObj":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"Ip":""},"source":{"activeIndex":4,"name":"LINUX_ORACLE","version":"","db_id":1573,"db_type":"oracle","versionObj":{"dbType":"oracle","id":"","imgName":"oracle","engineTypeCode":100,"name":"源端组件"},"datasourceObj":{"db_type":"oracle","host_ip":"10.0.0.71","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora"},"Ip":""},"sourceTable":[{"engineVersion":10,"tableType":"CESHI","create_time":1642082520000,"id":4,"engineName":"USERS","talbeRows":8,"tableName":"QQQ","username":"CESHI","addLType":2,"edit":false,"index":0,"src_type":1}],"targetTable":[{"edit":false,"edit_prefix":false,"index":0,"indexPrefix":"","engineVersion":"10","tableType":"BASE TABLE","create_time":1648172555000,"id":1,"engineName":"InnoDB","talbeRows":"452200","tableName":"tab1","isSeluser":true,"username":"duyu"}],"tableIndex":0,"status":"green"}]'
        params = {
                "flowID" : self.follow_id,
                "jsonString" : jsonstring,
                "tokenID" : self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveRelMloderDetailValue(datas=params)
            if codes == 200:
                loggers.info("savelink_om_pa.saveRelMloderDetailValuepa0_om执行成功".center(60, "~"))
            else:
                loggers.info("savelink_om_pa.saveRelMloderDetailValuepa0_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_om_pa.saveRelMloderDetailValuepa0_om执行异常，请检查".center(60, "@"))

    # 查询路径 getDefaultPathByMacID,返回路径供其它接口使用
    def getDefaultPathByMacID_om_s(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "20",
                "engineType" : "ds",
                "serviceName" : self.taskname,
                "isContainYloader" : "false",
                "macID" : "1011",
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
            loggers.info("savelink_om_pa.getDefaultPathByMacID_om_s执行异常，请检查".center(60, "@"))

    # 将路径放入txt
    def writepath_om_s(self):
        try:
            pathes = "/dataxone218/data/om_yuanduanpath.txt"
            # 获取packagename,packagepath,installpath
            packagename, packagepath, installpath = self.getDefaultPathByMacID_om_s()
            content = str(packagename + "," + packagepath + "," + installpath)
            Fileopera().writefilepa1(contents=content,path=pathes)
            print("写入源端:", packagename)
            print("写入源端:", packagepath)
            print("写入源端:", installpath)
        except Exception as e:
            loggers.info("savelink_om_pa.writepath_om_s写入文件异常".center(60,"@"))

    #   保存源端主机相关信息1（默认路径） publicSaveFlowMacConfigureInfo
    def publicSaveFlowMacConfigureInfo_om(self):
        # 获取相关路径
        pathes = "/dataxone218/data/om_yuanduanpath.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)
        params = {
                "packageName" : packagename,
                "packagePath" : packagepath,
                "engineID" : "20",
                "passWord" : pwd71,
                "hostName" : ip71,
                "path" : "",
                "port" : "22",
                "loginType" : "password",
                "ip": ip71,
                "linkMode": "ssh",
                "hostID": "1011",
                "userName": user71,
                "osName": "Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux",
                "flowID": self.follow_id,
                "moduleID": "1",
                "tokenID": self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            message = newres["dataInfo"][0]["message"]
            if codes == 200 and message == "sucess":
                loggers.info("savelink_om_pa.publicSaveFlowMacConfigureInfo_om执行成功".center(60,"~"))
            else:
                loggers.info("savelink_om_pa.publicSaveFlowMacConfigureInfo_om执行失败".center(60,"！"))
        except Exception as e:
            loggers.info("savelink_om_pa.publicSaveFlowMacConfigureInfo_om执行异常,请检查".center(60,"@"))

    # 再次保存log saveFlowLogInfo
    def saveFlowLogInfoagain_om(self):
        params = {
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName" : self.taskname,
                "operInfo" : "源端基础配置保存成功，ip地址："+ip71+"，安装目录：",
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and "success" in message:
                loggers.info("savelink_om_pa.saveFlowLogInfoagain_om执行成功".center(60, "~"))
            else:
                loggers.info("savelink_om_pa.saveFlowLogInfoagain_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_om_pa.saveFlowLogInfoagain_om执行异常，请检查".center(60, "@"))

    # 保存 publicSaveFlowMacConfigureInfo
    def publicSaveFlowMacConfigureInfo1_om(self):
        # 获取相关路径
        pathes = "/dataxone218/data/om_yuanduanpath.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)

        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)
        baseconfginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","9":42750,"15":42751,"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","19":"","22":"$DBPS_HOME/config/asm.conf","23":"$DBPS_HOME/config/aoxd.ini","24":"","34":42753,"35":42752,"41":"'+ip71+'","42":"'+ip71+'","43":"22","44":"'+user71+'","45":"'+pwd71+'","46":"orcl","47":"'+ip71+'","49":1573,"50":"password","53":"71ora","1039":"127.0.0.1","1112":"'+installpath+'5"}]'
        params = {
                "flowID" : self.follow_id,
                "engineID" : "20",
                "moduleID" : 1,
                "db_id" : "1573",
                "baseConfigInfo" : baseconfginfo,
                "passWord" : pwd71,
                "hostName": ip71,
                "path": installpath,
                "port": "22",
                "loginType": "password",
                "ip": ip71,
                "linkMode": "ssh",
                "hostID": "1011",
                "userName": user71,
                "osName": "Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux",
                "packagePath": packagepath,
                "installPath": installpath,
                "packageName": packagename,
                "createStat": "true",
                "docIsExist": "false",
                "OXAD_HOST" : "127.0.0.1",
                "PORT" : "42750",
                "OXAD_PORT" : "42753",
                "AOX_PORT" : "42752",
                "dbpsdPort" : "42751",
                "TIMING_SYNC_EXPORT" : "",
                "DBPS_HOME" : installpath,
                "ASM_CONF_FILENAME" : "$DBPS_HOME/config/asm.conf",
                "XLDR_HOME" : "$DBPS_HOME/rmp",
                "AOX_CONF_FILE" : "$DBPS_HOME/config/aoxd.ini",
                "VCFS_HOME" : "$DBPS_HOME/vcfsa",
                "LD_LIBRARY_PATH" : "$DBPS_HOME/elib",
                "db_name": "orcl",
                "host_ip": ip71,
                "db_alias_name" : "71ora",
                "db_type": "oracle",
                "host_port": "1521",
                "odbc": "",
                "pdb_flag": "",
                "pdb_name": "",
                "s3_url": "",
                "asm_sid": "",
                "srcFilePath": "",
                "db_stat": "1",
                "tns_name": "",
                "postgreSQL": "",
                "db_passwd": "dsg",
                "db2": "",
                "createTime": "2022-01-05 11:12:59",
                "db_user": "dsg",
                "link_flag": "SID",
                "asm_oracle_home": "/u01/app/oracle/product/11.2.0",
                "flag": "true",
                "hostIp": ip71,
                "hostPort": "22",
                "tokenID": self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            mdsdhome = newres["dataInfo"][0]["pathInfo"]["DBPS_HOME"]
            if codes == 200 and installpath == mdsdhome:
                loggers.info("savelink_om_pa.publicSaveFlowMacConfigureInfo1_om执行成功".center(60,"~"))
            else:
                loggers.info("savelink_om_pa.publicSaveFlowMacConfigureInfo1_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_om_pa.publicSaveFlowMacConfigureInfo1_om执行异常，请检查".center(60,"@"))

    # 保存 publicSaveEngineModuleDataBaseID
    def publicSaveEngineModuleDataBaseID_om(self):
        # 获取相关路径
        pathes = "/dataxone218/data/om_yuanduanpath.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)

        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)
        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","9":42754,"15":42755,"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","19":"","22":"$DBPS_HOME/config/asm.conf","23":"$DBPS_HOME/config/aoxd.ini","24":"","34":42757,"35":42756,"41":"'+ip71+'","42":"'+ip71+'","43":"22","44":"'+user71+'","45":"'+pwd71+'","46":"orcl","47":"'+ip71+'","49":1573,"50":"password","53":"71ora","1039":"127.0.0.1","1112":"'+installpath+'"}]'
        params = {
                "flowID" : self.follow_id,
                "engineID" : "20",
                "moduleID": "1",
                "db_id": "1573",
                "baseConfigInfo": baseconfiginfo,
                "passWord": pwd71,
                "hostName": ip71,
                "path": installpath,
                "port": "22",
                "loginType" : "password",
                "ip": ip71,
                "linkMode": "ssh",
                "hostID": "1011",
                "userName": user71,
                "osName": "Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux",
                "packagePath": packagepath,
                "installPath": installpath,
                "packageName": packagename,
                "createStat": "true",
                "docIsExist": "false",
                "OXAD_HOST": "127.0.0.1",
                "PORT": "42754",
                "OXAD_PORT": "42757",
                "AOX_PORT": "42756",
                "dbpsdPort": "42755",
                "TIMING_SYNC_EXPORT": "",
                "DBPS_HOME": installpath,
                "ASM_CONF_FILENAME": "$DBPS_HOME/config/asm.conf",
                "XLDR_HOME": "$DBPS_HOME/rmp",
                "AOX_CONF_FILE": "$DBPS_HOME/config/aoxd.ini",
                "VCFS_HOME": "$DBPS_HOME/vcfsa",
                "LD_LIBRARY_PATH": "$DBPS_HOME/elib",
                "db_name": "orcl",
                "host_ip": ip71,
                "db_alias_name": "71ora",
                "db_type": "oracle",
                "host_port": "1521",
                "odbc": "",
                "pdb_flag": "",
                "pdb_name": "",
                "s3_url": "",
                "asm_sid": "",
                "srcFilePath": "",
                "db_stat": "1",
                "tns_name": "",
                "postgreSQL": "",
                "db_passwd": "dsg",
                "db2": "",
                "createTime": "2022-01-05 11:12:59",
                "db_user": "dsg",
                "link_flag": "SID",
                "asm_oracle_home": "/u01/app/oracle/product/11.2.0",
                "flag": "true",
                "hostIp": ip71,
                "hostPort": "22",
                "tokenID": self.token,
        }
        try:
            codes, newres = Taskpublicmethods().publicSaveEngineModuleDataBaseID(datas=params)
            if codes == 200:
                loggers.info("savelink_om_pa.publicSaveEngineModuleDataBaseID_om执行成功".center(60, "~"))
            else:
                loggers.info("savelink_om_pa.publicSaveEngineModuleDataBaseID_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_om_pa.publicSaveEngineModuleDataBaseID_om执行异常，请检查".center(60, "@"))

    # 保存 publicSaveFlowConfigureInfo
    def publicSaveFlowConfigureInfo2_om(self):
        # 获取相关路径
        pathes = "/dataxone218/data/om_yuanduanpath.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)

        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","9":42754,"15":42755,"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","19":"","22":"$DBPS_HOME/config/asm.conf","23":"$DBPS_HOME/config/aoxd.ini","24":"","34":42757,"35":42756,"41":"'+ip71+'","42":"'+ip71+'","43":"22","44":"'+user71+'","45":"'+pwd71+'","46":"orcl","47":"'+ip71+'","49":1573,"50":"password","53":"71ora","1039":"127.0.0.1","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "20",
            "moduleID": "1",
            "db_id": "1573",
            "baseConfigInfo": baseconfiginfo,
            "passWord": pwd71,
            "hostName": ip71,
            "path": installpath,
            "port": "22",
            "loginType": "password",
            "ip": ip71,
            "linkMode": "ssh",
            "hostID": "1011",
            "userName": user71,
            "osName": "Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux",
            "packagePath": packagepath,
            "installPath": installpath,
            "packageName": packagename,
            "createStat": "true",
            "docIsExist": "false",
            "OXAD_HOST": "127.0.0.1",
            "PORT": "42754",
            "OXAD_PORT": "42757",
            "AOX_PORT": "42756",
            "dbpsdPort": "42755",
            "TIMING_SYNC_EXPORT": "",
            "DBPS_HOME": installpath,
            "ASM_CONF_FILENAME": "$DBPS_HOME/config/asm.conf",
            "XLDR_HOME": "$DBPS_HOME/rmp",
            "AOX_CONF_FILE": "$DBPS_HOME/config/aoxd.ini",
            "VCFS_HOME": "$DBPS_HOME/vcfsa",
            "LD_LIBRARY_PATH": "$DBPS_HOME/elib",
            "db_name": "orcl",
            "host_ip": ip71,
            "db_alias_name": "71ora",
            "db_type": "oracle",
            "host_port": "1521",
            "odbc": "",
            "pdb_flag": "",
            "pdb_name": "",
            "s3_url": "",
            "asm_sid": "",
            "srcFilePath": "",
            "db_stat": "1",
            "tns_name": "",
            "postgreSQL": "",
            "db_passwd": "dsg",
            "db2": "",
            "createTime": "2022-01-05 11:12:59",
            "db_user": "dsg",
            "link_flag": "SID",
            "asm_oracle_home": "/u01/app/oracle/product/11.2.0",
            "flag": "true",
            "hostIp": ip71,
            "hostPort": "22",
            "tokenID": self.token,
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowConfigureInfo(datas=params)
            if codes == 200 :
                loggers.info("savelink_om_pa.publicSaveFlowConfigureInfo2_om执行成功".center(60,"~"))
            else:
                loggers.info("savelink_om_pa.publicSaveFlowConfigureInfo2_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_om_pa.publicSaveFlowConfigureInfo2_om执行异常".center(60,"@"))

    # 再次保存 saveModuleEngineFlowInfo
    def saveModuleEngineFlowInfoagain_om(self):
        # 获取相关路径
        pathes = "/dataxone218/data/om_yuanduanpath.txt"
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)

        print("$$$$$$$$$$$$$$$$$$$$$$", self.follow_id)
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)

        modeldatas = '[{"istiming":0,"msg":{"dbType":"oracle","id":20,"imgName":"oracle","engineTypeCode":100,"name":"源端组件","linkName":"autotest1o_m","show":{"base":1,"mapping":1,"ddl":1},"version":"11.2","details":"Linux-3.10.x86_64"},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"'+ip71+'","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora","passWord":"'+pwd71+'","hostName":"'+ip71+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip71+'","linkMode":"ssh","hostID":1011,"userName":"'+user71+'","osName":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","OXAD_HOST":"127.0.0.1","PORT":42754,"OXAD_PORT":42757,"AOX_PORT":42756,"dbpsdPort":42755,"TIMING_SYNC_EXPORT":"","DBPS_HOME":"'+installpath+'","ASM_CONF_FILENAME":"$DBPS_HOME/config/asm.conf","XLDR_HOME":"$DBPS_HOME/rmp","AOX_CONF_FILE":"$DBPS_HOME/config/aoxd.ini","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true","dbID":1573},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"duyu","show":{"base":1,"yloader":1,"txad":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
                "modelLines" : '[{"endOrderId":2,"endId":"31","startId":20,"startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
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
                loggers.info("savelink_om_pa.saveModuleEngineFlowInfoagain_om执行成功".center(60, "~"))
            else:
                loggers.info("savelink_om_pa.saveModuleEngineFlowInfoagain_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("savelink_om_pa.saveModuleEngineFlowInfoagain_om执行异常，请检查".center(60, "@"))


if __name__ == "__main__":
    s = Savelink_om()
    s.saveRelMloderDetailValue_om()
    s.saveModuleEngineFlowInfo_om()
    s.saveFlowLogInfo_om()
    s.saveRelMloderDetailValuepa0_om()
    s.writepath_om_s()
    s.publicSaveFlowMacConfigureInfo_om()
    s.saveFlowLogInfoagain_om()
    s.publicSaveFlowMacConfigureInfo1_om()
    s.publicSaveEngineModuleDataBaseID_om()
    s.publicSaveFlowConfigureInfo2_om()
    s.saveModuleEngineFlowInfoagain_om()

