"""函數定義和使用

1.def 關鍵字
2.函數名：用來標識函數
3.函數體：要執行的代碼

"""
def hello():                        #hello是函數名
    print("Hello,world")            #函數體



"""函數定義好后，用call調用函數"""

hello()


def hell(name):                     #定義函數
    print(f"Hello,{name}")
    

hell("world")


"""默認函數"""
def hel(gender="girl"):             #將girl設置為默認值
    print(f"you are {gender}")

hel()
hel("boy")
hel("helicopter")                   #一定要注意！！！-----》在定義參數的時候，沒有默認值的參數必須在有默認參數的前面《--------




"""----------------------------------
   函數的默認參數并不是在每次調用函數時創建，而是在定義函數的時候創建
   所以調用多少次，就會對源列表操作多少次
   
   
   函數的默認參數應該避免使用可變的數據類型，使得每次執行的結果保持一致"""





"""不定長函數（要接受的參數非常多的時候使用）
   分爲兩類：
        不定長位置參數 *args
        不定長關鍵字參數 **kwargs
        
    在使用時遵循一個基本原則：位置參數在前，關鍵字參數在後"""

def f(*args,**kwargs):
    print(args)
    print(kwargs)

f(1,2,3)                            #都是位置參數
f(1,2,same=3)                       #最後一個是關鍵字參數
f(a=1,b=2,c=3)                      #都是關鍵字參數


"""函數的返回值"""

result11 = hello()
print(result11)                       #輸出結果None是變量result的值，也是hello（）函數的返回結果

def add (a,b):
    c= a + b
    print(f"{a}+{b}的計算結果為：",c)
    return [a,b,c]

result=add(23,45)
add(result[2],100)

"""多個返回值"""                       #注意：return 不僅僅是指定返回值，而且還會提前結束函數執行
"""若有多個内容返回，可以將他們放在一個容器類數據類型中一次性返回"""




"""變量作用域"""
#Local: 函數内部創建的變量都在局部作用域
#Enclosed:閉包作用域
#Global：未包含在任何函數中，代碼中直接創建的變量，處於全局作用域
#BuiltIn:内置作用域

input = "hi"                        #全局作用域 設置變量
import builtins                      #導入内置作用域

def f():
    input = "ffff"                  #局部作用域 設置變量
    print(locals()['input'])        #locals()以字典的形式返回局部作用域内容
    print(globals()['input'])       #globals()以字典的形式返回全局作用域内容
    print(builtins.input)           #以模塊形式返回内置作用域内容
                     

"""如何訪問各作用域的内容"""
f()



"""創建變量
        如果有局部作用域，則創建到局部作用域
        如果沒有局部則創建到全局作用域"""

def e():
    global input                    #聲明 input 為全局作用域中的内容
    input = "ffff"                  #在全局作用域設置變量


input ="hihi"                       #全局作用域 設置變量
e()
print(input)                        #在全局作用域中訪問全局變量