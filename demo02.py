# a = (1,2,3,4,"哈哈","嘻嘻",True,False)
# print(a[4])
# # 切片
# print(a[0:4]) # 左闭右开
# print(a[7:])
# # print(a.index("嘻嘻"))
# # print(a.count(True))

# # b = (a,"哈哈","嘻嘻")
# # print(b[0][2])

# a = [1,2,3,4,"哈哈","嘻嘻",True,False]
# a.append("append")
# a.insert(0,"insert")
# print(a)
# b = a.pop(0) # 剪切
# print(b)


# a ={"name":"张三","age":25}
# # 取值
# print(a["name"])
# #新增
# a["high"]="183cm"
# print(a)
# #修改
# a["name"]= "李四"
# print(a)

# b = a.get("name")
# print(b)

# a.update(name=111)

# print("------------------------")
# del a["name"]
# print(a)

"""
练习：获取用户输入的个人信息，并且存储到字典中。
个人信息包含：name,age,sex
"""
name = input("请输入你的名字：")
age = input("请输入你的年龄：")
sex = input("请输入你的性别：")
I = {"name":name,"age":age,"sex":sex}
# I.update(name=name,age=age,sex=sex)
print(I)