"""
1。使用conda install selenium
2。安装对应浏览器的driver 搜索selenium python api  路径  https://selenium-python-zh.readthedocs.io/en/latest/api.html
3.引入webdriver
exception:
Can not connect to the Service
1.检查mac是否信赖这个exe
2。在环境变量中配置chromedriver的安装目录 ，不要指向这个exe，一定要指向它的安装目录（上层目录）
3。ping 一下localhost，如果不可以在etc/hosts 里面加入 127.0.0.1  lcoalhost
可以解决上述问题

在github上搜索ArticleSpider-resourses  可以查看源码
"""
from selenium import webdriver

path = '/Users/apple/Desktop/chromedirver'
browser = webdriver.Chrome()
url = "https://www.zhihu.com/signin"
browser.get(url)
# selenium只要知道网页元素的位置，就可以模拟浏览器的行为。
# 1.使用css样式选择器选中元素，使用set—keys输入内容
browser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys("842917077@qq.com")
browser.find_element_by_css_selector(".SignFlow-password input").send_keys("842917077@qq.com")
browser.find_element_by_css_selector(".Button.SignFlow-submitButton").click()
# 2.保存cookie
import time

# 让程序等待10秒，等待浏览器获取到cookie
time.sleep(10)
Cookies = browser.get_cookies()
import pickle

for cookie in Cookies:
    print(cookie)

browser.close()
