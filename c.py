from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://baidu.com')
browser.find_element_by_link_text('登录').click()
time.sleep(1)
browser.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
browser.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('13171281076')
browser.find_element_by_id('TANGRAM__PSP_10__password').send_keys('zpf2012\n')
