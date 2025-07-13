"""————————————文件管理——————————————"""
#1，打开文件
f = open(r"F:\python\draft\test.txt", "r")                            # 如果只有文件名，则在本目录下找test.txt
print(f.read())
f.close()

"""内置函数open可以打开文件，并返回一个文件对象f。一般情况使用完f对象后，应该调用f.close()关闭文件
    关闭文件有两个好处：
        立刻将修改过的内容保存在硬盘中
        不影响其他程序使用本文件"""
#f.close的另一种写法（确实存在该文件时使用）

with open(r"F:\python\draft\test.txt", "r") as f:
    print(f.read())

"""此时python认为文件对象f的使用范围只在with语句块中，当with语句块代码执行完毕时会自动关闭文件"""

#打开模式
"""    --'r'   read      读取（默认）
       --'w'   write     写入
       --'a'   append    追加内容
       --'x'   exlusive  独占写入，如果文件存在则报错
       --'b'   binary    二进制模式
       --'t'   text      文本模式（默认）
       --'+'   扩展      扩展为读写模式             """

#实操
"""创建一个文件，文件名从标准输入获取，请注意open函数可以引发异常"""
def main():
    filename = input("请输入要创建的文件名：")

    try:
        with open(filename,"x") as f:
            print("创建成功!")
            pass
    
    except Exception as e:
        print("创建失败，文件已存在：{}".format(e))

#main()

#实操二
"""创建一个文件，并写入一下内容，然后从文件中读取最后一行内容并打印"""

def main2():
    filename = 'test.txt'

    try:
        with open(filename,mode="w",encoding="utf-8")as f:
            f.write("OK\n")
            f.write("I'm txdbt")

        with open(filename,encoding="utf-8")as f:
            content = f.readlines()
            print(content[-1])
    except Exception as e:
        print("文件打开失败：{}".format(e))

main2()



#处理CSV文件（固定格式文件）

l_1=[1,2,3]
l_2=[2,4,6]
l_3=[7,8,9]

l=[l_1,l_2,l_3]
"""当想要打印数字八时，需要2个索引表示"""

print(l[2][1])

"""数字6则为"""

print(l[1][2])