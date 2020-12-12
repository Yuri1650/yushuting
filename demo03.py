# # #判断
# # a = 1
# # b = 2
# # if a>b:
# #     print("a比b大")
# # else:
# #     print("b更大")


# # age = int(input("请输入你的年龄:"))
# # if age > 60:
# #     print("老了")
# # elif age > 50:
# #     print("年过半百")
# # elif age > 30:
# #     print("责任重大")
# # elif age > 20:
# #     print("正值年华")
# # else:
# #     print("小年轻")

# #--------------------------------  
# # a = "你好"
# # if a in ["你好","你吃了么"]:
# #     print("ok")
# # else:
# #     print("no ok")

# # a = "dadlfaj"
# # if type(a) is int:
# #     print("是数字！")
# # elif type(a) is str:
# #     print("是字符串")
# # else:
# #     print("其他")


# # a = 1
# # while a < 10:
# #     print("哈哈哈哈哈哈")
# #     a = a+1

# """
# 练习：
# 现在有十个学生的成绩，需要录入到系统中
# 这十个人分别是，张三、李四、哈哈、嘿嘿、喜喜、嘟嘟、嘎嘎、叽叽、喳喳、笨笨
# 并且名字和成绩需要对应上
# 而且大于60的和小于60的需要分开存放
# """
# highchengji = {}
# lowchengji = {}
# studentlist = ["张三","李四","哈哈","嘿嘿","喜喜","嘟嘟","嘎嘎","叽叽","喳喳","笨笨"]
# a = 0
# while a <len(studentlist):
#     chengji = int(input("请输入" + studentlist[a] + "的成绩:"))
#     if chengji >=60:
#         highchengji[studentlist[a]]=chengji
#     else:
#         lowchengji[studentlist[a]]=chengji
#     a = a+1
# print(highchengji)
# print(lowchengji)

# #for循环 遍历
 
# a = "你好，今天你吃了吗？"

# for i in a :
#     print(i)


# b = list(range(0，100，2))  #自动生成了一个数列，步进/步长
# print(b)

"""
打印99乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end="  ")
    print()




  