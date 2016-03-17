# from pyvirtualdisplay import Display
# from selenium import webdriver
#
# display = Display(visible=0, size=(800, 600))
# display.start()
# driver = webdriver.Chrome()
# driver.get('http://christopher.su')
# print driver.title

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.zhkd.com/terminal/admin/login")

#login
element_user_name = driver.find_element_by_xpath("//input[@name='user_name']")
element_user_name.send_keys("Admin")
element_user_password = driver.find_element_by_xpath("//input[@name='user_password']")
element_user_password.send_keys("admin")
btn=driver.find_element_by_xpath("//button[@type='submit']")
btn.submit()

time.sleep(5)
#choose desk
element_desk = driver.find_element_by_xpath("//div[@class='desk_box TabContent the_all']//li[@class='taihao_li not_move']")
element_desk.click()

#choose people
element_people = driver.find_element_by_xpath("//div[@class='jianpan-number'][1]")
element_people.click()

#make order
element_btn=driver.find_element_by_xpath("//div[@class='btn kt_btn'][1]")
element_btn.click()

#choose cat
element_cat=driver.find_element_by_xpath("//ul[@id='myTab2']//li[@class='normal'][2]")
element_cat.click()

#choose dish
element_dish=driver.find_element_by_xpath("//div[@class='nTab']//div[@style='display: block;']//li[@class='dishes_item relevant_li discountable'][1]")
element_dish.click()

#submit order
element_btn=driver.find_element_by_xpath("//div[@class='btn sm_cart']")
element_btn.click()

# driver.close()