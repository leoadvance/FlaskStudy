# coding=utf-8

from urllib.parse import urlparse
import urllib
import numpy as np
from datetime import datetime
from logFile import *

class HttpGetAnalysisClass():

    fileHandle = None

    def __init__(self):
        print("__init__ HttpGetAnalysisClass()", self)
        pass

    def __del__(self):
        print("__del__ HttpGetAnalysisClass()", self)
        pass
    # 直接声明类方法
    @classmethod
    def saveGetValueToLog(cls, url:str) -> bool:
        """
        分析url 并保存到log
        :param url: 接收到的url
        :return:
        """
        # 分解url参数到二维list
        tempMultList = urllib.parse.parse_qsl(urlparse(url).query)
        listValues = []

        # 无参数
        if not tempMultList:
            return False
        for tuple_ in tempMultList:

            # 判断是否格式错误
            if len(tuple_) != 2:
                return False
            else:
                # 二维数组转一维
                listValues.append(tuple_[0])
                listValues.append(tuple_[1])

        # start = datetime.now()

        # 插入时间数据 年月日 时分秒
        timeNow = datetime.now()
        logDate = timeNow.strftime("%Y/%m/%d")
        logTime = timeNow.strftime("%H:%M:%S")
        logTimems = timeNow.strftime("%f")[:-3]
        wrtiteData = logDate + "," + logTime + "," + logTimems + ","  + ','.join(
            listValues[1:]) + "\n"
        # print("wrtiteData", wrtiteData)

        # 写log
        LOGClass.log_file_write(str(listValues[1]), wrtiteData)

        # print ("listData", listData)
        return True
