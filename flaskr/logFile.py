# coding=utf-8

import os
# log目录名称
DIR_NAME = "../Log"

class LOGClass():

    logFilePath = DIR_NAME

    def __init__(self):
        print("__init__ LOGClass", self)
        self.creatLogDir()
        # print("logFilePWD:", os.path.abspath(__file__))

    def __del__(self):
        print("__del__ LOGClass", self)
        pass
        # 类方法

    @classmethod
    def getLogDir(cls):
        return DIR_NAME

    # 类方法
    @classmethod
    def creatLogDir(cls):
        # 判断目录是否存在
        if os.path.isdir(DIR_NAME) == False:
            os.mkdir(DIR_NAME)
            print("目录不存在，创建目录:" + DIR_NAME)


    # 创建or打开log文件 
    def log_file_open(self, fileName:str):

        # # 判断目录是否存在
        # if os.path.isdir(DIR_NAME) == False:
        #     os.mkdir(DIR_NAME)
        #     print("目录不存在，创建目录:" + DIR_NAME)
        self.creatLogDir()
        #print(time_str)
        # print("fileName:", fileName)
        # 追加的方式打开文件
        return(open(DIR_NAME + "/" + fileName+ ".csv", "a"))

    @classmethod
    def log_file_write(cls, fileName:str, strData:str):
        """
        写入数据到log文件 单次打开 写入 并关闭
        :param fileName:    要写入的文档名称
        :param strData:     要写入的数据
        :return:            无
        """
        fileHandle = open(DIR_NAME + "/" + fileName + ".csv", "a")
        fileHandle.writelines(strData)
        fileHandle.flush()
        fileHandle.close()