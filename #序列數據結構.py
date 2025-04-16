#序列數據結構
#列表----------一批數據，可修改，可重複
list1=["懶覺","dick",1997,2025]


#訪問列表中值
print("list1[0]",list1[0])

#更新列表
list=['china','美國',2002,1233]
print(list[2])
print("new value available at index 2:")
list[2]="dicksuck"
print(list[2])

#刪除列表元素
#(方法一：del)
print(list)
del list[3]
print("after deleting value at index2")
print(list)
#(方法二:remove())
print(list)
list.remove('china')
print("after alter list")
print(list)
#(方法三:pop())
print(list,"----------")
list.pop()    #括號内無數時刪除最後一個元素
print(list)

#添加列表元素append(),,添加至列表末尾
print(list)
list.append(7578)
print(list)

#列表的排序——————運用内置排序方法list.sort(),和内置函數sorted()
#list.sort--對原列表進行排序
list2=[2,4,5,3,1,7]
list2.sort()
print(list2,"---------")
#sorted()----返回新的排序列表
list2=[2,4,5,3,1,7]
list3=sorted([2,4,5,4,1,7])
print("list2:",list2)
print("list3:",list3)
#排序函數中的（）裏可以接受布爾值reverse=True(降序/reverse=False（升序

#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#|           python列表的操作符
#|len([1,2,3])-------長度--------result:3
#|
#|[1,2]+[2,3]--------組合--------result:[1,2,2,3]
#|
#|['hi']*3-----------重複--------result:['hi','hi','hi']
#|
#|3 in [1,2,3]-------查詢元素----result:True
#|
#|for x in [1,2,3]: print(x,end="")---迭代----result:1,2,3
#|
#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww


#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#|
#|python列表方法和内置函數
#|
#|list.count()----統計
#|
#|list.extend()---在列表末尾一次性加入多個值
#|
#|list.reverse()---反轉列表順序
#|
#|
#|
#|
#|
#|
#|
#|
#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

