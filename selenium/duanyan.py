#导包
import time
from selenium import webdriver 
driver=webdriver.Firefox()
url='http://www.baidu.com'  #访问百度
driver.get(url)
print("访问"+driver.current_url+"成功")
time.sleep(2)
url='http://news.baidu.com/'  #访问新闻
driver.get(url)
print("访问"+driver.current_url+"成功")
time.sleep(2)
#前进 
driver.back()
time.sleep(2)
#后退
driver.forward()
time.sleep(2)
#关闭
driver.close()