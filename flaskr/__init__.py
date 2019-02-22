# coding=utf-8
from flask import Flask
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

    @app.route('/blog/<int:postID>')
    def show_blog(postID):
        return 'Blog Number %d' % postID

    @app.route('/hello')
    def hello():
        return 'Hello, LEO!'
        
    return app