# for i in range(10):
#     if i == 4:
#         continue
#     print(i)


# 函数/方法，自定义方法

def checkname(username):
    """
    自动判断账号长度时5-8位，且账号必须以小写字母开头
    """
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
            print(ok)
        else:
            print("账号的首字母必须小写字母开头")
    else:
        print("账号长度仅支持5-8位")

#def 方法的声明
#checkname 方法的名字
#username方法的参数
#方法的逻辑代码

checkname('2343')