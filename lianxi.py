"""
联系1:
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
联系2：
使用代码，实现一个注册的功能。用户输入账号和密码，要求账号长度5-8位，密码6-12位
并且账号必须小写开头，储存到字典中，{username:password}。 
"""

# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"秒")


username = input("请输入你的名字:")
password = input("请输入你的密码:")
if len(username)>=5 and len(username)<=8:
    if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
        if len(password)>=6 and len(password) <=12:
            print("您的账号注册成功,账号密码为:",{username,password})
        else:
            print("密码的长度仅支持6到12位")
    else:
        print("账号的首字母必须小写字母开头")
else:
    print("账号长度仅支持5-8位")