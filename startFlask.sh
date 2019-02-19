# 设定运行环境变量
export FLASK_APP=./flaskr/FlaskStudy.py 
export FLASK_RUN_PORT=2222
echo $FLASK_APP
python -m flask run --host=0.0.0.0
