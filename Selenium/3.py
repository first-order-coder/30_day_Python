from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.daraz.lk/#')
driver.maximize_window()

search = driver.find_element(By.ID, 'q')
search.send_keys('apple')
search.send_keys(Keys.RETURN)

item  = driver.find_element(By.LINK_TEXT, "Apple iPhone 14 Pro Max")

action = ActionChains(driver)
action.scroll_to_element(item)
# action.context_click(on_element= item)
action.click(item)
action.perform()
time.sleep(20)
