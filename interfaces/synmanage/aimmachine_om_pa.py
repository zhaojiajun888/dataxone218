# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import json
from commons.log import loggers
from commons.config import newhost,ip140,user140,pwd140
from commons.config import ip71,user71,pwd71
from commons.fileopera import Fileopera
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods


class Aimmachine_om(Publicmethods):
    """
        oracle-mysql，一对一，不开启分离
        承接 savelink_om_pa
        实现：设置目标端主机
    """
    def __init__(self):
        super(Aimmachine_om, self).__init__()
        # 获取taskname 和follow_id
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 获取目标端的相关路径 getDefaultPathByMacID
    def getDefaultPathByMacID_om_d(self):
        print(">>>>>>>>>>>>>>>>>", self.taskname)
        print(">>>>>>>>>>>>>>>>>", self.follow_id)
        path = "/autoMaticEngineBoot-1.0.0/hostAndDataSourceConfig/getDefaultPathByMacID.do"
        url = newhost + path
        params = {
                "flowID" : self.follow_id,
                "engineID" : "31",
                "engineType" : "dt",
                "serviceName" : self.taskname,
                "isContainYloader" : "false",
                "macID" : "1081",
                "path" : "",
                "tokenID" : self.token
        }
        try:
            response = self.post_data(url=url,data=params)
            newres = json.loads(response.text)
            packagename = newres["dataInfo"]["target"]["packageName"]
            packagepath = newres["dataInfo"]["target"]["packagePath"]
            installpath = newres["dataInfo"]["target"]["installPath"]
            return packagename,packagepath,installpath
        except Exception as e:
            loggers.info("aimmachine_om_pa.getDefaultPathByMacID_om_d执行异常,请检查".center(60,"@"))

    # 将目标端路径存入txt
    def writepath_om_d(self):
        paths = "/dataxone218/data/om_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = self.getDefaultPathByMacID_om_d()
        content = str(packagename + "," + packagepath + "," + installpath)
        Fileopera().writefilepa1(contents=content, path=paths)

    # 保存目标端 publicSaveFlowMacConfigureInfo
    def des_publicSaveConfigureInfo_om(self):
        # 获取packagename,packagepath,installpath
        pathes = "/dataxone218/data/om_mubiaoduanpath.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        params = {
            "packageName": packagename,
            "packagePath": packagepath,
            "engineID": "31",
            "passWord": pwd140,
            "hostName": ip140,
            "path": "",
            "port": "22",
            "loginType": "password",
            "ip": ip140,
            "linkMode": "ssh",
            "hostID": "1081",
            "userName": user140,
            "osName": "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
            "flowID": self.follow_id,
            "moduleID": "3",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            dbpshome = newres["dataInfo"][0]["pathInfo"]["DBPS_HOME"]
            if codes == 200 and dbpshome == installpath:
                loggers.info("aimmachine_om_pa.des_publicSaveConfigureInfo_om执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_om_pa.des_publicSaveConfigureInfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_om_pa.des_publicSaveConfigureInfo_om执行异常,请检查".center(60, "@"))

    # 保存log saveFlowLogInfo
    def des_saveFlowLogInfo_om(self):
        operinfo = "目标端基础配置保存成功，ip地址："+ip140+"，安装目录："
        params = {
            "flowID": self.follow_id,
            "moduleID": "",
            "serviceName": self.taskname,
            "operInfo": operinfo,
            "operStat": "success",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().saveFlowLogInfo(datas=params)
            message = newres["message"]
            if codes == 200 and "success" == message:
                loggers.info("aimmachine_om_pa.des_saveFlowLogInfo_om执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_om_pa.des_saveFlowLogInfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_om_pa.des_saveFlowLogInfo_om执行异常，请检查".center(60, "@"))

    # 再次保存 publicSaveFlowMacConfigureInfo
    def des_saveMacConfigureInfo_om(self):
        pathes = "/dataxone218/data/om_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","30":50941,"31":"127.0.0.1","32":50942,"41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gxds","47":"10.0.0.84","49":1659,"50":"password","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "31",
            "moduleID": "3",
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
            "xagentdPort" : "50941",
            "yxadIpAddress" : "127.0.0.1",
            "yxadPort" : "50942",
            "DBPS_HOME" : installpath,
            "XLDR_HOME" : "$DBPS_HOME/rmp",
            "VCFS_HOME" : "$DBPS_HOME/vcfsa",
            "LD_LIBRARY_PATH" : "$DBPS_HOME/elib",
            "db_name" : "gxds",
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
            codes,newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            dbpshome = newres["dataInfo"][0]["pathInfo"]["DBPS_HOME"]
            if codes == 200 and dbpshome == installpath:
                loggers.info("aimmachine_om_pa.des_saveMacConfigureInfo_om执行成功".center(60,"~"))
            else:
                loggers.info("aimmachine_om_pa.des_saveMacConfigureInfo_om执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("aimmachine_om_pa.des_saveMacConfigureInfo_om执行异常，请检查".center(60,"@"))

    # 保存 publicSaveEngineModuleDataBaseID
    def des_publicDataBaseID_om(self):
        pathes = "/dataxone218/data/om_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","30":50943,"31":"127.0.0.1","32":50944,"41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gxds","47":"10.0.0.84","49":1659,"50":"password","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "31",
            "moduleID": "3",
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
            "xagentdPort": "50943",
            "yxadIpAddress": "127.0.0.1",
            "yxadPort": "50944",
            "DBPS_HOME": installpath,
            "XLDR_HOME": "$DBPS_HOME/rmp",
            "VCFS_HOME": "$DBPS_HOME/vcfsa",
            "LD_LIBRARY_PATH": "$DBPS_HOME/elib",
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
                loggers.info("aimmachine_om_pa.des_publicDataBaseID_om执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_om_pa.des_publicDataBaseID_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_om_pa.des_publicDataBaseID_om执行异常，请检查".center(60, "@"))

    # 保存 publicSaveFlowConfigureInfo
    def des_SaveFlowConfigureInfo_om(self):
        pathes = "/dataxone218/data/om_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","19":"","30":50943,"31":"127.0.0.1","32":50944,"41":"'+ip140+'","42":"'+ip140+'","43":"22","44":"'+user140+'","45":"'+pwd140+'","46":"gxds","47":"10.0.0.84","49":1659,"50":"password","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "31",
            "moduleID": "3",
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
            "userName":user140,
            "osName": "Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux",
            "packagePath": packagepath,
            "installPath": installpath,
            "packageName": packagename,
            "createStat": "true",
            "docIsExist": "false",
            "xagentdPort": "50943",
            "yxadIpAddress": "127.0.0.1",
            "yxadPort": "50944",
            "DBPS_HOME": installpath,
            "XLDR_HOME": "$DBPS_HOME/rmp",
            "VCFS_HOME": "$DBPS_HOME/vcfsa",
            "LD_LIBRARY_PATH": "$DBPS_HOME/elib",
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
            codes, newres = Taskpublicmethods().publicSaveFlowConfigureInfo(datas=params)
            message = newres["dataInfo"]
            if codes == 200 and "suc" in message:
                loggers.info("aimmachine_om_pa.des_SaveFlowConfigureInfo_om执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_om_pa.des_SaveFlowConfigureInfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_om_pa.des_SaveFlowConfigureInfo_om执行异常，请检查".center(60, "@"))

    # 保存 saveModuleEngineFlowInfo
    def des_ModuleEngineFlowInfo_om(self):
        # 获取packagename,packagepath,installpath
        pathes_d = "/dataxone218/data/om_mubiaoduanpath.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes_d)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        # 获取源端 packagename和packagepath
        pathes_s = "/dataxone218/data/om_yuanduanpath.txt"
        packagename1, packagepath1, installpath1 = Fileopera().readfilepa1(path=pathes_s)
        print("源端", packagename1)
        print("源端", packagepath1)
        print("源端", installpath1)

        modeldatas = '[{"istiming":0,"msg":{"dbType":"oracle","id":20,"imgName":"oracle","engineTypeCode":100,"name":"源端组件","linkName":"autotest1o_m","show":{"base":1,"mapping":1,"ddl":1},"version":"11.2","details":"Linux-3.10.x86_64"},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"'+ip71+'","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora","passWord":"'+pwd71+'","hostName":"'+ip71+'","path":"'+installpath1+'","port":"22","loginType":"password","ip":"'+ip71+'","linkMode":"ssh","hostID":1011,"userName":"'+user71+'","osName":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath1+'","installPath":"'+installpath1+'","packageName":"'+packagename1+'","createStat":"true","docIsExist":"false","OXAD_HOST":"127.0.0.1","PORT":42754,"OXAD_PORT":42757,"AOX_PORT":42756,"dbpsdPort":42755,"TIMING_SYNC_EXPORT":"","DBPS_HOME":"'+installpath1+'","ASM_CONF_FILENAME":"$DBPS_HOME/config/asm.conf","XLDR_HOME":"$DBPS_HOME/rmp","AOX_CONF_FILE":"$DBPS_HOME/config/aoxd.ini","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true","dbID":1573},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"gid":"1","level":2,"onlyOne":false,"engineType":100,"engineTypeCode":201,"version":"5.1+","tid":"10,12","imgName":"mysql","hideFlag":false,"name":"目标端组件","javaOrC":1,"details":"Linux-2.6.x86_64","id":"31","KAFKA_DDL_TOPIC":"duyu","show":{"base":1,"yloader":1,"txad":1}},"data":{},"data2":{"nowValue":{"db_type":"mysql","host_ip":"10.0.0.84","host_port":"3306","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1659,"db_name":"gxds","postgreSQL":null,"db_passwd":"Dsgdata@123","db2":null,"createTime":"2022-03-01 17:51:13","db_user":"dsg","link_flag":"","asm_oracle_home":"","db_alias_name":"84-mysql","passWord":"'+pwd140+'","hostName":"'+ip140+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip140+'","linkMode":"ssh","hostID":1081,"userName":"'+user140+'","osName":"Linux host01 2.6.32-504.el6.x86_64 #1 SMP Wed Oct 15 04:27:16 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","xagentdPort":50943,"yxadIpAddress":"127.0.0.1","yxadPort":50944,"DBPS_HOME":"'+installpath+'","XLDR_HOME":"$DBPS_HOME/rmp","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'

        params = {
            "modelLines": '[{"endOrderId":2,"endId":"31","startId":20,"startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
            "modelDatas": modeldatas,
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
                loggers.info("aimmachine_om_pa.des_ModuleEngineFlowInfo_om执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_om_pa.des_ModuleEngineFlowInfo_om执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_om_pa.des_ModuleEngineFlowInfo_om执行异常，请检查".center(60, "@"))


if __name__ == "__main__":
    s = Aimmachine_om()
    s.getDefaultPathByMacID_om_d()
    s.writepath_om_d()
    s.des_publicSaveConfigureInfo_om()
    s.des_saveFlowLogInfo_om()
    s.des_saveMacConfigureInfo_om()
    s.des_publicDataBaseID_om()
    s.des_SaveFlowConfigureInfo_om()
    s.des_ModuleEngineFlowInfo_om()