# coding=utf-8

from urllib.parse import urlparse
import urllib
import numpy as np
from datetime import datetime
# 相对路径库
import os
import sys
lib_path = os.path.abspath(os.path.join('./flaskr'))
sys.path.append(lib_path)
from flaskr.logFile import *

class HttpGetAnalysisClass():

    fileHandle = None

    def __init__(self):
        # print("__init__", self)
        pass

    def __del__(self):
        # print("__del__", self)
        pass

    def saveGetValueToLog(self, url:str):
        # 分解url参数到list
        tempMultList = urllib.parse.parse_qsl(urlparse(url).query)
        values = np.array(tempMultList)
        # print(b)
        # print("array.size:", values.size, " array.shape:", values.shape)

        # 遍历数组 并且把二维转成1维
        listValues = []
        [rows, cols] = values.shape
        # print(rows, cols)
        for i in range(rows):
            for j in range(cols):
                # print(a)
                listValues.append(str(values[i][j]))

        # start = datetime.now()
        # 声明log 实例
        logClass = LOGClass(str(listValues[1]))

        # 插入时间数据 年月日 时分秒
        log_date = datetime.now().strftime("%Y/%m/%d")
        log_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        wrtiteData = log_date + "," + log_time + "," + ','.join(
            listValues[1:]) + "\n"
        # print("wrtiteData", wrtiteData)

        # 写log
        logClass.log_file_write(wrtiteData)

        # print ("listData", listData)
