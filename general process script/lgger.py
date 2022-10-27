import logging


# 目标：1.实现init_logger(out_pth: str = '日志文件存放路径')，该函数返回一个logging类实例对象。
def init_logger(out_pth: str):
    '''

    :param out_pth: 日治文件存放路径
    :return: logging对象
    '''
    logger=logging.getLogger("这里写需要记录的模块名字")
    return logger

'''
logging模块
1.日志级别等级排序：critical > error > warning > info > debug

级别越高打印的日志越少，反之亦然，即

debug : 打印全部的日志( notset 等同于 debug )
info : 打印 info, warning, error, critical 级别的日志
warning : 打印 warning, error, critical 级别的日志
error : 打印 error, critical 级别的日志
critical : 打印 critical 级别

2.Logging 定义的模块级别函数
# 打印日志级别函数
当指定一个日志级别之后，会记录大于或等于这个日志级别的日志信息，小于的将会被丢弃， ==默认情况下日志打印只显示大于等于 WARNING 级别的日志。==
logging.debug('Python debug')
logging.info('Python info')
logging.warning('Python warning')
logging.error('Python Error')
logging.critical('Python critical')

3.设置日志显示级别
通过 logging.basicConfig() 可以设置 root 的日志级别，和日志输出格式。
注意：Logging.basicConfig() 需要在开头就设置，在中间设置并无作用

logging.basicConfig(level=logging.DEBUG)
logging.debug('Python debug')
logging.info('Python info')
logging.warning('Python warning')
logging.error('Python Error')
logging.critical('Python critical')

4.将日志信息记录到文件
logging.basicConfig(filename='F:/example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

5.显示消息日期
# 显示消息时间
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')

6.longging模块之logger

Logger 持有日志记录器的方法，日志记录器不直接实例化，而是通过模块级函数 logger.getlogger (name) 来实例化,使用相同的名称多次调用 getLogger() 总是会返回对相同 Logger 对象的引用。

应用程序代码能直接调用日志接口。
Logger最常用的操作有两类：配置和发送日志消息。
初始化 logger = logging.getLogger("endlesscode")，获取 logger 对象，getLogger() 方法后面最好加上所要日志记录的模块名字，配置文件和打印日志格式中的 %(name)s 对应的是这里的模块名字，如果不指定name则返回root对象。
logger.setLevel(logging.DEBUG)，Logging 中有 NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL这几种级别，日志会记录设置级别以上的日志
多次使用相同的name调用 getLogger 方法返回同一个 looger 对象；
Logger是一个树形层级结构，在使用接口 debug，info，warn，error，critical 之前必须创建 Logger 实例：

创建方法: logger = logging.getLogger(logger_name)
创建Logger实例后，可以使用以下方法进行日志级别设置，增加处理器 Handler：

logger.setLevel(logging.ERROR) # 设置日志级别为 ERROR，即只有日志级别大于等于 ERROR 的日志才会输出
logger.addHandler(handler_name) # 为 Logger 实例增加一个处理器
logger.removeHandler(handler_name) # 为 Logger 实例删除一个处理器

四大模块关系：
简明了说就是：日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。

Logger 可以包含一个或多个 Handler 和 Filter
Logger 与 Handler 或 Fitler 是一对多的关系
一个 Logger 实例可以新增多 个 Handler，一个 Handler 可以新增多个格式化器或多个过滤器，而且日志级别将会继承。
'''