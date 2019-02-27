# coding=utf-8
from flask import Flask, redirect, url_for, request
from flask import render_template
from urllib.parse import urlparse
import urllib
import numpy as np
import itertools
import os
import sys
lib_path = os.path.abspath(os.path.join('./flaskr'))
sys.path.append(lib_path)
from flaskr.logFile import *
from datetime import datetime


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    print("app_name:", __name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # 绑定函数到url
    @app.route('/', methods = ['POST', 'GET'])
    # 通用get post解析
    def commonGetPost():
        if request.method == "POST":
            print(request.args)
            return "CMD POST SUCCESS!"

        if request.method == "GET":

            # 获取Http Get参数并转化成dict
            getMuslDict = request.args
            getDict = getMuslDict.to_dict()
            print("getMuslDict", getMuslDict)
            print("url", request.url)
            print("getDict", getDict)
            # dict参数转list
            listKey   = list(getDict.keys())
            listValue = list(getDict.values())
            listData  = list(itertools.chain.from_iterable(zip(listKey,
                                                              listValue)))

            tempMultList = urllib.parse.parse_qsl(urlparse(request.url).query)
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
            return "CMD GET SUCCESS!"

    @app.route('/index')
    def index():
        user = {'username': 'LEO'}
        return render_template('index.html', title='Home', user=user)
    # 限定只能是int型
    @app.route('/blog/<int:postID>')
    def show_blog(postID):
        return 'Blog Number %d' % postID

    @app.route('/hello')
    def hello():
        return 'Hello, LEO!'

    # 重定向
    @app.route('/admin')
    def hello_admin():
        return 'Hello Admin'

    @app.route('/guest/<guest>')
    def hello_guest(guest):
        return 'Hello %s as Guest' % guest

    @app.route('/user/<name>')
    def user(name):
        if name =='admin':
            return redirect(url_for('hello_admin'))
        else:
            return redirect(url_for('hello_guest',guest = name))

    return app