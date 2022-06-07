# _*_ coding:utf-8 _*_
__author__ = 'jiajun.zhao'

import requests
import json


'''
response.text返回的是Unicode格式，通常需要转换为utf-8格式，否则就是乱码。
response.content是二进制模式，可以下载视频之类的，如果想看的话需要decode成utf-8格式。
不管是通过response.content.decode("utf-8)的方式还是通过response.encoding="utf-8"的方式
都可以避免乱码的问题发生
'''
class Base():

#------------------------------------------------------get--------------------------------------------------------------


    '''
        # 封装有请求参数的类型（键值对形式表示参数）
        # get请求，含参数（参数以字典方式传入）
    '''
    def get_dic(self,url,params,headers=None):

        response = requests.get(url=url,params=params,headers=headers,timeout=0.5).json()
        result = json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2)
        # 返回值，调用时判断
        return result

    '''
        # 某些接口执行前都需要先登录，此时需要先用session登录
        # 然后再执行get方法
    '''
    def post_session_get(self,url,data):
        # 用session登录
        lourl = "http://ggapi.testapi.pw/v1/user/login"
        lodata = {
            "account": "502690608@qq.com",
            "password": "0462864b64bb4a8635407c894a45dba1",
            "remember_pwd": 0}
        session = requests.session()
        session.post(lourl, data=lodata, verify=False)
        # 执行get方法
        s = session.get(url, params=data,timeout=0.5,verify=False)
        return s


#-------------------------------------------------post-----------------------------------------------------------------
    '''
        #请求正文是application / x - www - form - urlencoded
        #header是{'Content-Type': 'application/x-www-form-urlencoded'}
    '''

    def post_data(self,url,data,headers=None):
        response = requests.post(url=url,data=data,headers=headers)
        return response

    '''
        # 某些接口执行前都需要先登录，此时需要先用session登录
        # 然后再执行post方法
    '''
    def post_session_post(self,url,data):

        # 用session登录
        lourl = "http://ggapi.testapi.pw/v1/user/login"
        lodata = {
            "account": "502690608@qq.com",
            "password": "0462864b64bb4a8635407c894a45dba1",
            "remember_pwd": 0}
        session = requests.session()
        session.post(lourl, data=lodata, verify=False)
        # 执行post方法
        s = session.post(url, data=data, verify=False)
        return s


#-------------------------------------------------patch-----------------------------------------------------------------

    def patch(self,url,params,headers=None):
        response = requests.patch(url=url, data=params).json()
        result = json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    '''
        # 某些接口执行前都需要先登录，此时需要先用session登录
        # 然后再执行patch方法
    '''
    def post_session_patch(self, url, data):
        # 用session登录
        lourl = "http://ggapi.testapi.pw/v1/user/login"
        lodata = {
            "account": "502690608@qq.com",
            "password": "0462864b64bb4a8635407c894a45dba1",
            "remember_pwd": 0}
        session = requests.session()
        session.post(lourl, data=lodata, verify=False)
        # 执行patch方法
        s = session.patch(url, data=data, verify=False)
        return s

#-------------------------------------------------del-------------------------------------------------------------------

    def post_session_del(self,url,params):
        # 用session登录
        lourl = "http://ggapi.testapi.pw/v1/user/login"
        lodata = {
            "account": "502690608@qq.com",
            "password": "0462864b64bb4a8635407c894a45dba1",
            "remember_pwd": 0}
        session = requests.session()
        session.post(lourl, data=lodata, verify=False)
        # 执行patch方法
        s = session.delete(url=url,data=params)
        return s
#-------------------------------------------------others----------------------------------------------------------------
