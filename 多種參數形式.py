"""
多種傳參形式

"""
def user_info(name,age,gender):
    print(f"name:{name},age:{age},gender:{gender}")


#位置參數 - 默認使用形式
user_info('lyh',19,'男')


#關鍵字參數
user_info(name='mike',age=13,gender='woman')
user_info(age=10,gender='girl',name='mary')
user_info('mary',gender='girl',age=1)


#缺省參數（設定默認值）
def user_info(name,age,gender='man'):
    print(f"name:{name},age:{age},gender:{gender}")

user_info('xiaotian',18,)


#不定長 - 位置不定長，*號
#不定長定義的形式參數會作爲元組存在，接收不定長數量的參數傳入
def user_info(*args):
    print(f"args參數的類型是:{type(args)},内容是:{args}")

user_info(1,2,3,'jerry','boy')


#不定長 - 關鍵字不定長， **號
def user_info(**kwargs):
    print(f"kwargs參數的類型是:{type(kwargs)},内容是:{kwargs}")

user_info(name='jelly',age=19,gender='boy',addr='beijing')


#函數作爲參數傳遞
def test_func(compute):
    result = compute(3,4)
    print(f"compute參數的類型是:{type(compute)}")
    print(f"計算結果：{result}")


def compute(x,y):
    return x*y

test_func(compute)    


#lambda匿名函數
"""
lambda 傳入參數： 函數體（一行代碼）

傳入參數表示匿名函數的形式參數

函數體就是函數的執行邏輯-----只能寫一行代碼


"""

def test_func(compute):
    result = compute(1,2)
    print(f"結果為:{result}")

test_func(lambda x,y:x + y)