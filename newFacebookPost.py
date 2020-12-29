#! /usr/bin/env python3

# newFacebookPost.py - Login Facebook and post a message.

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)     # 关闭左上角设置项提示
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.facebook.com/')
emailInput = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id('email'))
pwdInput = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_id('pass'))

emailInput.send_keys('freya.fu@gpower.co')
pwdInput.send_keys('123456Test', Keys.ENTER)
addNews = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_css_selector('div[aria-label="创建"]'))
addNews[0].click()

time.sleep(3)
newPost = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_css_selector('div['
                                                                                             'data-visualcompletion'
                                                                                             '="ignore-dynamic"]'))
newPost[0].click()

postContent = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_class_name('_1mf._1mj'))
postContent.send_keys('Robot Typing...')

postBtn = WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_css_selector('div[aria-label="发帖"]'))
postBtn[0].click()

time.sleep(3)
profilePage = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_link_text('Freya Fu'))
profilePage.click()

latestPost = WebDriverWait(driver, 5).until(lambda driver: driver.find_element_by_xpath("//div[contains(text(),'Robot "
                                                                                        "Typing...')]"))

driver.quit()

if latestPost is not None:
    print('Post Successfully!')
