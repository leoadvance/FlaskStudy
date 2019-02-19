# 设定运行环境变量
export FLASK_APP=flaskr/__init__.py 
export FLASK_ENV=development
# 运行端口号
export FLASK_RUN_PORT=2222
echo $FLASK_APP
python -m flask run --host=0.0.0.0
