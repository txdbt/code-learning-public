name = None
name=input("請輸入你的id:\n")
money = 5000000
 
def check(show_header):
    if show_header:

        print(f"Hello,{name},you have {money} right now")
   

def saving(num):
    global money
    money += num
    print(f"Hello,{name},you just saving {num},now you have {money} total ")
    
    check(False)

def qukuan(num1):
    global money
    money -=num1
    print(f"Hello,{name},you just take out {num1},now you have {money} total ")
    
    check(False)

def home():
    print(f"welcome back {name},what do you want to do")
    print("press 1 for check your money, press 2 for saving your money, press 3 for take out your money:\n")
    return input("pls tap:")  

while True:
    keyboard_input = home()
    if keyboard_input == "1":
        check(True)
        continue
    elif keyboard_input == "2":
        num=int(input("please input the sum money you want to saving:\n"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num=int(input("please input the money you want to take out:\n"))
        qukuan(num)
        continue
    else:
        print("over now")
        break