#1.import语法
"""要在程序中使用其他文件的代码可以借助import关键字将其引入，称之为模块
模块是包含python定义和语句的文件，使用.py后缀
如果有多个模块（文件），可以使用文件夹组织起来，称之为包
包是包含其他模块，包的文件夹，并且必须有一个__init__.py文件"""

#2.标准库
#2.1csv
"""csv模块实现以CSV格式表格数据的读取和写入。提供列表的形式或字典的形式继续数据读写"""


"""创建CSV文件（以列表进行数据读写）"""
import csv

with open('test1.csv','w',newline='',encoding='utf8')as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['姓名''性别''年龄'])
    writer.writerow(['张三''男''2'])
    writer.writerow(['李四''女''18'])
    writer.writerow(['mike''男''29'])

"""读取CSV文件"""

import csv

with open('test1.csv','r',newline='',encoding="utf8")as csvfile:
    reader = csv.reader(csvfile)
    for i in reader :
        print(i)


"""以字典形式读写"""
import csv

with open('test1.csv','w',newline='',encoding="utf8")as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=['姓名','性别','年龄'])
    writer.writeheader()
    writer.writerow({'年龄':'20','姓名':'张三','性别':'male'})
    writer.writerow({'年龄':'132','姓名':'mary','性别':'female'})
    writer.writerow({'年龄':'23','姓名':'tom','性别':'male'})

"""读取CSV文件"""
import csv

with open('test1.csv','r',newline='',encoding='utf8')as csvfile:
    reader= csv.DictReader(csvfile)
    for d in reader:
        print(d)


#2.2time
"""知识点：
   epoch时间的起点，通常为1970年1月1日00:00:00
   UTC世界统一时间，全球各地的时间进行换算时，通过UTC进行统一"""

#time（）->float 返回epoch开始的秒数值
import time
print(time.time())                                                      #从1970年1月1日00:00:00到此刻的秒数

#sleep(n)程序休眠n秒
print(time.time()); time.sleep(2); print(time.time())                   #两次输入中间休眠了2秒

#gmtime([secs])返回epoch开始的时间值，未传递secs时使用time（）的返回值
print(time.gmtime())

#localtime返回本地时间

#strftime(format[,t])将时间格式化输出为字符串
print(time.strftime("%Y-%m-%d %H:%M:%S"))



#2.3random                                                              #伪随机

#random()最基本的随机数生成函数，返回0~1的随机浮点数
import random
random.random()

#randint(a,b) 返回一个随机整数N,满足a<=N <=b

#randrange(start,stop[,step])