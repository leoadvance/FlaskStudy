# coding=utf-8

from urllib.parse import urlparse
import urllib
import numpy as np
from datetime import datetime
from logFile import *

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
        npArray = np.array(tempMultList)
        # print("npArray:", npArray)
        # print("npArray.size:", npArray.size)
        # print("npArray.size:", npArray.size, " npArray.shape:", npArray.shape)

        # 做数据保护 数组大小是2的整倍数
        if npArray.size > 0 and npArray.size % 2 == 0:
            # 遍历数组 并且把二维转成1维
            listValues = []
            [rows, cols] = npArray.shape
            # print(rows, cols)
            for i in range(rows):
                for j in range(cols):
                    # print(a)
                    listValues.append(str(npArray[i][j]))

            # start = datetime.now()
            # 声明log 实例
            logClass = LOGClass(str(listValues[1]))

            # 插入时间数据 年月日 时分秒
            timenow = datetime.now()
            logDate = timenow.strftime("%Y/%m/%d")
            logTime = timenow.strftime("%H:%M:%S")
            logTimems = timenow.strftime("%f")[:-3]
            wrtiteData = logDate + "," + logTime + "," + logTimems + ","  + ','.join(
                listValues[1:]) + "\n"
            # print("wrtiteData", wrtiteData)

            # 写log
            logClass.log_file_write(wrtiteData)

            # print ("listData", listData)
            return True

        else:
            return False