"""異常特點
    1.停止執行
    2.向上傳播
    3.打印標準錯誤"""

"""for i in range(5):
    if i == 3:
        raise ValueError #引發任意異常
    print(i)
    """

"""for i in range(5):
    if i == 3:
        assert 1 == 2
        print(i)"""


"""異常處理的目的在於，儅程序出現異常時，程序依舊在代碼的控制之中，而不是立刻結束
通常可以完成數據的備份，日志和進度的記錄，甚至重新執行程序（失敗重試是測試常用的功能）"""

try:

    for i in range(5):
        if i ==3:
            raise ValueError("沒事抛個異常")
        print(i)

except Exception as e:
    print(f"{type(e)}:{e}")


"""这段 Python 代码主要用于演示异常处理机制，以下逐行讲解核心逻辑：
1. 代码结构与功能总览
代码通过 try-except 语法捕获并处理程序运行时的异常，目的是展示 “当程序抛出异常时，如何用 try-except 控制流程，避免程序直接崩溃”。
2. 逐部分拆解
try 块：
Python 中，try 用于包裹 “可能抛出异常的代码”。你可以把不确定是否会报错的逻辑（比如网络请求、数据转换）放在这里。
except 块：

except Exception as e:
    print(f"{type(e)}: {e}")


except 用于捕获异常，一旦 try 里的代码抛出异常，就会跳转到 except 执行。
Exception 是 Python 里 “所有常规异常的父类”，写 except Exception 可以捕获绝大多数异常（也可针对性捕获 ValueError、TypeError 等具体类型）。
as e 把捕获到的异常对象存到变量 e，方便后续处理：
type(e) 会输出异常的类型（比如这里的 ValueError）。
e 直接输出异常的提示文本（比如 "没事抛个异常"）。
最终格式像 "<class 'ValueError'>: 没事抛个异常"。"""



#Exception絕大部異常的父類，可以捕捉大部分異常
#BaseException所有異常的祖父類，可以捕捉到全部的異常