import time
import logging
import logging.handlers

# logging初始化工作
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# myapp的初始化工作
myapp = logging.getLogger('myapp')
myapp.setLevel(logging.INFO)


# 添加TimedRotatingFileHandler
# 定义一个1秒换一次log文件的handler
# 保留3个旧log文件
timefilehandler = logging.handlers.TimedRotatingFileHandler("myapp.log", when='H', interval=1, backupCount=3)
# 设置后缀名称，跟strftime的格式一样
timefilehandler.suffix = "%Y-%m-%d_%H.log"

# formatter = logging.Formatter('%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s')
# timefilehandler.setFormatter(formatter)
myapp.addHandler(timefilehandler)

while True:
    time.sleep(0.1)
    myapp.info("test")
