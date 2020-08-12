#导入webdriver
from selenium import webdriver
#创建一个浏览器对象
driver=webdriver.Firefox()
#设置全屏
driver.maximize_window()
#获取当前浏览器尺寸
size=driver.get_window_size()
print(size)
#设置浏览器尺寸
driver.set_window_size(400,400)

size=driver.get_window_size()
print(size)

# print(dir(driver))

#浏览器的位置操作
position=driver.get_window_position()
print(position)

driver.set_window_position(100,0)
#关闭浏览器
driver.close()  #关闭当前标签/窗口
driver.quit()  #关闭所有窗口/标签
