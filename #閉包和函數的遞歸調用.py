#閉包和函數的遞歸調用
#使用閉包(函數的嵌套)

def func_lib():
    def add (x,y):
        return x+y
    return add    #返回函數對象

fadd = func_lib()
print(fadd(1,2))


#遞歸調用
def f(x):
    if x ==1:
        return 1
    else:
        return(f(x-1)+x*x)
print(f(5))