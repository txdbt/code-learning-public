sum_money=10000

for x in range(1,21):
    import random
    num = random.randint(1,10)
    if num<5:
        print(f"員工{x},績效分{num},不發工資，下一位")
        continue
    if sum_money >=1000:
        sum_money=sum_money-1000
        print(f"向員工{x}發放工資1000元，賬戶餘額還剩{sum_money}元")
    else:
            print("工資發完了，下個月再來吧")
            break