#www.dm5.com
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import re, urllib
import time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://images.baidu.com/channel/wallpaper#%E9%A3%8E%E6%99%AF&%E5%85%A8%E9%83%A8&11&0")

#elem =driver.find_element_by_id("swf1_em")

script="window.scrollBy(0,500);"
driver.execute_script(script)
time.sleep(5)
driver.execute_script(script)
time.sleep(5)
driver.execute_script(script)
time.sleep(5)
driver.execute_script(script)
time.sleep(5)
driver.execute_script(script)
time.sleep(5)

elems=driver.find_elements_by_xpath('//ul[@class="list"]//li//img')

for i in elems:
    src=i.get_attribute("src")
    print "\n"+src

    
    

    

    

 
driver.close()
driver.quit()

# print driver.window_handles
# print driver.title
# print driver.current_window_handle



#elem=driver.find_element_by_id("mb_content")
#print elem.get_attribute("codebase")
#print elem.get_attribute("pluginspage")



