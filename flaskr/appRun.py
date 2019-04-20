# coding=utf-8
from flask import Flask, redirect, url_for, request, make_response,send_from_directory
from flask import render_template, after_this_request
from httpGetAnalysis import *
from datetime import datetime
import threading
import time
import socket
import shutil

logCount = 0
import logging
# 控制台只显示ERROR级别的信息
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

app = Flask(__name__)

# 绑定函数到url
@app.route('/', methods = ['POST', 'GET'])
# 通用get post解析
def commonGetPost():
    if request.method == "POST":
        # print(request.args)
        return "CMD POST SUCCESS!"

    if request.method == "GET":
        # start = datetime.now()
        global logCount
        logCount += 1
        if (HttpGetAnalysisClass.saveGetValueToLog(request.url) == True):
            # print("runTime = ", datetime.now() - start)
            return "CMD GET SUCCESS!"
        else:
            return "ERROR CMD FORMATE!"

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

@app.route("/log")
def loglist():
    # 列出log下文件列表
    app.config['LOG_PATH'] = os.path.join(app.root_path, LOGClass.logFilePath)
    tempFileList = os.listdir(app.config['LOG_PATH'])

    # 过滤文件 只显示xx.csv
    logFileList = []
    for data in tempFileList:
        # 提取文件名和后缀
        templist = os.path.splitext(data)
        # 找出CSV文件
        if templist[-1] == ".csv":
            # 非备份文件
            if templist[0][-4:] != "_Bak":
                logFileList.append(data)

    # print("logFileList:", logFileList)
    return render_template('logDownload.html', file_list = logFileList)

# log上传
@app.route("/logDownload/", methods = ['GET'])
def logDownload():
    # 从字典的value中找到文件名
    fileName = request.args.to_dict()["name"]

    # 重命名 删除原始文件 让用户下载重命名后文件
    temp = fileName.split(".")
    fileNameCopy = temp[0]+"_Bak."+temp[1]
    if os.path.exists(LOGClass.getLogDir() + "/" + fileNameCopy) == True:
        os.remove(LOGClass.getLogDir() + "/" + fileNameCopy)
    os.rename(LOGClass.getLogDir() + "/" + fileName, LOGClass.getLogDir() + "/" + fileNameCopy)
    # 准备文件并下载
    response = make_response(send_from_directory(LOGClass.getLogDir(), fileNameCopy.encode('utf-8').decode('utf-8'),
                                                 as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(fileNameCopy.encode().decode('latin-1'))

    return response

# @app.route("/logrm/<string:fileName>",  methods = ['GET'])
# def logRemove(fileName:str):
#
#     return "The %s logfile was deleted successfully!" %fileName

def serverRunInfo():
    global logCount
    count = 0
    while True:
        # 原地打印信息
        print("服务器运行时间：",count,"s", " 每秒接收到HTTP请求：",logCount ,"条", end="\r", flush=True)
        logCount = 0
        time.sleep(1)
        count += 1
def get_host_ip()->str:
    """
    查询本机ip地址
    :return:        ip str
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

# 主函数
if __name__ == "__main__":
    print("服务器运启动: ")
    ip = get_host_ip()
    print("IP:", ip, "Port: 80")
    # thread1 = threading.Thread(target=serverRunInfo)
    #
    # thread1.start()

    LOGClass.creatLogDir()
    app.run(host = "0.0.0.0", port = "80", debug = True)




