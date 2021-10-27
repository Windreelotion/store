'''
    京东的登陆、淘宝登陆、苏宁的登陆脚本
    bilibili登陆脚本，搜索一个鬼畜视频并播放脚本写出来。
    做知乎的官网，并登陆，和发表一篇文章。
    企查查的官网登陆。
'''

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# 苏宁自动化登陆操作
driver = webdriver.Chrome()

driver.get("https://www.suning.com")

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/a[1]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()

driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/input').send_keys("13135992021")
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/input').send_keys("xiangyangxy123")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/div[6]/div/div/span').click()
time.sleep(5)
ac = ActionChains(driver)
ele = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/div/div[3]')
time.sleep(2)
ac.click_and_hold(ele).move_by_offset(113.8,0).perform()# 立即执行
ac.release() # 释放鼠标
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/a').click()
driver.quit()



# 知乎自动化登陆操作
driver = webdriver.Chrome()

driver.get("https://www.zhihu.com")

driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[1]/div/div[1]/form/div[2]/div/label/input').send_keys("13135992021")
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys("xiangyangxy123")
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[1]/div/div[1]/form/button').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div/button[3]/svg/g/circle').click()
# 获取所有窗口唯一标号

data = driver.window_handles   # ["s001","s002"]

driver.switch_to.window(data[1])
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[2]/div[2]/label/textarea').send_keys("半自动化登陆操作")
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[2]/div[2]/label/textarea').send_keys("123456")
driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[1]/div/div/div[1]/div[2]/div[3]/button').click()
driver.quit()