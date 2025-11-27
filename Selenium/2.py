from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

language = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'langSelect-EN')))
language.click()

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice0' + str(i)) for i in range(1,-1)]

#predefined chain of actions which will perform in a specific sequance like a queue
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform() #from  here the above mentioned action will start to perform
    time.sleep(10)
    count = cookie_count.text.split(' ')[0]
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()