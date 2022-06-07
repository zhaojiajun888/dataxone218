# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'


class Fileopera():
    """
        同步管理中将生成的taskname和follow_id放入txt
        然后读取
    """
    path = "/dataxone218/data/datapro.txt"
    def writefilepa(self,contents):
        f = open(self.path,"w",encoding="utf-8")
        f.write(contents)
        f.close()

    def readfilepa(self):
        f = open(self.path,"r",encoding="utf-8")
        for line in f:
            lines = line.strip()
        f.close()
        datas = lines.partition(",")
        taskname = datas[0]
        followid = datas[2]
        return taskname,followid

    """
        同步管理中将生成的源端路径放入txt
        然后读取
    """
    path1 = "/dataxone218/data/yuanduanpath.txt"
    def writefilepa1(self, contents,path=path1):
        f = open(path, "w", encoding="utf-8")
        f.write(contents)
        f.close()

    def readfilepa1(self,path=path1):
        f = open(path,"r",encoding="utf-8")
        for line in f:
            lines = line.strip()
        f.close()
        datas = lines.split(",")
        packagename = datas[0]
        packagepath = datas[1]
        installpath = datas[2]
        return packagename,packagepath,installpath


if __name__ == "__main__":
    f = Fileopera()
    # f.writefilepa("11,22,33")
    k,v,m = f.readfilepa1()
    print(k)
    print(v)
    print(m)

