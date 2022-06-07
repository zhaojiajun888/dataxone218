# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

from commons.log import loggers
from commons.config import ip140,user140,pwd140
from commons.fileopera import Fileopera
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Savelink(Publicmethods):
    """
         mysql-mysql，一对一，不开启分离
        实现：选择链路-选择源端主机
    """
    def __init__(self):
        super(Savelink, self).__init__()
        # 获取taskname 和follow_id
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 保存选择链路相关内容 saveRelMloderDetailValue
    def saveRelMloderDetailValue_mm(self):
        jsonstring = r'[{"link_type":"","source_db_name":"gxds","mapValue":"{\"source\":{\"activeIndex\":1,\"name\":\"MYSQL\",\"version\":\"89\",\"db_id\":1659,\"db_type\":\"mysql\",\"versionObj\":{\"gid\":\"1\",\"level\":1,\"onlyOne\":false,\"engineType\":200,\"engineTypeCode\":200,\"version\":\"5.1-8.0\",\"tid\":\"12\",\"imgName\":\"mysql\",\"hideFlag\":false,\"name\":\"源端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"89\"},\"datasourceObj\":{\"db_type\":\"mysql\",\"host_ip\":\"10.0.0.84\",\"host_port\":\"3306\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1659,\"db_name\":\"gxds\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-03-01 17:51:13\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"84-mysql\"},\"Ip\":\"\"},\"target\":{\"activeIndex\":1,\"name\":\"MYSQL\",\"version\":\"31\",\"db_id\":1659,\"db_type\":\"mysql\",\"versionObj\":{\"gid\":\"1\",\"level\":2,\"onlyOne\":false,\"engineType\":100,\"engineTypeCode\":201,\"version\":\"5.1+\",\"tid\":\"10,12\",\"imgName\":\"mysql\",\"hideFlag\":false,\"name\":\"目标端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"31\"},\"datasourceObj\":{\"db_type\":\"mysql\",\"host_ip\":\"10.0.0.84\",\"host_port\":\"3306\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1659,\"db_name\":\"gxds\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-03-01 17:51:13\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"84-mysql\"},\"Ip\":\"\"},\"sourceTable\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978877000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t1_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978878000,\"id\":2,\"engineName\":\"InnoDB\",\"talbeRows\":\"7\",\"tableName\":\"t2_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":1,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978879000,\"id\":4,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t3_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":2,\"src_type\":1}],\"targetTable\":[{\"edit\":false,\"edit_prefix\":false,\"index\":0,\"indexPrefix\":\"\",\"tableName\":\"t1_m5\",\"username\":\"gxdt\"},{\"edit\":false,\"edit_prefix\":false,\"index\":1,\"indexPrefix\":\"\",\"tableName\":\"t2_m5\",\"username\":\"gxdt\"},{\"edit\":false,\"edit_prefix\":false,\"index\":2,\"indexPrefix\":\"\",\"tableName\":\"t3_m5\",\"username\":\"gxdt\"}],\"tableData_center\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978877000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t1_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978878000,\"id\":2,\"engineName\":\"InnoDB\",\"talbeRows\":\"7\",\"tableName\":\"t2_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":1,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978879000,\"id\":4,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t3_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":2,\"src_type\":1}],\"mappingData\":{\"engineID\":\"89\",\"moduleID\":1,\"engineTypeCode\":200,\"etypest\":200,\"etypett\":201,\"valueString\":\"{\\\"search_sql\\\":[],\\\"vagent_mapping\\\":[{\\\"sourceown\\\":\\\"gxds\\\",\\\"targetown\\\":\\\"gxdt\\\",\\\"centerOwn\\\":\\\"\\\",\\\"tableName\\\":[{\\\"st\\\":\\\"t1_m5\\\",\\\"tt\\\":\\\"t1_m5\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2},{\\\"st\\\":\\\"t2_m5\\\",\\\"tt\\\":\\\"t2_m5\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2},{\\\"st\\\":\\\"t3_m5\\\",\\\"tt\\\":\\\"t3_m5\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2}],\\\"addLType\\\":2,\\\"type\\\":\\\"\\\",\\\"selType\\\":\\\"drag\\\"}],\\\"vagent_location\\\":{\\\"users\\\":[[\\\"gxds\\\"],[\\\"gxdt\\\"],[\\\"gxds\\\"],[\\\"gxdt\\\"],[],[],[],[]],\\\"tables\\\":{\\\"0,gxds\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"],\\\"1,gxdt\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"],\\\"2,gxds\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"],\\\"3,gxdt\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"]}},\\\"vagent_location_line\\\":[\\\"0,1,gxds,t1_m5==1,1,gxdt,t1_m5\\\",\\\"2,1,gxds,t1_m5==3,1,gxdt,t1_m5\\\",\\\"0,1,gxds,t2_m5==1,1,gxdt,t2_m5\\\",\\\"2,1,gxds,t2_m5==3,1,gxdt,t2_m5\\\",\\\"0,1,gxds,t3_m5==1,1,gxdt,t3_m5\\\",\\\"2,1,gxds,t3_m5==3,1,gxdt,t3_m5\\\"],\\\"srcModuleID\\\":1,\\\"tarModuleID\\\":2,\\\"src_datasource_id\\\":1659,\\\"target_datasource_id\\\":1659}\"}}","source_host_ip":"10.0.0.84","target_db_name":"gxds","target_type":"mysql","source_type":"mysql","target_host_ip":"10.0.0.84","linkName":"gx-mysql-mysql-84","timeIndex":1653390348114,"target":{"activeIndex":1,"name":"MYSQL","version":"31","db_id":1659,"db_type":"mysql","versionObj":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31"},"datasourceObj":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"Ip":""},"source":{"activeIndex":1,"name":"MYSQL","version":"89","db_id":1659,"db_type":"mysql","versionObj":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":200,"version":"5.1-8.0","tid":"12","imgName":"mysql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"89"},"datasourceObj":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"Ip":""},"sourceTable":[{"engineVersion":"10","tableType":"BASE TABLE","create_time":1647978877000,"id":0,"engineName":"InnoDB","talbeRows":"5","tableName":"t1_m5","username":"gxds","addLType":2,"edit":false,"index":0,"src_type":1},{"engineVersion":"10","tableType":"BASE TABLE","create_time":1647978878000,"id":2,"engineName":"InnoDB","talbeRows":"7","tableName":"t2_m5","username":"gxds","addLType":2,"edit":false,"index":1,"src_type":1},{"engineVersion":"10","tableType":"BASE TABLE","create_time":1647978879000,"id":4,"engineName":"InnoDB","talbeRows":"5","tableName":"t3_m5","username":"gxds","addLType":2,"edit":false,"index":2,"src_type":1}],"targetTable":[{"edit":false,"edit_prefix":false,"index":0,"indexPrefix":"","tableName":"t1_m5","username":"gxdt"},{"edit":false,"edit_prefix":false,"index":1,"indexPrefix":"","tableName":"t2_m5","username":"gxdt"},{"edit":false,"edit_prefix":false,"index":2,"indexPrefix":"","tableName":"t3_m5","username":"gxdt"}],"tableIndex":0,"status":"green"}]'
        params = {
                "flowID" : self.follow_id,
                "tokenID" : self.token,
                "jsonString" : jsonstring
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
                loggers.info("savelink_mm_pa.saveRelMloderDetailValue_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.saveRelMloderDetailValue_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.saveRelMloderDetailValue_mm执行异常,请检查".center(60,"@"))

    # 保存创建任务页面相关内容 saveModuleEngineFlowInfo
    def saveModuleEngineFlowInfo_mm(self):
        params = {
                "modelLines" : '[{"endOrderId":2,"endId":"31","startId":"89","startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
                "modelDatas" : '[{"istiming":0,"msg":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":200,"version":"5.1-8.0","tid":"12","imgName":"mysql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"89","linkName":"gx-mysql-mysql-84","show":{"base":1,"mapping":1,"ddl":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"gxdt","show":{"base":1,"yloader":1,"txad":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]',
                "flowId" : self.follow_id,
                "flowName" : self.taskname,
                "flowDescribe": self.taskname,
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
                loggers.info("savelink_mm_pa.saveModuleEngineFlowInfo_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.saveModuleEngineFlowInfo_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.saveModuleEngineFlowInfo_mm执行异常,请检查".center(60,"@"))

    # 保存log saveFlowLogInfo
    def saveFlowLogInfo_mm(self):
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
            code,newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            """
                判断log是否保存成功
            """
            if code == 200 and message == "success":
                loggers.info("savelink_mm_pa.saveFlowLogInfo_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.saveFlowLogInfo_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.saveFlowLogInfo_mm执行异常,请检查".center(60,"@"))

    # 再次保存 saveRelMloderDetailValue
    def saveRelMloderDetailValue0_mm(self):

        jsonstring = r'[{"link_type":"","source_db_name":"gxds","mapValue":"{\"source\":{\"activeIndex\":1,\"name\":\"MYSQL\",\"version\":\"89\",\"db_id\":1659,\"db_type\":\"mysql\",\"versionObj\":{\"gid\":\"1\",\"level\":1,\"onlyOne\":false,\"engineType\":200,\"engineTypeCode\":200,\"version\":\"5.1-8.0\",\"tid\":\"12\",\"imgName\":\"mysql\",\"hideFlag\":false,\"name\":\"源端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"89\"},\"datasourceObj\":{\"db_type\":\"mysql\",\"host_ip\":\"10.0.0.84\",\"host_port\":\"3306\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1659,\"db_name\":\"gxds\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-03-01 17:51:13\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"84-mysql\"},\"Ip\":\"\"},\"target\":{\"activeIndex\":1,\"name\":\"MYSQL\",\"version\":\"31\",\"db_id\":1659,\"db_type\":\"mysql\",\"versionObj\":{\"gid\":\"1\",\"level\":2,\"onlyOne\":false,\"engineType\":100,\"engineTypeCode\":201,\"version\":\"5.1+\",\"tid\":\"10,12\",\"imgName\":\"mysql\",\"hideFlag\":false,\"name\":\"目标端组件\",\"javaOrC\":1,\"details\":\"Linux-2.6.x86_64\",\"id\":\"31\"},\"datasourceObj\":{\"db_type\":\"mysql\",\"host_ip\":\"10.0.0.84\",\"host_port\":\"3306\",\"odbc\":\"\",\"pdb_flag\":\"\",\"pdb_name\":\"\",\"s3_url\":\"\",\"asm_sid\":\"\",\"srcFilePath\":\"\",\"db_stat\":1,\"tns_name\":\"\",\"db_id\":1659,\"db_name\":\"gxds\",\"postgreSQL\":null,\"db_passwd\":\"Dsgdata@123\",\"db2\":null,\"createTime\":\"2022-03-01 17:51:13\",\"db_user\":\"dsg\",\"link_flag\":\"\",\"asm_oracle_home\":\"\",\"db_alias_name\":\"84-mysql\"},\"Ip\":\"\"},\"sourceTable\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978877000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t1_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978878000,\"id\":2,\"engineName\":\"InnoDB\",\"talbeRows\":\"7\",\"tableName\":\"t2_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":1,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978879000,\"id\":4,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t3_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":2,\"src_type\":1}],\"targetTable\":[{\"edit\":false,\"edit_prefix\":false,\"index\":0,\"indexPrefix\":\"\",\"tableName\":\"t1_m5\",\"username\":\"gxdt\"},{\"edit\":false,\"edit_prefix\":false,\"index\":1,\"indexPrefix\":\"\",\"tableName\":\"t2_m5\",\"username\":\"gxdt\"},{\"edit\":false,\"edit_prefix\":false,\"index\":2,\"indexPrefix\":\"\",\"tableName\":\"t3_m5\",\"username\":\"gxdt\"}],\"tableData_center\":[{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978877000,\"id\":0,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t1_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":0,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978878000,\"id\":2,\"engineName\":\"InnoDB\",\"talbeRows\":\"7\",\"tableName\":\"t2_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":1,\"src_type\":1},{\"engineVersion\":\"10\",\"tableType\":\"BASE TABLE\",\"create_time\":1647978879000,\"id\":4,\"engineName\":\"InnoDB\",\"talbeRows\":\"5\",\"tableName\":\"t3_m5\",\"username\":\"gxds\",\"addLType\":2,\"edit\":false,\"index\":2,\"src_type\":1}],\"mappingData\":{\"engineID\":\"89\",\"moduleID\":1,\"engineTypeCode\":200,\"etypest\":200,\"etypett\":201,\"valueString\":\"{\\\"search_sql\\\":[],\\\"vagent_mapping\\\":[{\\\"sourceown\\\":\\\"gxds\\\",\\\"targetown\\\":\\\"gxdt\\\",\\\"centerOwn\\\":\\\"\\\",\\\"tableName\\\":[{\\\"st\\\":\\\"t1_m5\\\",\\\"tt\\\":\\\"t1_m5\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2},{\\\"st\\\":\\\"t2_m5\\\",\\\"tt\\\":\\\"t2_m5\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2},{\\\"st\\\":\\\"t3_m5\\\",\\\"tt\\\":\\\"t3_m5\\\",\\\"ct\\\":\\\"\\\",\\\"addLType\\\":2}],\\\"addLType\\\":2,\\\"type\\\":\\\"\\\",\\\"selType\\\":\\\"drag\\\"}],\\\"vagent_location\\\":{\\\"users\\\":[[\\\"gxds\\\"],[\\\"gxdt\\\"],[\\\"gxds\\\"],[\\\"gxdt\\\"],[],[],[],[]],\\\"tables\\\":{\\\"0,gxds\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"],\\\"1,gxdt\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"],\\\"2,gxds\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"],\\\"3,gxdt\\\":[\\\"t1_m5\\\",\\\"t2_m5\\\",\\\"t3_m5\\\"]}},\\\"vagent_location_line\\\":[\\\"0,1,gxds,t1_m5==1,1,gxdt,t1_m5\\\",\\\"2,1,gxds,t1_m5==3,1,gxdt,t1_m5\\\",\\\"0,1,gxds,t2_m5==1,1,gxdt,t2_m5\\\",\\\"2,1,gxds,t2_m5==3,1,gxdt,t2_m5\\\",\\\"0,1,gxds,t3_m5==1,1,gxdt,t3_m5\\\",\\\"2,1,gxds,t3_m5==3,1,gxdt,t3_m5\\\"],\\\"srcModuleID\\\":1,\\\"tarModuleID\\\":2,\\\"src_datasource_id\\\":1659,\\\"target_datasource_id\\\":1659}\"}}","source_host_ip":"10.0.0.84","target_db_name":"gxds","target_type":"mysql","source_type":"mysql","target_host_ip":"10.0.0.84","linkName":"gx-mysql-mysql-84","timeIndex":1653390348114,"target":{"activeIndex":1,"name":"MYSQL","version":"31","db_id":1659,"db_type":"mysql","versionObj":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31"},"datasourceObj":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"Ip":""},"source":{"activeIndex":1,"name":"MYSQL","version":"89","db_id":1659,"db_type":"mysql","versionObj":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":200,"version":"5.1-8.0","tid":"12","imgName":"mysql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"89"},"datasourceObj":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"Ip":""},"sourceTable":[{"engineVersion":"10","tableType":"BASE TABLE","create_time":1647978877000,"id":0,"engineName":"InnoDB","talbeRows":"5","tableName":"t1_m5","username":"gxds","addLType":2,"edit":false,"index":0,"src_type":1},{"engineVersion":"10","tableType":"BASE TABLE","create_time":1647978878000,"id":2,"engineName":"InnoDB","talbeRows":"7","tableName":"t2_m5","username":"gxds","addLType":2,"edit":false,"index":1,"src_type":1},{"engineVersion":"10","tableType":"BASE TABLE","create_time":1647978879000,"id":4,"engineName":"InnoDB","talbeRows":"5","tableName":"t3_m5","username":"gxds","addLType":2,"edit":false,"index":2,"src_type":1}],"targetTable":[{"edit":false,"edit_prefix":false,"index":0,"indexPrefix":"","tableName":"t1_m5","username":"gxdt"},{"edit":false,"edit_prefix":false,"index":1,"indexPrefix":"","tableName":"t2_m5","username":"gxdt"},{"edit":false,"edit_prefix":false,"index":2,"indexPrefix":"","tableName":"t3_m5","username":"gxdt"}],"tableIndex":0,"status":"green"}]'
        params = {
                "flowID" : self.follow_id,
                "jsonString" : jsonstring,
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().saveRelMloderDetailValue(datas=params)
            if codes  == 200 :
                loggers.info("savelink_mm_pa.saveRelMloderDetailValue0_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.saveRelMloderDetailValue0_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.saveRelMloderDetailValue0_mm执行异常，请检查".center(60,"@"))

    # 查询源主机 queryMachineConfigureInfo
    def queryMachineConfInfo_mm(self):
        params = {
                "limit" : "10",
                "offset" : "0",
                "tokenID" : self.token,
                "hostType" : "2",
                "ip" : ip140
        }
        try:
            codes,newres = Taskpublicmethods().queryMachineConfigureInfo(datas=params)
            message = newres["message"]
            if codes == 200 and "success" in message:
                loggers.info("savelink_mm_pa.queryMachineConfInfo_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.queryMachineConfInfo_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.queryMachineConfInfo_mm执行异常，请检查".center(60,"@"))

    # 查询路径 getDefaultPathByMacID,返回路径供其它接口使用
    def getDefaultPathByMacIDpa_s(self):
        params = {
                "flowID" : self.follow_id,
                "engineID" : "89",
                "engineType" : "ds",
                "serviceName" : self.taskname,
                "isContainYloader" : "false",
                "macID" : "1081",
                "path" : "",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().getDefaultPathByMacID(datas=params)
            # 获取packagename，packagepath，installpath，返回
            packagename = newres["dataInfo"]["source"]["packageName"]
            packagepath = newres["dataInfo"]["source"]["packagePath"]
            installpath = newres["dataInfo"]["source"]["installPath"]
            return packagename,packagepath,installpath
        except Exception as e:
            loggers.info("savelink_mm_pa.getDefaultPathByMacIDpa_s执行异常，请检查".center(60,"@"))

    # 将路径放入txt
    def writepath_s(self):
        try:
            # 获取packagename,packagepath,installpath
            packagename, packagepath, installpath = self.getDefaultPathByMacIDpa_s()
            print("写入:",packagename)
            print("写入:", packagepath)
            print("写入:", installpath)
            contents = str(packagename + "," + packagepath + "," + installpath)
            Fileopera().writefilepa1(contents)
        except Exception as e:
            loggers.info("savelink_mm_pa.writepath_s写入文件异常".center(60,"@"))

    """
    保存源端主机相关信息1（默认路径） publicSaveFlowMacConfigureInfo
    """
    def publicSaveFlowMacConfInfo_mm(self):

        # txt中获取packagename,packagepath,installpath
        packagename,packagepath,installpath = Fileopera().readfilepa1()
        print("源端",packagename)
        print("源端", packagepath)
        print("源端", installpath)

        params = {
                "packageName" : packagename,
                "packagePath" : packagepath,
                "engineID" : "89",
                "passWord" : pwd140,
                "hostName" : ip140,
                "path" : "",
                "port" : "22",
                "loginType" : "password",
                "ip" : ip140,
                "linkMode" : "ssh",
                "hostID" : user140,
                "userName" : user140,
                "osName" : "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
                "flowID" : self.follow_id,
                "moduleID" : "1",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            message = newres["dataInfo"][0]["message"]
            if codes == 200 and message == "sucess":
                loggers.info("savelink_mm_pa.publicSaveFlowMacConfInfo_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.publicSaveFlowMacConfInfo_mm执行失败".center(60,"！"))
        except Exception as e:
            loggers.info("savelink_mm_pa.publicSaveFlowMacConfInfo_mm执行异常,请检查".center(60,"@"))

    # 再次保存log saveFlowLogInfo
    def savelogagain(self):
        operinfo = "源端基础配置保存成功，ip地址："+ ip140 +"，安装目录："
        params ={
                "flowID" : self.follow_id,
                "moduleID" : "",
                "serviceName" : self.taskname,
                "operInfo" : operinfo,
                "operStat" : "success",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and "success" in message:
                loggers.info("savelink_mm_pa.savelogagain执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.savelogagain执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.savelogagain执行异常，请检查".center(60,"@"))

    # 保存 publicSaveFlowMacConfigureInfo
    def publicSaveFlowMacConfInfo1_mm(self):

        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1()
        print("源端",packagename)
        print("源端", packagepath)
        print("源端", installpath)
        baseconfiginfo = '[{"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gxds","47":"10.0.0.84","49":1659,"50":"password","1005":50312,"1006":"'+installpath+'","1007":"$MDSD_HOME/elib","1112":"'+installpath+'"}]'
        params = {
                "flowID" : self.follow_id,
                "engineID" : "89",
                "moduleID" : "1",
                "db_id" : "1659",
                "baseConfigInfo" : baseconfiginfo,
                "passWord" : pwd140,
                "hostName" : ip140,
                "path" : installpath,
                "port" : "22",
                "loginType" : "password",
                "ip" : ip140,
                "linkMode" : "ssh",
                "hostID" : "1081",
                "userName" : user140,
                "osName" : "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
                "packagePath" : packagepath,
                "installPath" : installpath,
                "packageName" : packagename,
                "createStat" : "true",
                "docIsExist" : "false",
                "MDSD_HOME" : installpath,
                "MDSD_PORT" : "50312",
                "LD_LIBRARY_PATH" : "$MDSD_HOME / elib",
                "db_name" : "gxds",
                "host_ip" : "10.0.0.84",
                "db_type": "mysql",
                "host_port": "3306",
                "odbc" : "",
                "pdb_flag" : "",
                "pdb_name" : "",
                "s3_url" : "",
                "asm_sid" : "",
                "srcFilePath" : "",
                "db_stat" : "1",
                "tns_name" : "",
                "postgreSQL" : "",
                "db_passwd" : "Dsgdata@123",
                "db2" : "",
                "createTime" : "2022-03-01 17:51:13",
                "db_user" : "dsg",
                "link_flag" : "",
                "asm_oracle_home" : "",
                "db_alias_name" : "84-mysql",
                "flag" : "true",
                "hostIp" : ip140,
                "hostPort" : "22",
                "tokenID" : self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            mdsdhome = newres["dataInfo"][0]["pathInfo"]["MDSD_HOME"]
            if codes == 200 and installpath == mdsdhome:
                loggers.info("savelink_mm_pa.publicSaveFlowMacConfInfo1_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.publicSaveFlowMacConfInfo1_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.publicSaveFlowMacConfInfo1_mm执行异常，请检查".center(60,"@"))

    # 保存 publicSaveEngineModuleDataBaseID
    def publicSaveEngineModuleDataID_mm(self):
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1()
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)

        baseconfiginfo = '[{"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gxds","47":"10.0.0.84","49":1659,"50":"password","1005":50313,"1006":"'+installpath+'","1007":"$MDSD_HOME/elib","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "89",
            "moduleID": "1",
            "db_id": "1659",
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
            "MDSD_PORT": "50313",
            "LD_LIBRARY_PATH": "$MDSD_HOME / elib",
            "db_name": "gxds",
            "host_ip": "10.0.0.84",
            "db_type": "mysql",
            "host_port": "3306",
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
            "createTime": "2022-03-01 17:51:13",
            "db_user": "dsg",
            "link_flag": "",
            "asm_oracle_home": "",
            "db_alias_name": "84-mysql",
            "flag": "true",
            "hostIp": ip140,
            "hostPort": "22",
            "tokenID": self.token
        }

        try:
            codes, newres = Taskpublicmethods().publicSaveEngineModuleDataBaseID(datas=params)
            if codes == 200:
                loggers.info("savelink_mm_pa.publicSaveEngineModuleDataID_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.publicSaveEngineModuleDataID_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.publicSaveEngineModuleDataID_mm执行异常，请检查".center(60,"@"))

    # 保存 publicSaveFlowConfigureInfo
    def publicSaveFlowConfInfo2_mm(self):
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1()
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)

        baseconfiginfo = '[{"16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gxds","47":"10.0.0.84","49":1659,"50":"password","1005":50313,"1006":"'+installpath+'","1007":"$MDSD_HOME/elib","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "89",
            "moduleID": "1",
            "db_id": "1659",
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
            "MDSD_PORT": "50313",
            "LD_LIBRARY_PATH": "$MDSD_HOME / elib",
            "db_name": "gxds",
            "host_ip": "10.0.0.84",
            "db_type": "mysql",
            "host_port": "3306",
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
            "createTime": "2022-03-01 17:51:13",
            "db_user": "dsg",
            "link_flag": "",
            "asm_oracle_home": "",
            "db_alias_name": "84-mysql",
            "flag": "true",
            "hostIp": ip140,
            "hostPort": "22",
            "tokenID": self.token
        }
        try:
            codes,newres = Taskpublicmethods().publicSaveFlowConfigureInfo(datas=params)
            if codes == 200 :
                loggers.info("savelink_mm_pa.publicSaveFlowConfInfo2_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.publicSaveFlowConfInfo2_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.publicSaveFlowConfInfo2_mm执行异常".center(60,"@"))

    # 再次保存 saveModuleEngineFlowInfo
    def saveModuleEngineInfoagain_mm(self):
        print("$$$$$$$$$$$$$$$$$$$$$$",self.follow_id)
        # txt中获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1()
        print("源端", packagename)
        print("源端", packagepath)
        print("源端", installpath)

        modeldatas = '[{"istiming":0,"msg":{"gid":"1","level":1,"onlyOne":false,"engineType":200,"engineTypeCode":200,"version":"5.1-8.0","tid":"12","imgName":"mysql","hideFlag":false,"name":"源端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"89","linkName":"gx-mysql-mysql-84","show":{"base":1,"mapping":1,"ddl":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","MDSD_HOME":"'+installpath+'","MDSD_PORT":50313,"LD_LIBRARY_PATH":"$MDSD_HOME/elib","flag":"true","dbID":1659},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"gxdt","show":{"base":1,"yloader":1,"txad":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
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
            codes,newres = Taskpublicmethods().saveModuleEngineFlowInfo(datas=params,headers=head)
            flowid = newres["dataInfo"]["flowId"]
            if codes == 200 and flowid == self.follow_id:
                loggers.info("savelink_mm_pa.saveModuleEngineInfoagain_mm执行成功".center(60,"~"))
            else:
                loggers.info("savelink_mm_pa.saveModuleEngineInfoagain_mm执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("savelink_mm_pa.saveModuleEngineInfoagain_mm执行异常，请检查".center(60,"@"))



if __name__ == "__main__":
    s = Savelink()
    s.saveRelMloderDetailValue_mm()
    s.saveModuleEngineFlowInfo_mm()
    s.saveFlowLogInfo_mm()
    s.saveRelMloderDetailValue0_mm()
    s.queryMachineConfInfo_mm()
    s.getDefaultPathByMacIDpa_s()
    s.writepath_s()
    s.publicSaveFlowMacConfInfo_mm()
    s.savelogagain()
    s.publicSaveFlowMacConfInfo1_mm()
    s.publicSaveEngineModuleDataID_mm()
    s.publicSaveFlowConfInfo2_mm()
    s.saveModuleEngineInfoagain_mm()