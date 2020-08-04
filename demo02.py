print("----------判断和循环--------------")
"""
a=input("请输入a的值：")
b=input("请输入b的值：")
if a > b:
    print("a比b大")
else:
    print("b比a大")
"""


#age=23
# age=int(input("请输入你的年龄："))
# if age>60:
#     print("可以退休了")
# elif age>30:
#     print("上有老下有小的阶段")
# elif age>20:
#     print("初入职场，需要规划")
# else:
#     print("读书的时候，要认真")


"""
age=int(input("请输入你的年龄："))
if age>=20 and age <30:    # 20<age<30
    print("22222")
elif age>=30 and age <60:
    print("333333")
elif age>60:
    print("666666")
else:
    print("111111")
"""
####判断条件：==、！=、<、>、 in、not in、not is

# a="你好"
# if a in "你好，最近怎么样？":
#     print("ok")
# else:
#     print("not ok")

###in的用法####
# a=input("请输入：")
# if a in "0123456789"
#     a=int(a)
# else:
#     print("请输入正确的数字")
#     exit()
# if a>5:
#     print("大")
# else:
#     print("小")

###is的用法###
# a="dessfg"
# if type(a) is int:
#     print("a是数字")
# elif type(a) is str:
#     print("a是字符串")
# else:
#     print("其他")


# a=1
# while a<10:
#     print("hahha",a)
#     a=a+2


""" 练习：现在有10个学生的成绩，需要录入到系统中，分别是A,B,C,D,E,F,G,H,I,J 并且名字和成绩需要对应上，并且大于60和小于60的需要分开存放  """
# s={}
# t={}
# studentlist=["A","B","C","D","E","F","G","H","I","J"]
# a=0
# while a<len(studentlist):
#     #print(a)
#     chengji=int(input("请输入"+studentlist[a]+"的成绩："))
#     if(chengji>=60):
#         s[studentlist[a]]=chengji
#     else:
#         t[studentlist[a]]=chengji
#     a=a+1
# print("大于60的：",s)
# print("小于60的：",t)


##遍历
"""
a=["A","B","C","D","E","F"]
for i in a:
    print(i)

b=list(range(0,100,2))   #自动生成一个数列，0~99，第三个参数是步长，默认为1
for i in range(10):
    print(i)
"""
#使用for循环实现上个练习题
"""
s={}
t={}
studentlist=["A","B","C","D","E","F","G","H","I","J"]
for i in studentlist:
    chengji=int(input("请输入"+i+"的成绩："))
    if(chengji>=60):
        s[i]=chengji
    else:
        t[i]=chengji

print("大于60的：",s)
print("小于60的：",t)
"""
"""
##打印99乘法表###
for i in range(1,10):
    for i in range(1,i+1):
        print(i,"x",j,"=",i*j,end=" ")
    print()
"""
"""
作业1：模拟一个红绿灯，红灯打印30次  绿灯打印35次，黄灯打印3次
作业2：实现一个注册功能，用户输入账号和密码，要求长度是5-8位，密码是6-12位，并且账号必须是小写开头。
存储到字典中，{username:password}
"""

for i in range(1,31):
    print("红灯还有",i,"次")
for j in range(1,36):
    print("黄灯还有",j,"次")
for h in range(1,4):
    print("绿灯还有",h,"次")



