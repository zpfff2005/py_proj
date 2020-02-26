from selenium import webdriver
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
def k_press(a):
    keyboard.press(a)
    keyboard.release(a)

def bt(a, b):
    keyboard.press(a)
    keyboard.press(b)
    keyboard.release(b)
    keyboard.release(a)

try:
    a = '2201599311'
    b = 'msm20041023'
    browser = webdriver.Chrome()
    bt(Key.cmd, 'l')
    time.sleep(1)
    keyboard.type('chrome://settings/content/siteDetails?site=https%3A%2F%2Fcdn.ssjj.iwan4399.com')
    k_press(Key.enter)
    time.sleep(1)
    for i in range(25):
        k_press(Key.tab)
    k_press(Key.space) 
    k_press(Key.down)
    k_press(Key.down)
    time.sleep(0.1)
    k_press(Key.enter)
    #bt(Key.cmd, 'w')
    """browser.get("http://ssjj.4399.com/")
    browser.switch_to.frame("flash22")
    browser.switch_to.frame("popup_login_frame")
    browser.find_element_by_id("username").send_keys(a)
    browser.find_element_by_id("j-password").send_keys(b + '\n')
    time.sleep(2)
    browser.switch_to.parent_frame()
    browser.find_element_by_id('3_1').click()"""
finally:
    time.sleep(3)
    #browser.quit()