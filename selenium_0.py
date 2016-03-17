#www.dm5.com
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import re, urllib

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://www.4399.com/flash/132872_4.htm")
elem=driver.switch_to_frame("flash22")
#elem =driver.find_element_by_id("swf1_em")
elem=driver.find_element_by_id("swf1")
driver.switch_to_default_content()

driver.close()
driver.quit()

print driver.window_handles
print driver.title
print driver.current_window_handle



#elem=driver.find_element_by_id("mb_content")
#print elem.get_attribute("codebase")
#print elem.get_attribute("pluginspage")



