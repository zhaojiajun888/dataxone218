# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import json
from commons.log import loggers
from commons.config import newhost,ip71,user71,pwd71
from commons.fileopera import Fileopera
from interfaces.publics.publicmethods import Publicmethods
from interfaces.publics.taskpublicmethods import Taskpublicmethods

class Aimmachine_oo(Publicmethods):
    """
        oracle-oracle，一对一，不开启分离
        承接 savelink_oo_pa
        实现：设置目标端主机
    """
    def __init__(self):
        super(Aimmachine_oo, self).__init__()
        # 获取taskname 和follow_id
        self.taskname, self.follow_id = Fileopera().readfilepa()

    # 获取目标端的相关路径 getDefaultPathByMacID
    def getDefaultPathByMacID_oo_d(self):
        print(">>>>>>>>>>>>>>>>>", self.taskname)
        print(">>>>>>>>>>>>>>>>>", self.follow_id)
        path = "/autoMaticEngineBoot-1.0.0/hostAndDataSourceConfig/getDefaultPathByMacID.do"
        url = newhost + path
        params = {
                "flowID" : self.follow_id,
                "engineID" : "21",
                "engineType" : "dt",
                "serviceName" : self.taskname,
                "isContainYloader" : "false",
                "macID" : "1011",
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
            loggers.info("aimmachine_oo_pa.getDefaultPathByMacID_oo_d执行异常,请检查".center(60,"@"))

    # 将目标端路径存入txt
    def writepath_oo_d(self):
        paths = "/dataxone218/data/oo_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = self.getDefaultPathByMacID_oo_d()
        content = str(packagename + "," + packagepath + "," + installpath)
        Fileopera().writefilepa1(contents=content, path=paths)

    # 保存目标端 publicSaveFlowMacConfigureInfo
    def des_publicSaveConfigureInfo_oo(self):
        # 获取packagename,packagepath,installpath
        pathes = "/dataxone218/data/oo_mubiaoduanpath.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        params = {
            "packageName": packagename,
            "packagePath": packagepath,
            "engineID": "21",
            "passWord": pwd71,
            "hostName": ip71,
            "path": "",
            "port": "22",
            "loginType": "password",
            "ip": ip71,
            "linkMode": "ssh",
            "hostID": "1011",
            "userName": user71,
            "osName": "Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux",
            "flowID": self.follow_id,
            "moduleID": "3",
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().publicSaveFlowMacConfigureInfo(datas=params)
            dbpshome = newres["dataInfo"][0]["pathInfo"]["DBPS_HOME"]
            if codes == 200 and dbpshome == installpath:
                loggers.info("aimmachine_oo_pa.des_publicSaveConfigureInfo_oo执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_oo_pa.des_publicSaveConfigureInfo_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_oo_pa.des_publicSaveConfigureInfo_oo执行异常,请检查".center(60, "@"))

    # 保存log saveFlowLogInfo
    def des_saveFlowLogInfo_oo(self):
        operinfo = "目标端基础配置保存成功，ip地址：10.0.0.71，安装目录："
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
                loggers.info("aimmachine_oo_pa.des_saveFlowLogInfo_oo执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_oo_pa.des_saveFlowLogInfo_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_oo_pa.des_saveFlowLogInfo_oo执行异常，请检查".center(60, "@"))

    # 再次保存 publicSaveFlowMacConfigureInfo
    def des_saveMacConfigureInfo_oo(self):
        pathes = "/dataxone218/data/oo_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","19":"","30":42218,"31":"127.0.0.1","32":42219,"41":"'+ip71+'","42":"'+ip71+'","43":"22","44":"'+user71+'","45":"'+pwd71+'","46":"orcl","47":"'+ip71+'","49":1573,"50":"password","53":"71ora","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "21",
            "moduleID": "3",
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
            "xagentdPort" : "37292",
            "yxadIpAddress" : "127.0.0.1",
            "yxadPort" : "37293",
            "DBPS_HOME" : installpath,
            "XLDR_HOME" : "$DBPS_HOME/rmp",
            "VCFS_HOME" : "$DBPS_HOME/vcfsa",
            "LD_LIBRARY_PATH" : "$DBPS_HOME/elib",
            "db_name" : "orcl",
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
            dbpshome = newres["dataInfo"][0]["pathInfo"]["DBPS_HOME"]
            if codes == 200 and dbpshome == installpath:
                loggers.info("aimmachine_oo_pa.des_saveMacConfigureInfo_oo执行成功".center(60,"~"))
            else:
                loggers.info("aimmachine_oo_pa.des_saveMacConfigureInfo_oo执行失败".center(60,"!"))
        except Exception as e:
            loggers.info("aimmachine_oo_pa.des_saveMacConfigureInfo_oo执行异常，请检查".center(60,"@"))

    # 保存 publicSaveEngineModuleDataBaseID
    def des_publicDataBaseID_oo(self):
        pathes = "/dataxone218/data/oo_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","19":"","30":42220,"31":"127.0.0.1","32":42221,"41":"'+ip71+'","42":"'+ip71+'","43":"22","44":"'+user71+'","45":"'+pwd71+'","46":"orcl","47":"'+ip71+'","49":1573,"50":"password","53":"71ora","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "21",
            "moduleID": "3",
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
            "xagentdPort": "37294",
            "yxadIpAddress": "127.0.0.1",
            "yxadPort": "37295",
            "DBPS_HOME": installpath,
            "XLDR_HOME": "$DBPS_HOME/rmp",
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
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().publicSaveEngineModuleDataBaseID(datas=params)
            if codes == 200:
                loggers.info("aimmachine_oo_pa.des_publicDataBaseID_oo执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_oo_pa.des_publicDataBaseID_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_oo_pa.des_publicDataBaseID_oo执行异常，请检查".center(60, "@"))

    # 保存 publicSaveFlowConfigureInfo
    def des_SaveFlowConfigureInfo_oo(self):
        pathes = "/dataxone218/data/oo_mubiaoduanpath.txt"
        # 获取packagename,packagepath,installpath
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        baseconfiginfo = '[{"5":"'+installpath+'","6":"$DBPS_HOME/rmp","7":"$DBPS_HOME/vcfsa","8":"$DBPS_HOME/elib","16":"'+packagepath+'","17":"'+packagename+'","18":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","19":"","30":42220,"31":"127.0.0.1","32":42221,"41":"'+ip71+'","42":"'+ip71+'","43":"22","44":"'+user71+'","45":"'+pwd71+'","46":"orcl","47":"'+ip71+'","49":1573,"50":"password","53":"71ora","1112":"'+installpath+'"}]'
        params = {
            "flowID": self.follow_id,
            "engineID": "21",
            "moduleID": "3",
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
            "xagentdPort": "37294",
            "yxadIpAddress": "127.0.0.1",
            "yxadPort": "37295",
            "DBPS_HOME": installpath,
            "XLDR_HOME": "$DBPS_HOME/rmp",
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
            "tokenID": self.token
        }
        try:
            codes, newres = Taskpublicmethods().publicSaveFlowConfigureInfo(datas=params)
            message = newres["dataInfo"]
            if codes == 200 and "suc" in message:
                loggers.info("aimmachine_oo_pa.des_SaveFlowConfigureInfo_oo执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_oo_pa.des_SaveFlowConfigureInfo_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_oo_pa.des_SaveFlowConfigureInfo_oo执行异常，请检查".center(60, "@"))

    # 保存 saveModuleEngineFlowInfo
    def des_ModuleEngineFlowInfo_oo(self):
        # 获取packagename,packagepath,installpath
        pathes_d = "/dataxone218/data/oo_mubiaoduanpath.txt"
        packagename, packagepath, installpath = Fileopera().readfilepa1(path=pathes_d)
        print("目标端", packagename)
        print("目标端", packagepath)
        print("目标端", installpath)

        # 获取源端 packagename和packagepath
        pathes_s = "/dataxone218/data/oo_yuanduanpath.txt"
        packagename1, packagepath1, installpath1 = Fileopera().readfilepa1(path=pathes_s)
        print("源端", packagename1)
        print("源端", packagepath1)
        print("源端", installpath1)

        modeldatas = '[{"istiming":0,"msg":{"dbType":"oracle","id":20,"imgName":"oracle","engineTypeCode":100,"name":"源端组件","linkName":"autotest1o_o","show":{"base":1,"mapping":1,"ddl":1},"version":"11.2","details":"Linux-3.10.x86_64"},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"'+ip71+'","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora","passWord":"'+pwd71+'","hostName":"'+ip71+'","path":"'+installpath1+'","port":"22","loginType":"password","ip":"'+ip71+'","linkMode":"ssh","hostID":1011,"userName":"'+user71+'","osName":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath1+'","installPath":"'+installpath1+'","packageName":"'+packagename1+'","createStat":"true","docIsExist":"false","OXAD_HOST":"127.0.0.1","PORT":42210,"OXAD_PORT":42213,"AOX_PORT":42212,"dbpsdPort":42211,"TIMING_SYNC_EXPORT":"","DBPS_HOME":"'+installpath1+'","ASM_CONF_FILENAME":"$DBPS_HOME/config/asm.conf","XLDR_HOME":"$DBPS_HOME/rmp","AOX_CONF_FILE":"$DBPS_HOME/config/aoxd.ini","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true","dbID":1573},"exportD":{}},"moduleid":1},{"isetl":0,"monitorType":1,"isDesensitization":0,"isConversionFilter":0,"isTablestructure":0,"taskType":1,"msg":{"dbType":"oracle","id":21,"imgName":"oracle","engineTypeCode":101,"name":"目标端组件","KAFKA_DDL_TOPIC":"AQ","show":{"base":1,"yloader":1,"txad":1},"version":"11.2","details":"Linux-3.10.x86_64"},"data":{},"data2":{"nowValue":{"db_type":"oracle","host_ip":"'+ip71+'","host_port":"1521","odbc":"","pdb_flag":"","pdb_name":"","s3_url":"","asm_sid":"","srcFilePath":"","db_stat":1,"tns_name":"","db_id":1573,"db_name":"orcl","postgreSQL":null,"db_passwd":"dsg","db2":null,"createTime":"2022-01-05 11:12:59","db_user":"dsg","link_flag":"SID","asm_oracle_home":"/u01/app/oracle/product/11.2.0","db_alias_name":"71ora","passWord":"'+pwd71+'","hostName":"'+ip71+'","path":"'+installpath+'","port":"22","loginType":"password","ip":"'+ip71+'","linkMode":"ssh","hostID":1011,"userName":"'+user71+'","osName":"Linux host71 3.10.0-327.el7.x86_64 #1 SMP Thu Nov 19 22:10:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux","packagePath":"'+packagepath+'","installPath":"'+installpath+'","packageName":"'+packagename+'","createStat":"true","docIsExist":"false","xagentdPort":42220,"yxadIpAddress":"127.0.0.1","yxadPort":42221,"DBPS_HOME":"'+installpath+'","XLDR_HOME":"$DBPS_HOME/rmp","VCFS_HOME":"$DBPS_HOME/vcfsa","LD_LIBRARY_PATH":"$DBPS_HOME/elib","flag":"true"},"exportD":{}},"moduleid":3,"manyTarget":"false","mlDseParate":"false"}]'
        params = {
            "modelLines": '[{"endOrderId":2,"endId":21,"startId":20,"startModuleId":1,"endModuleId":3,"serverName":"'+self.taskname+'","startOrderId":1}]',
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
                loggers.info("aimmachine_oo_pa.des_ModuleEngineFlowInfo_oo执行成功".center(60, "~"))
            else:
                loggers.info("aimmachine_oo_pa.des_ModuleEngineFlowInfo_oo执行失败".center(60, "!"))
        except Exception as e:
            loggers.info("aimmachine_oo_pa.des_ModuleEngineFlowInfo_oo执行异常，请检查".center(60, "@"))



if __name__ == "__main__":
    s = Aimmachine_oo()
    # s.getDefaultPathByMacID_oo_d()
    # s.writepath_om_d()
    # s.des_publicSaveConfigureInfo_oo()
    # s.des_saveFlowLogInfo_oo()
    # s.des_saveMacConfigureInfo_oo()
    # s.des_publicDataBaseID_oo()
    # s.des_SaveFlowConfigureInfo_oo()
    s.des_ModuleEngineFlowInfo_oo()