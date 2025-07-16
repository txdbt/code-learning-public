#日志记录
"""loggging的作用
1.调试程序：忠实记录下程序在运行过程中所发生的东西
2.方法溯源：记录历史，降低沟通成本
3.分析依据：为非技术性决策"""

"""基本用法
1，日志记录在哪
2，日志记录成什么格式
3，日志记录哪些信息
4，是否一定要使用logging记录日志"""

#先尝试再改进
import logging

logging.info("日志内容   1")
logging.warning("日志内容 2")
logging.error("我是日志内容 3")
logging.debug("日志内容 4")

"""观察：
1.
日志内容出现控制台，容易区分，和print执行结果，有差别
2.不是所有的日志内容都会出现（记录）
3.在日志内容之外，会自动添加其他的内容，然后一起显示"""

#basicConfig函数(配置日志记录)

import logging

logging.basicConfig(filename="a.txt",level=logging.debug)                   #实现了日志配置

logging.info("日志内容   1")
logging.warning("日志内容 2")
logging.error("我是日志内容 3")
logging.debug("日志内容 4")