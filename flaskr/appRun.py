# coding=utf-8
from flask import Flask, redirect, url_for, request, make_response,send_from_directory
from flask import render_template
from httpGetAnalysis import *
from datetime import datetime
import threading
import time

#
# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.DEBUG)

app = Flask(__name__)

# 绑定函数到url
@app.route('/', methods = ['POST', 'GET'])
# 通用get post解析
def commonGetPost():
    if request.method == "POST":
        print(request.args)
        return "CMD POST SUCCESS!"

    if request.method == "GET":
        # start = datetime.now()
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
    logFileList = os.listdir(app.config['LOG_PATH'])
    # print("logFileList:", logFileList)
    return render_template('logDownload.html', file_list = logFileList)

# log上传
@app.route("/logDownload/", methods = ['GET'])
def logDownload():

    # 从字典的value中找到文件名
    fileName = request.args.to_dict()["name"]
    # print("fileName:", fileName)

    # 准备文件并下载
    response = make_response(
        send_from_directory(LOGClass.logFilePath, fileName.encode('utf-8').decode('utf-8'),
                            as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(
        fileName.encode().decode('latin-1'))
    return response

@app.route("/logrm/<string:fileName>",  methods = ['GET'])
def logRemove(fileName:str):

    return "The %s logfile was deleted successfully!" %fileName

def serverRunInfo():
    count = 0
    while True:
        print('\x1b[2K\r')
        time.sleep(1)
        count += 1
        print("服务器运行时间",count, end="", flush=True)


# 主函数
if __name__ == "__main__":
    # thread1 = threading.Thread(target=serverRunInfo())
    # thread1.start()
    print("服务器运启动")
    LOGClass.creatLogDir()
    app.run(host = "0.0.0.0", port = "80", debug = True)