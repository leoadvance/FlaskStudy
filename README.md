## 使用说明

### 运行环境
```
Python3.x
Flask
```
### 功能
```
记录局域网内设备通过HTTP GET发过来的数据并解析保存成csv格式
如url="http://192.168.199.140:80/?deviceID=Test1&temp=123&humi=456&CO2=4234.23"
会解析成设备Test1传递来的temp，humi以及CO2数据

2019/01/06,20:23:12,574,Test1,temp,123,humi,456,CO2,4234.23

其中，前三列分别是年月日，时分秒，以及毫秒

```

### 调用说明
```
python3 appRun.py
./log文件夹下会以CSV格式保存log
文件名为对应的设备名称
```

### log下载
```
浏览器访问http://xx.xx.xx.xx/log 获取文件列表 
点击文件完成log下载
下载完成后服务器上文件会自动删除

```