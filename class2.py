##案例1：“温度转换”问题，F表示华摄氏度，C表示摄氏度
# TempStr = input("请输入带有符号的温度值：")
# if TempStr[-1] in ['F','f']:   #索引：TempStr[-1]表示获取字符串的倒数第一个字符  使用[]获取字符串中一个或多个字符
#     C=(eval (TempStr[0:-1])-32/1.8)     #切片：返回字符串中一段字符子串  TempStr[0,-1]表示取字符串的第一个字符到最后一个字符的前一个字符之间的这些字符   【左闭右开】
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C','c']:
#     F =1.8 *eval (TempStr[0:-1])+32    #eval()函数，去掉最外侧语句并执行余下语句的函数 
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")


###获得用户输入的一个字符串，格式如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬M OP N‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬,其中，M和N是任何数字，OP代表一种操作，表示为如下四种：+, -, *, /（加减乘除）‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬,根据OP，输出M OP N的运算结果，统一保存小数点后2位。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬注意：M和OP、OP和N之间可以存在多个空格，不考虑输入错误情况。
# s =input()
# print("{:.2f}".format(eval(s)))