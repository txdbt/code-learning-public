#字典---------一批數據，可用key檢索鍵 的儲存場景（不支持下標索引
#字典創建--基本語法
#d={key1:value1,key2:value2}

dict = {'xmj':40,'zhang':91}


#修改字典
stu_dict={'class':'軟件五班','stu_num':31,'age':17}
stu_dict['age']=18         #更新字典元素
stu_dict['height']  =188   #增加新值
print(stu_dict)

#in運算--查詢字典是否有某鍵
print('height'in stu_dict)