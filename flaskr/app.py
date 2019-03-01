# coding=utf-8
from flask import Flask, redirect, url_for, request
from flask import render_template
from httpGetAnalysis import *




app = Flask(__name__)

# 绑定函数到url
@app.route('/', methods = ['POST', 'GET'])
# 通用get post解析
def commonGetPost():
    if request.method == "POST":
        print(request.args)
        return "CMD POST SUCCESS!"

    if request.method == "GET":
        httpGetAnalysis = HttpGetAnalysisClass()
        if (httpGetAnalysis.saveGetValueToLog(request.url) == True):
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

# 主函数
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "2222", debug = True)