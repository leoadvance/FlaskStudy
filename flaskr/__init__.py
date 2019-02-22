# coding=utf-8
from flask import Flask, redirect, url_for
from flask import render_template

import os

from flask import Flask


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
    @app.route('/')
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