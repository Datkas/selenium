from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass

login = 'rysbek_uulu.2018@stud.nstu.ru'
password = getpass.getpass('Введите пароль: ')

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://nstu.ru")
time.sleep(2)

btn_login = driver.find_element_by_css_selector('div.header__login>a')

btn_login.click()

time.sleep(1)

btn_kabinet = driver.find_element_by_xpath('//a[text () = "Кабинет обучающегося"]')
btn_kabinet.click()

time.sleep(2)

input_login = driver.find_element_by_name('callback_0')
input_password = driver.find_element_by_name('callback_1')

input_login.send_keys(login)
input_password.send_keys(password)

input_password.send_keys(Keys.RETURN)

time.sleep(2)
btn_progress = driver.find_element_by_css_selector("#menuID>div>#ctSubTreeID3+table")


btn_progress.click()

time.sleep(2)
btn_progress1 = driver.find_element_by_css_selector("#ctSubTreeID4>table+table>tbody>tr>td+td+td>a")


btn_progress1.click()

time.sleep(2)

btn_dis = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/table[1]/tbody/tr")

rc = len(btn_dis)
a =""
for i in range(2, rc + 1):
    d = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table[1]/tbody/tr["+str(i)+"]/td[2]").text
    a = a + "    " + d

import json 

dic = {"list:" : a}

jsontext = json.dumps(dic)

with open("List", "w") as f:
    f.write(jsontext)
    
time.sleep(10)
driver.close()