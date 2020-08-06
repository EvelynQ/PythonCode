a=input("请输入姓名：")
b=input("请输入年龄：")
try:
    if int(b) >18:
        print(a,"成年了")
    else：
        print(a,"未成年")
except:
    print("请输入正确的年龄")  #处理用户输入


import time
import random
import pymysql
pymysql.connect(host="127.0.0.1",user="root",password="123456",db="mysql")

a=random.randint(100,1000)
print(a)