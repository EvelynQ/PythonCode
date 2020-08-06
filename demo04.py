"""
class 声明类的名字
然后类的名字首字母必须大写
面向对象编程
类里面所有的方法都必须传一个参数，叫self
"""
# class GirlFriend():
#     def __init__(self,sex,high,weigth,age,hair):
#         self.sex=sex
#         self.high=high
#         self.weigth=weigth
#         self.age=age
#         self.hair=hair
#     def singe(self,num):
#         print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weigth+"年龄"+self.age+"发型"+self.hair+"开始了自己的唱歌：")
#         if num==1:
#             print("rap")
#         elif num == 2:
#             print("情歌")
#         else:
#             print("飙高音")
#     def gramer(self):
#         """
#         技能
#         """
#         print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weigth+"年龄"+self.age+"发型"+self.hair+"开始了自己的技能：")
#         print("java,python.....各种语言都精通")
#     def work(self):
#         """
#         工作挣钱
#         """
#         print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weigth+"年龄"+self.age+"发型"+self.hair+"开始了自己的工作：")
#         print("公司CEO")


# #类的实例化
# lixiaotong=GirlFriend("男","180CM","5KG","25岁","锡纸烫")
# lixiaotong.work()
# lixiaotong.singe(2)
# lixiaotong.gramer()

class Car():
    def __init__(self,pinpai,color,neishi,jilun):
        self.pinpai=pinpai  
        self.color=color
        self.neishi=neishi
        self.jilun=jilun
    def bianxing(self):
        print("车子变身喜羊羊了")

    #zhangsan = Car("宝马","红色","四椅豪华内饰","四轮")
    #xiaoqiche.bianxing()
zhangsan=Car("11","22","33","44")
zhangsan.bianxing()
